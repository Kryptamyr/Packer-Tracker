import os
from datetime import datetime

class PackerDatabase:
    """Database model for packer tracking data"""
    
    def __init__(self, data_file='packer_data.txt'):
        self.data_file = data_file
        self.ensure_data_file()
    
    def ensure_data_file(self):
        """Ensure the data file exists"""
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as f:
                f.write('')  # Create empty file
    
    def save_packer_data(self, packer_name, order_number):
        """Save packer data to file"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.data_file, 'a') as f:
            f.write(f"{packer_name}|{order_number}|{timestamp}\n")
    
    def load_packer_data(self):
        """Load all packer data from file"""
        data = []
        with open(self.data_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split('|')
                    if len(parts) >= 3:
                        data.append({
                            'packer_name': parts[0],
                            'order_number': parts[1],
                            'timestamp': parts[2]
                        })
        return data
    
    def find_packer_by_order(self, order_number):
        """Find packer by order number"""
        data = self.load_packer_data()
        for entry in data:
            if entry['order_number'] == order_number:
                return entry
        return None
    
    def order_exists(self, order_number):
        """Check if order number already exists"""
        return self.find_packer_by_order(order_number) is not None
    
    def get_all_orders(self):
        """Get all orders with packer information"""
        return self.load_packer_data()
    
    def get_orders_by_packer(self, packer_name):
        """Get all orders for a specific packer"""
        data = self.load_packer_data()
        return [entry for entry in data if entry['packer_name'].lower() == packer_name.lower()]
    
    def get_recent_orders(self, limit=10):
        """Get recent orders (most recent first)"""
        data = self.load_packer_data()
        return sorted(data, key=lambda x: x['timestamp'], reverse=True)[:limit] 