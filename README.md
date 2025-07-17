# 📦 Packer Tracker v1.1.0

A modern, user-friendly web application for tracking which packer completed which orders. Built with Python/Flask backend and clean HTML/CSS/JS frontend.

## 🚀 Quick Start

### For End Users (Packing Station Workers)
1. **Download**: `PackerTracker_Console.exe` from the `dist/` folder
2. **Run**: Double-click the executable
3. **Use**: Browser opens automatically - start tracking orders!

### For Developers
1. **Clone/Download** the project
2. **Install**: `pip install -r backend/requirements.txt`
3. **Run**: `python backend/startup.py` or use `run.bat`
4. **Build**: Use `build.bat` to create executable

## ✨ Features

### Core Functionality
- ✅ **Record Orders**: Enter packer name and order number
- 📋 **View All Orders**: See complete list of all recorded orders with packer names, order numbers, and timestamps
- 💾 **JSON Storage**: Data saved to `packer_data.json` (structured format)
- 🔔 **Smart Notifications**: Success/error messages with auto-dismiss
- 🚫 **Duplicate Prevention**: Can't record the same order twice

### User Experience
- 🎨 **Modern UI**: Beautiful gradient design with smooth animations
- 📱 **Responsive**: Works on desktop, tablet, and mobile
- 🔄 **Auto-browser**: Opens browser automatically when started
- ⚡ **Fast**: Lightweight and responsive interface
- 🎯 **Intuitive**: Simple, clean interface for quick data entry

### Technical Features
- 🏗️ **Clean Architecture**: Separated backend/frontend structure
- 🚀 **Standalone Executable**: No installation required for end users
- 🔒 **Local Only**: Runs on localhost (no network access required)
- 📊 **Data Persistence**: Automatic data saving to JSON file
- 🛠️ **Easy Maintenance**: Structured JSON-based data storage
- 🔒 **Thread-Safe**: Atomic file operations prevent data corruption

## 📁 Project Structure

```
packer_app/
├── backend/                    # Python/Flask backend
│   ├── controllers/            # Business logic
│   │   └── packer_controller.py
│   ├── models/                 # Data operations
│   │   └── database.py
│   ├── startup.py              # Main Flask application
│   ├── requirements.txt        # Python dependencies
│   └── build_exe_console.py    # Build script
├── frontend/                   # HTML/CSS/JS frontend
│   ├── resources/
│   │   ├── scripts/
│   │   │   └── index.js        # Main JavaScript
│   │   └── styles/
│   │       ├── index.css       # Main styles
│   │       └── result.css      # Results page styles
│   ├── index.html              # Main page
│   ├── orders.html             # View orders page
│   └── result.html             # Results page
├── dist/                       # Distribution files
│   ├── PackerTracker_Console.exe
│   └── Launch_PackerTracker_Console.bat
├── build.bat                   # Build script
├── run.bat                     # Development launcher
├── README.md                   # This file
└── DEPLOYMENT.md               # Deployment guide
```

## 🛠️ Development

### Prerequisites
- Python 3.7+
- Flask (installed via requirements.txt)

### Setup
```bash
# Install dependencies
pip install -r backend/requirements.txt

# Run in development mode
python backend/startup.py
# or
run.bat
```

### Building Executable
```bash
# Build standalone executable
build.bat
# or manually:
cd backend
python build_exe_console.py
```

### Architecture
- **Backend**: Flask web server with MVC pattern
- **Frontend**: Static HTML with external CSS/JS
- **Data**: Simple text file with delimited format
- **Build**: PyInstaller for standalone executable

## 📊 Data Format

Data is now stored in `packer_data.json`:
```json
{
  "John Smith": [
    {"order": "ORD-12345", "timestamp": "2024-01-15T14:30:25"},
    {"order": "ORD-12346", "timestamp": "2024-01-15T14:35:10"}
  ],
  "Jane Doe": [
    {"order": "ORD-12347", "timestamp": "2024-01-15T14:40:15"}
  ]
}
```

**Each packer name appears only once, with a list of their orders and timestamps.**

## 📋 Version History

### v1.1urrent)
- **Search & Filter**: Added search by order number, filter by packer name, and date range filtering
- **Data Validation**: Enhanced validation for packer names (non-empty) and order numbers (exactly 6digits)
- **Auto-Backup**: Automatic backup system that creates backups every 50 orders or 4 hours
- **Version Display**: Added version number display in bottom-right corner of all pages
- **Enhanced UI**: Improved search and filter controls with responsive design

### v1.0.0 **JSON Storage**: Migrated from text format to structured JSON with packer-based organization
- **Thread-Safe Operations**: Atomic file operations prevent data corruption in multi-user scenarios
- **Auto-Migration**: Automatic migration from old text format to new JSON format
- **Enhanced Data Structure**: Each packer appears once with a list of their orders

### v0.20- **New Feature**: Changed from search functionality to comprehensive order viewing
- **UI Update**: Replaced search form with tabular display of all orders
- **Enhanced UX**: Users can now see complete order history at a glance
- **Improved Layout**: Wider container and responsive table design
- **Better Navigation**: Updated link text from Search Orders" to View Orders

###v0.1.0
- **Initial Release**: Basic order recording and search functionality
- **Core Features**: Record orders, search by order number, duplicate prevention
- **Modern UI**: Clean, responsive design with gradient styling
- **Standalone Executable**: Easy deployment with PyInstaller

---

**Built with ❤️ for efficient order tracking**