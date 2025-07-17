import os
import json
import tempfile
from datetime import datetime
from threading import Lock

class PackerDatabase:
    """Database model for packer tracking data with JSON storage and thread-safe operations"""
    
    def __init__(self, data_file='packer_data.json'):
        self.data_file = data_file
        self.lock = Lock()  # Thread safety lock
        self.ensure_data_file()
    
    def ensure_data_file(self):
        """Ensure the data file exists with proper JSON structure"""
        if not os.path.exists(self.data_file):
            # Create empty JSON structure
            empty_data = {}
            self._atomic_write(empty_data)
    
    def _atomic_write(self, data):
        """Thread-safe atomic write operation using temporary file and rename"""
        with self.lock:
            # Create temporary file in the same directory
            temp_file = tempfile.NamedTemporaryFile(
                mode='w',
                dir=os.path.dirname(self.data_file),
                delete=False,
                suffix='.tmp'
            )
            
            try:
                # Write data to temporary file
                json.dump(data, temp_file, indent=2, ensure_ascii=False)
                temp_file.flush()
                os.fsync(temp_file.fileno())  # Ensure data is written to disk
                temp_file.close()
                
                # Atomic replace operation
                os.replace(temp_file.name, self.data_file)
                
            except Exception as e:
                # Clean up temporary file on error
                try:
                    os.unlink(temp_file.name)
                except:
                    pass
                raise e
    
    def _load_data(self):
        """Load JSON data from file with error handling"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Return empty structure if file doesn't exist or is corrupted
            return {}
    
    def save_packer_data(self, packer_name, order_number):
        """Save packer data to JSON file with thread safety"""
        timestamp = datetime.now().isoformat()
        
        # Load current data
        data = self._load_data()
        
        # Initialize packer if not exists
        if packer_name not in data:
            data[packer_name] = []
        
        # Add new order
        order_entry = {
            "order": order_number,
            "timestamp": timestamp
        }
        
        data[packer_name].append(order_entry)
        
        # Atomic write back to file
        self._atomic_write(data)
    
    def load_packer_data(self):
        """Load all packer data from JSON file in flat format for compatibility"""
        data = self._load_data()
        flat_data = []
        
        for packer_name, orders in data.items():
            for order in orders:
                flat_data.append({
                    'packer_name': packer_name,
                    'order_number': order['order'],
                    'timestamp': order['timestamp']
                })
        
        return flat_data
    
    def find_packer_by_order(self, order_number):
        """Find packer by order number"""
        data = self._load_data()
        
        for packer_name, orders in data.items():
            for order in orders:
                if order['order'] == order_number:
                    return {
                        'packer_name': packer_name,
                        'order_number': order['order'],
                        'timestamp': order['timestamp']
                    }
        return None
    
    def order_exists(self, order_number):
        """Check if order number already exists"""
        return self.find_packer_by_order(order_number) is not None
    
    def get_all_orders(self):
        """Get all orders with packer information in flat format"""
        return self.load_packer_data()
    
    def get_orders_by_packer(self, packer_name):
        """Get all orders for a specific packer"""
        data = self._load_data()
        packer_orders = data.get(packer_name, [])
        
        return [
            {
                'packer_name': packer_name,
                'order_number': order['order'],
                'timestamp': order['timestamp']
            }
            for order in packer_orders
        ]
    
    def get_recent_orders(self, limit=10):
        """Get recent orders (most recent first)"""
        data = self.load_packer_data()
        return sorted(data, key=lambda x: x['timestamp'], reverse=True)[:limit]
    
    def get_packer_statistics(self):
        """Get statistics for all packers"""
        data = self._load_data()
        stats = {}
        
        for packer_name, orders in data.items():
            stats[packer_name] = {
                'total_orders': len(orders),
                'orders': orders
            }
        
        return stats
    
    def migrate_from_txt(self, txt_file='packer_data.txt'):
        """Migrate data from old text format to new JSON format"""
        if not os.path.exists(txt_file):
            return False
        
        try:
            # Load old data
            old_data = []
            with open(txt_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        parts = line.split('|')
                        if len(parts) >= 3:
                            old_data.append({
                                'packer_name': parts[0],
                                'order_number': parts[1],
                                'timestamp': parts[2]
                            })
            
            # Convert to new JSON format
            new_data = {}
            for entry in old_data:
                packer_name = entry['packer_name']
                if packer_name not in new_data:
                    new_data[packer_name] = []
                
                new_data[packer_name].append({
                    'order': entry['order_number'],
                    'timestamp': entry['timestamp']
                })
            
            # Write new format
            self._atomic_write(new_data)
            
            # Backup old file
            backup_file = f"{txt_file}.backup"
            os.rename(txt_file, backup_file)
            
            return True          
        except Exception as e:
            print(f"Migration failed: {e}")
            return False 