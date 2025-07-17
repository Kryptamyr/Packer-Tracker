# 📦 Packer Tracker v1.1.0 - Deployment Guide

## 🎯 For Packing Station Workers

### Quick Start (5 minutes)
1. **Get the app**: Ask your supervisor for `PackerTracker_Console.exe`
2. **Save it**: Put it anywhere on your computer (Desktop is fine)
3. **Run it**: Double-click the file
4. **Start working**: Browser opens automatically - you're ready!

### What You'll See
When you double-click the app:
```
🚀 Starting Packer Tracker...
📦 Application will open in your browser automatically
🔄 Keep this window open while using the application
❌ Close this window to stop the application
--------------------------------------------------
 * Running on http://localhost:5000
```

**Keep this window open while working!** Close it when you're done.

### How to Use the App

#### 📝 Recording an Order
1. **Enter your name** in the "Packer Name" field (cannot be empty)
2. **Enter the order number** in the "Order Number" field (must be exactly 6 digits)
3. **Click "Record Order"**
4. **See the green success message** - you're done!

#### 📋 Viewing & Searching Orders
1. **Click "View Orders"** at the bottom
2. **Use the search box** to find an order by number
3. **Filter by packer name** using the dropdown
4. **Filter by date range** using the start/end date pickers
5. **See all recorded orders** in a table format
6. **View packer names, order numbers, and timestamps** for all entries

### Tips for Packers
- ✅ **Use your real name** - this helps track your work
- ✅ **Double-check order numbers** - typos can cause issues
- ✅ **Order number must be 6 digits**
- ✅ **Keep the app running** - don't close the console window
- ✅ **Ask for help** if something doesn't work

### Common Issues & Solutions

**❌ "Port already in use"**
- Close other applications
- Restart your computer if needed

**❌ Browser doesn't open**
- Wait a few seconds
- Or manually go to: `http://localhost:5000`

**❌ Can't save orders**
- Make sure you're not in a restricted folder
- Try putting the app on your Desktop

---

## 👨‍💼 For Administrators & Supervisors

### Installing on Packing Stations

#### Single Station Setup
1. **Copy** `PackerTracker_Console.exe` to the packing station
2. **Place it** in a folder (e.g., `C:\PackerTracker\`)
3. **Test it** by double-clicking
4. **Create shortcut** on Desktop for easy access

#### Multiple Station Setup
1. **Copy executable** to each station
2. **Each station** will have its own data file
3. **No network setup** required
4. **Independent operation** per station

### Data Management

#### 📊 Understanding the Data File
Data is stored in `packer_data.json` in the same folder as the executable:
```json
{
  "John Smith": [
    {"order": "123456", "timestamp": "2025-07-17T08:15:23"},
    {"order": "654321", "timestamp": "2025-07-17T09:02:11"}
  ],
  "Jane Doe": [
    {"order": "777777", "timestamp": "2025-07-17T08:17:45"}
  ]
}
```
- **Each packer appears only once, with a list of their orders and timestamps.**
- **Duplicate order numbers are not allowed.**

#### 📁 File Locations
- **Executable**: `PackerTracker_Console.exe`
- **Data file**: `packer_data.json` (created automatically)
- **Backups**: `backups/` folder (auto-created, contains periodic backups)
- **Both files** are in the same folder

#### 🔄 Data Operations

**Backup Data:**
- Backups are created automatically every 50 orders or every 4 hours.
- Backups are stored in the `backups/` folder as `packer_data_backup_YYYYMMDD_HHMMSS.json`.
- Only the last 10 backups are kept.
- You can manually copy a backup file for extra safety.

**Move to New Location:**
```bash
# Copy both files together
copy PackerTracker_Console.exe new_location\
copy packer_data.json new_location\
copy /Y backups\* new_location\backups\
```

**Merge Data from Multiple Stations:**
- Open both `packer_data.json` files in a text editor or use a script to merge by packer name and order.
- Ensure no duplicate order numbers.

**View Data in Excel:**
1. Open `packer_data.json` in Notepad
2. Copy all content
3. Paste into Excel (or use a JSON-to-CSV converter)
4. Use Excel's features to analyze data

### Monitoring & Maintenance

#### 📈 Daily Checks
- **Verify app is running** on all stations
- **Check data file size** (should grow daily)
- **Backup data** at end of shift (optional, auto-backup is enabled)

#### 📊 Weekly Tasks
- **Review data** for accuracy
- **Backup all data files**
- **Check for duplicate entries** (should not occur)
- **Monitor packer performance**

#### 🛠️ Monthly Maintenance
- **Update executable** if new version available
- **Archive old data** if needed
- **Review packer statistics**
- **Clean up old backups**

### Troubleshooting for Administrators

#### ❌ App Won't Start
**Check:**
- Port 5000 available
- Antivirus blocking
- File permissions
- Windows firewall

**Solutions:**
- Close other applications using port 5000
- Add to antivirus exclusions
- Run as administrator
- Check Windows firewall settings

#### ❌ Data Not Saving
**Check:**
- Folder write permissions
- Disk space available
- Antivirus blocking file creation

**Solutions:**
- Move to folder with write permissions
- Free up disk space
- Add folder to antivirus exclusions

#### ❌ Multiple Users Can't Use Same Station
**Solution:**
- Each station should have its own executable
- Data files are independent per station
- No sharing needed for basic operation

### Advanced Configuration

#### 🔧 Custom Data Location
To store data in a different location:
1. **Create folder** (e.g., `C:\PackerData\`)
2. **Copy executable** there
3. **Data file** will be created in that folder

#### 📊 Data Analysis
**Simple Analysis with Excel:**
1. Open `packer_data.json` in Excel (or convert to CSV)
2. Analyze by packer, order, or date
3. Create pivot tables for:
   - Orders per packer
   - Orders per day
   - Packing speed analysis

**Command Line Analysis:**
- Use a JSON tool or script to analyze `packer_data.json`

### Security Considerations

#### 🔒 Data Protection
- **Local storage only** - no network access
- **JSON format** - easily readable
- **No encryption** - suitable for trusted environments
- **Regular backups** recommended (auto-backup enabled)

#### 🛡️ Best Practices
- **Use on trusted computers only**
- **Regular data backups**
- **Monitor for unusual activity**
- **Keep executables updated**

### Support & Training

#### 📚 Training Packers
1. **Show them the app** - 5 minute demo
2. **Explain the process** - record, search, filter
3. **Practice with test data**
4. **Provide written instructions**

#### 🆘 Getting Help
- **Check this guide first**
- **Review common issues above**
- **Contact IT support** for technical problems
- **Keep backup of data** before making changes

---

## 📞 Quick Reference

### For Packers
- **Start**: Double-click `PackerTracker_Console.exe`
- **Record**: Name + 6-digit Order Number → "Record Order"
- **View/Filter/Search**: Click "View Orders" → Use search/filter controls
- **Stop**: Close the console window

### For Administrators
- **Install**: Copy executable to station
- **Monitor**: Check `packer_data.json` file
- **Backup**: Use auto-backup or copy backup files from `backups/`
- **Update**: Replace executable when needed

### File Locations
- **App**: `PackerTracker_Console.exe`
- **Data**: `packer_data.json` (same folder)
- **Backups**: `backups/` folder (auto-created) 