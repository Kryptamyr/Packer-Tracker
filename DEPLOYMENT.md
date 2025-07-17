# 📦 Packer Tracker v1.1.0 - Deployment Guide

## 🎯 For Packing Station Workers

### Quick Start (5 minutes)
1. **Access the app**: Use the desktop/taskbar shortcut provided by your supervisor
2. **Run it**: Click the shortcut - browser opens automatically
3. **Start working**: Begin tracking orders - data saves to network storage

### How to Use the App

#### 📝 Recording an Order
1. **Enter your name** in the "Packer Name field (cannot be empty)
2. **Enter the order number** in the "Order Number" field (must be exactly 6 digits)
3. **Click "Record Order"**after filling out fields
4. **Wait for the green success message** - you're done!

#### 📋 Viewing & Searching Orders
1. **Click View Orders** at the bottom
2. **Use the search box** to find an order by number
3. **Filter by packer name** using the dropdown
4. **Filter by date range** using the start/end date pickers
5. **See all recorded orders** in a table format

### Tips for Packers
- ✅ **Use your real name** - this helps track your work
- ✅ **Double-check order numbers** - typos can cause issues
- ✅ **Order number must be 6 digits** - prevents tracking problems
- ✅ **Keep the app running** - don't close the console window
- ✅ **Data saves to network** - accessible from any computer
- ✅ **Ask for help** if something doesn't work

### Common Issues & Solutions

**❌ "Port already in use"**
- Close other applications
- Restart your computer if needed

**❌ Browser doesn't open**
- Wait a few seconds
- Or manually go to: `http://localhost:5000 

**❌ Cant save orders**
- Check network connection to Compliance storage
- Contact Supervisor if network access is down
- Try putting the app on your Desktop temporarily

---

## 👨‍💼 For Administrators & Supervisors

### Installing on Packing Stations

#### Single Station Setup
1. **Create shortcut** on desktop pointing to `\\Compliance\PackerTracker\PackerTracker_Console.exe`
2. **Test it** by clicking the shortcut
3. **Verify** data saves to network location

#### Multiple Station Setup
1. **Create shortcuts** on each station pointing to the network executable
2. **All stations** share the same data file on network storage
3. **Real-time access** - changes visible immediately across all stations
4. **Centralized management** - single location for updates and maintenance

#### 📁 File Locations
- **Network Path**: `\\Compliance\PackerTracker\`
- **Executable**: `PackerTracker_Console.exe`
- **Data file**: `packer_data.json` (created automatically)
- **Backups**: `backups/` folder (auto-created, contains periodic backups)

#### 🔄 Data Operations

**Backup Data:**
- Backups are created automatically every 50 orders or every4ours
- Backups are stored in the `backups/` folder as `packer_data_backup_YYYYMMDD_HHMMSS.json`
- Only the last 10 backups are kept
- You can manually copy a backup file for extra safety

**View Data in Excel:**
1. Open `\\Compliance\PackerTracker\packer_data.json` in Notepad
2. Copy all content
3. Paste into Excel (or use a JSON-to-CSV converter)
4. Use Excel's features to analyze data

### Monitoring & Maintenance

#### 📈 Daily Checks
- **Verify app is running** on all stations
- **Check network connectivity** to Compliance storage
- **Monitor data file size** (should grow daily)
- **Check backup folder** for recent backups

#### 📊 Weekly Tasks
- **Review data** for accuracy
- **Check network folder permissions**
- **Monitor packer performance**
- **Verify all stations can access data**

#### 🛠️ Monthly Maintenance
- **Update executable** if new version available
- **Review packer statistics**
- **Clean up old backups** (if needed)
- **Test network connectivity** from all stations

### Troubleshooting for Administrators

#### ❌ Network Access Issues
**Check:**
- Network connectivity to `\\Compliance\`
- User permissions on PackerTracker folder
- Network drive mapping
- Firewall settings

**Solutions:**
- Verify network path is accessible
- Check folder permissions (read/write for all users)
- Map network drive if needed
- Contact network administrator

#### ❌ App Won't Start
**Check:**
- Port 5000 available
- Antivirus blocking
- File permissions
- Network access

**Solutions:**
- Close other applications using port 5000
- Add to antivirus exclusions
- Run as administrator
- Check network connectivity

#### ❌ Data Not Saving
**Check:**
- Network folder write permissions
- Network connection stability
- Disk space on network storage
- Antivirus blocking file creation

**Solutions:**
- Verify network folder permissions
- Check network connection
- Free up disk space on network storage
- Add folder to antivirus exclusions

#### ❌ Multiple Users Can't Access Simultaneously
**Solution:**
- This is normal and expected
- Thread-safe operations prevent data corruption
- Each user gets their own browser session
- All changes are immediately visible to other users
