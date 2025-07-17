# 📦 Packer Tracker v1.1.0, user-friendly web application for tracking which packer completed which orders.

**Designed for network storage deployment with centralized data access.**

## 🚀 Quick Start

### For End Users (Packing Station Workers)
1. **Access**: Use the desktop/taskbar shortcut provided by your supervisor
2. **Run**: Click the shortcut - browser opens automatically
3. **Start**: Start tracking orders - data saves to network storage

### For Administrators
1. **Deploy**: Copy `PackerTracker_Console.exe` to `\\Compliance\PackerTracker\`
2. **Setup**: Create shortcuts on packer station desktops pointing to the network executable
3. **Configure**: Ensure network permissions allow read/write access to the PackerTracker folder
4. **Test**: Verify all stations can access and save data

### For Developers
1. **Clone/Download** the project
2. **Install**: `pip install -r backend/requirements.txt`
3. **Run**: `python backend/startup.py` or use `run.bat`
4. **Build**: Use `build.bat` to create executable

## ✨ Features

### Core Functionality
- ✅ **Record Orders**: Enter packer name and order number
- 📋 **View All Orders**: See complete list of all recorded orders with packer names, order numbers, and timestamps
- 🔍 **Search & Filter**: Search by order number, filter by packer name, and date range filtering
- 💾 **JSON Storage**: Data saved to `packer_data.json` (structured format)
- 🔒 **Thread-Safe**: Atomic file operations prevent data corruption in multi-user scenarios
- 🔔 **Smart Notifications**: Success/error messages with auto-dismiss
- 🚫 **Duplicate Prevention**: Cant record the same order twice
- 🔄 **Auto-Backup**: Automatic backup system every 50 orders or 4 hours

### Network Features
- 🌐 **Centralized Storage**: All data stored on Compliance network storage
- 🔗 **Multi-Station Access**: Any computer with network access can view data
- 📁 **Shared Backups**: Automatic backups stored in network location
- ⚡ **Real-Time Sync**: Changes visible immediately across all stations

### User Experience
- 🎨 **Modern UI**: Beautiful gradient design with smooth animations
- 📱 **Responsive**: Works on desktop, tablet, and mobile
- 🔄 **Auto-browser**: Opens browser automatically when started
- ⚡ **Fast**: Lightweight and responsive interface
- 🎯 **Intuitive**: Simple, clean interface for quick data entry

### Technical Features
- 🏗️ **Clean Architecture**: Separated backend/frontend structure
- 🚀 **Standalone Executable**: No installation required for end users
- 🔒 **Network-Ready**: Optimized for network storage deployment
- 📊 **Data Persistence**: Automatic data saving to JSON file
- 🛠️ **Easy Maintenance**: Structured JSON-based data storage
- 🔒 **Thread-Safe**: Atomic file operations prevent data corruption

## 📁 Project Structure

```
PackerTracker/                    # Network storage folder
├── PackerTracker_Console.exe     # Main executable
├── packer_data.json             # Data file (auto-created)
├── backups/                     # Auto-backup folder
│   ├── packer_data_backup_2025116_143022.json
│   └── packer_data_backup_20251163045on
└── packer_data.json.backup_state # Backup tracking file

packer_app/                      # Development folder
├── backend/                     # Python/Flask backend
│   ├── controllers/             # Business logic
│   │   └── packer_controller.py
│   ├── models/                  # Data operations
│   │   └── database.py
│   ├── startup.py               # Main Flask application
│   ├── requirements.txt         # Python dependencies
│   └── build_exe_console.py     # Build script
├── frontend/                    # HTML/CSS/JS frontend
│   ├── resources/
│   │   ├── scripts/
│   │   │   ├── index.js         # Main JavaScript
│   │   │   └── orders.js        # Orders page JavaScript
│   │   └── styles/
│   │       └── index.css        # Main styles
│   ├── index.html               # Main page
│   └── orders.html              # View orders page
├── build.bat                    # Build script
├── run.bat                      # Development launcher
├── README.md                    # This file
└── DEPLOYMENT.md                # Deployment guide
```

## 🌐 Network Deployment

### Network Storage Setup
1. **Create Network Folder**: `\\Compliance\PackerTracker\`
2. **Copy Executable**: Place `PackerTracker_Console.exe` in the network folder
3. **Set Permissions**: Ensure all users have read/write access to the folder
4. **Create Shortcuts**: On each packer station desktop/taskbar pointing to `\\Compliance\PackerTracker\PackerTracker_Console.exe`

### Benefits of Network Storage
- **Centralized Data**: All orders saved in one location
- **Multi-Station Access**: Any computer can view all data
- **Automatic Backups**: Backups stored on network for safety
- **Easy Management**: Single location for updates and maintenance
- **Real-Time Sharing**: Changes visible immediately across all stations

### Network Requirements
- **Network Access**: All stations must have access to `\\Compliance\`
- **Permissions**: Read/write access to PackerTracker folder
- **Stability**: Reliable network connection for data saving
- **Bandwidth**: Minimal bandwidth required (local web interface)

## 🛠️ Development

### Prerequisites
- Python 3.7- Flask (installed via requirements.txt)

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
- **Data**: JSON file with structured format
- **Network**: Optimized for network storage access
- **Build**: PyInstaller for standalone executable

## 📊 Data Format

Data is now stored in `packer_data.json`:
```json
{
  "John Smith": [
    {"order": "ORD-123456", "timestamp": "2024-01-15T14:30:25.000000"},
    {"order": "ORD-123456", "timestamp": "2024-01-15T14:35:10.000000"}
  ],
 "Jane Doe": [
    {"order": "ORD-123456", "timestamp": "2024-01-15T14:40:15.000000"}
  ]
}
```

**Each packer name appears only once, with a list of their orders and timestamps.**

## 🔧 Configuration

### Network Configuration
- **Network Path**: `\\Compliance\PackerTracker\`
- **Data File**: `packer_data.json` (auto-created)
- **Backup Folder**: `backups\` (auto-created)
- **Permissions**: Read/write access for all users

### Environment Variables
- `FLASK_SECRET_KEY`: Secret key for sessions (default: auto-generated)
- `DATA_FILE`: Path to data file (default: `packer_data.json`)

### Port Configuration
- Default port: 5000 Change in `backend/startup.py` if needed

## 🚨 Troubleshooting

### Network Issues

**Can't access network folder:**
- Check network connectivity
- Verify user permissions
- Contact network administrator

**Data not saving to network:**
- Check network folder permissions
- Ensure stable network connection
- Verify folder is not read-only

**Multiple users can't access simultaneously:**
- This is normal - the app is designed for this
- Thread-safe operations prevent data corruption
- Each user gets their own browser session

### Common Issues

**Executable won't start:**
- Check if port 50available
- Ensure antivirus isn't blocking the file
- Try running as administrator

**Browser doesnt open:**
- Check default browser settings
- Manually navigate to `http://localhost:5000`

**Data not saving:**
- Check network folder write permissions
- Ensure antivirus isn't blocking file creation
- Verify network connection is stable

**Import errors:**
- Rebuild executable with `build.bat`
- Check Python path configuration

### Development Issues

**Module not found:**
- Ensure all dependencies installed
- Check import paths in controllers

**Template errors:**
- Verify frontend folder structure
- Check template folder configuration

## 🔒 Security & Privacy

### Data Security
- ✅ **Network Storage**: All data stored on secure network location
- ✅ **Local Interface**: Application runs on localhost only
- ✅ **No Authentication**: Suitable for trusted environments
- ✅ **Thread-Safe**: Prevents data corruption in multi-user scenarios
- ✅ **JSON Format**: Data stored in readable format

### Network Security
- **Access Control**: Network folder permissions control access
- **Data Integrity**: Thread-safe operations prevent corruption
- **Backup Safety**: Automatic backups stored on network
- **Audit Trail**: All changes timestamped and tracked

### Recommendations
- Use on trusted network only
- Regular network backups recommended
- Monitor network folder access
- Keep executables updated

## 📈 Future Enhancements

### Potential Features
- 📊 **Reports**: Export data to Excel/CSV
- 👥 **User Management**: Multiple packer profiles
- 📅 **Date Filtering**: Filter orders by date ranges
- 🔍 **Search Functionality**: Search by order number or packer name
- 📱 **Mobile App**: Native mobile application
- ☁️ **Cloud Sync**: Multi-station synchronization

### Technical Improvements
- 🗄️ **Database**: SQLite/PostgreSQL for larger datasets
- 🔐 **Authentication**: User login system
- 📊 **Analytics**: Usage statistics and reports
- 🎨 **Themes**: Customizable UI themes

## 🤝 Contributing

### Development Workflow
1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

### Code Standards
- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Test all functionality before submitting

## 📄 License

This project is open source and available under the MIT License.

## 📞 Support

### For Users
- Check the DEPLOYMENT.md for user-specific guidance
- Contact your system administrator for technical issues

### For Developers
- Review the code structure in `backend/` and `frontend/`
- Check the build scripts for deployment options
- Use the development setup for testing

## 📋 Version History

### v1.1.0 (current)
- **Search & Filter**: Added search by order number, filter by packer name, and date range filtering
- **Data Validation**: Enhanced validation for packer names (non-empty) and order numbers (exactly 6digits)
- **Auto-Backup**: Automatic backup system that creates backups every 50 orders or 4 hours
- **Version Display**: Added version number display in bottom-right corner of all pages
- **Enhanced UI**: Improved search and filter controls with responsive design
- **Network Ready**: Optimized for network storage deployment

### v1.0.0 **JSON Storage**: Migrated from text format to structured JSON with packer-based organization
- **Thread-Safe Operations**: Atomic file operations prevent data corruption in multi-user scenarios
- **Auto-Migration**: Automatic migration from old text format to new JSON format
- **Enhanced Data Structure**: Each packer appears once with a list of their orders

### v0.5.0- **New Feature**: Changed from search functionality to comprehensive order viewing
- **UI Update**: Replaced search form with tabular display of all orders
- **Enhanced UX**: Users can now see complete order history at a glance
- **Improved Layout**: Wider container and responsive table design
- **Better Navigation**: Updated link text from Search Orders" to View Orders

### v0.1.0
- **Initial Release**: Basic order recording and search functionality
- **Core Features**: Record orders, search by order number, duplicate prevention
- **Modern UI**: Clean, responsive design with gradient styling
- **Standalone Executable**: Easy deployment with PyInstaller

---

**Built with ❤️ for efficient order tracking on network storage**