from flask import Flask, render_template, request, redirect, url_for, flash
import webbrowser
import threading
import time
import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from controllers.packer_controller import PackerController

if hasattr(sys, '_MEIPASS'):
    base_path = sys._MEIPASS # type: ignore
else:
    base_path = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__,
            template_folder=os.path.join(base_path, 'frontend'),
            static_folder=os.path.join(base_path, 'frontend', 'resources'))
app.secret_key = 'your-secret-key-here'  # Required for flash messages

# Initialize controller
packer_controller = PackerController()

def open_browser():
    """Open browser after a short delay to ensure Flask is running"""
    time.sleep(1.5)  # Wait for Flask to start
    webbrowser.open('http://localhost:5000')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    packer_name = request.form.get('packer_name', '').strip()
    order_number = request.form.get('order_number', '').strip()
    
    success = packer_controller.submit_order(packer_name, order_number)
    
    if success:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/orders')
def orders():
    orders = packer_controller.get_all_orders()
    return render_template('orders.html', orders=orders)

if __name__ == '__main__':
    # Start browser in a separate thread
    threading.Thread(target=open_browser, daemon=True).start()
    
    print("🚀 Starting Packer Tracker...")
    print("📦 Application will open in your browser automatically")
    print("🔄 Keep this window open while using the application")
    print("❌ Close this window to stop the application")
    print("-" * 50)
    
    # Run the Flask app
    app.run(debug=False, host='localhost', port=5000)
