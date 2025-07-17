import os
import json
import tempfile
import shutil
from datetime import datetime, timedelta
from threading import Lock

class PackerDatabase:
    """Database model for packer tracking data with JSON storage and thread-safe operations"""
    
    def __init__(self, data_file='packer_data.json'):
        self.data_file = data_file
        self.lock = Lock()  # Thread safety lock
        self.backup_config = {
            'backup_every_orders': 50,  # Backup every 50 orders
            'backup_every_hours': 4,    # Backup every 4 hours
            'max_backups': 10       # Keep last 10 backups
        }
        self.order_count = 0
        self.last_backup_time = None
        self.ensure_data_file()
        self._load_backup_state()
    
    def _load_backup_state(self):
        """Load backup state from file if exists"""
        backup_state_file = f"{self.data_file}.backup_state"
        try:
            if os.path.exists(backup_state_file):
                with open(backup_state_file, 'r') as f:
                    state = json.load(f)
                    self.order_count = state.get('order_count', 0)
                    last_backup = state.get('last_backup_time')
                    if last_backup:
                        self.last_backup_time = datetime.fromisoformat(last_backup)
        except Exception:
            # If backup state file is corrupted, start fresh
            self.order_count = 0
            self.last_backup_time = None
    
    def _save_backup_state(self):
        """Save backup state to file"""
        backup_state_file = f"{self.data_file}.backup_state"
        state = {
            'order_count': self.order_count,
            'last_backup_time': self.last_backup_time.isoformat() if self.last_backup_time else None
        }
        try:
            with open(backup_state_file, 'w') as f:
                json.dump(state, f)
        except Exception as e:
            print(f"Warning: Could not save backup state: {e}")
    
    def _should_create_backup(self):
        """Check if backup should be created based on config"""
        now = datetime.now()
        
        # Check order count
        if self.order_count >= self.backup_config['backup_every_orders']:
            return True
        
        # Check time interval
        if self.last_backup_time:
            time_diff = now - self.last_backup_time
            if time_diff >= timedelta(hours=self.backup_config['backup_every_hours']):
                return True
        
        return False
    
    def _create_backup(self):
        """Create a backup of the current data file"""
        if not os.path.exists(self.data_file):
            return
        
        try:
            # Create backup filename with timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_dir = 'backups'
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)
            
            backup_file = os.path.join(backup_dir, f'packer_data_backup_{timestamp}.json')
            
            # Copy current file to backup
            shutil.copy2(self.data_file, backup_file)
            
            # Update backup state
            self.order_count = 0
            self.last_backup_time = datetime.now()
            self._save_backup_state()
            
            # Clean up old backups
            self._cleanup_old_backups()
            
            print(f"✅ Backup created: {backup_file}")
            
        except Exception as e:
            print(f"❌ Backup failed: {e}")
    
    def _cleanup_old_backups(self):
        """Keep only the most recent backups"""
        backup_dir = 'backups'
        if not os.path.exists(backup_dir):
            return
        
        try:
            # Get all backup files
            backup_files = []
            for file in os.listdir(backup_dir):
                if file.startswith('packer_data_backup_') and file.endswith('.json'):
                    file_path = os.path.join(backup_dir, file)
                    backup_files.append((file_path, os.path.getmtime(file_path)))
            
            # Sort by modification time (newest first)
            backup_files.sort(key=lambda x: x[1], reverse=True)
            
            # Remove old backups
            if len(backup_files) > self.backup_config['max_backups']:
                for file_path, _ in backup_files[self.backup_config['max_backups']:]:
                    try:
                        os.remove(file_path)
                        print(f"🗑️ Removed old backup: {file_path}")
                    except Exception as e:
                        print(f"Warning: Could not remove old backup {file_path}: {e}")
                        
        except Exception as e:
            print(f"Warning: Could not cleanup old backups: {e}")
    
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
        """Save packer data to JSON file with thread safety and auto-backup"""
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
        
        # Update order count and check for backup
        self.order_count += 1
        if self._should_create_backup():
            self._create_backup()
        else:
            self._save_backup_state()
    
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