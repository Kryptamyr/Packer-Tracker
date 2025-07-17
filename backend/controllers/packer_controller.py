from flask import flash, redirect, url_for
import sys
import os

# Add the backend directory to the path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.database import PackerDatabase

class PackerController:
    """Controller for packer-related operations"""
    
    def __init__(self):
        self.db = PackerDatabase()
        # Attempt migration from old format if needed
        self._migrate_if_needed()
    
    def _migrate_if_needed(self):
        """Attempt to migrate from old text format to new JSON format if needed"""
        old_file = 'packer_data.txt'
        if os.path.exists(old_file) and not os.path.exists(self.db.data_file):
            print("🔄 Migrating from old text format to new JSON format...")
            if self.db.migrate_from_txt(old_file):
                print("✅ Migration completed successfully!")
                print(f"📁 Old data backed up as {old_file}.backup")
            else:
                print("❌ Migration failed. Using new format with empty data.")
    
    def submit_order(self, packer_name, order_number):
        """Submit a new order with validation"""
        # Validate input
        if not packer_name or not packer_name.strip():
            flash('Please enter a packer name.', 'error')
            return False
        
        if not order_number or not order_number.strip():
            flash('Please enter an order number.', 'error')
            return False
        
        packer_name = packer_name.strip()
        order_number = order_number.strip()
        
        # Check if order already exists
        if self.db.order_exists(order_number):
            existing = self.db.find_packer_by_order(order_number)
            if existing:
                flash(f'Order number {order_number} has already been recorded by {existing["packer_name"]}.', 'error')
            return False
        
        # Save the order
        try:
            self.db.save_packer_data(packer_name, order_number)
            flash(f'Successfully recorded! Packer {packer_name} completed order {order_number}.', 'success')
            return True
        except Exception as e:
            flash(f'Error saving order: {str(e)}', 'error')
            return False
    
    def search_order(self, order_number):
        """Search for an order by order number"""
        # Input validation is handled in the route
        order_number = order_number.strip()
        return self.db.find_packer_by_order(order_number)
    
    def get_recent_orders(self, limit=10):
        """Get recent orders for display"""
        return self.db.get_recent_orders(limit)
    
    def get_orders_by_packer(self, packer_name):
        """Get all orders for a specific packer"""
        if not packer_name or not packer_name.strip():
            return []
        
        return self.db.get_orders_by_packer(packer_name.strip())
    
    def get_all_orders(self):
        """Get all orders"""
        return self.db.get_all_orders() 
    
    def get_packer_statistics(self):
        """Get statistics for all packers"""
        return self.db.get_packer_statistics() 
    
    def get_packer_names(self):
        """Get a list of all packer names"""
        stats = self.get_packer_statistics()
        return sorted(stats.keys()) 