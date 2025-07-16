# 📦 Packer Tracker

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
- 🔍 **Search Orders**: Find who packed a specific order
- 💾 **Simple Storage**: Data saved to `packer_data.txt` (delimited format)
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
- 📊 **Data Persistence**: Automatic data saving to text file
- 🛠️ **Easy Maintenance**: Simple text-based data storage

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

Data is stored in `packer_data.txt`:
```
packer_name|order_number|timestamp
```

**Example:**
```
John Smith|ORD-12345|2024-01-15 14:30:25
Jane Doe|ORD-12346|2024-01-15 14:35:10
```

## 🔧 Configuration

### Environment Variables
- `FLASK_SECRET_KEY`: Secret key for sessions (default: auto-generated)
- `DATA_FILE`: Path to data file (default: `packer_data.txt`)

### Port Configuration
- Default port: 5000
- Change in `backend/startup.py` if needed

## 🚨 Troubleshooting

### Common Issues

**Executable won't start:**
- Check if port 5000 is available
- Ensure antivirus isn't blocking the file
- Try running as administrator

**Browser doesn't open:**
- Check default browser settings
- Manually navigate to `http://localhost:5000`

**Data not saving:**
- Check folder write permissions
- Ensure antivirus isn't blocking file creation

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
- ✅ **Local Storage**: All data stored locally
- ✅ **No Network**: Application runs on localhost only
- ✅ **No Authentication**: Suitable for trusted environments
- ⚠️ **Plain Text**: Data stored in readable text format

### Recommendations
- Use on trusted computers only
- Regular data backups recommended
- Consider encryption for sensitive data

## 📈 Future Enhancements

### Potential Features
- 📊 **Reports**: Export data to Excel/CSV
- 👥 **User Management**: Multiple packer profiles
- 📅 **Date Filtering**: Search by date ranges
- 🔍 **Advanced Search**: Search by packer name
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

---

**Built with ❤️ for efficient order tracking** 
