# 📦 Packer Tracker - Deployment Guide

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
1. **Enter your name** in the "Packer Name" field
2. **Enter the order number** in the "Order Number" field
3. **Click "Record Order"**
4. **See the green success message** - you're done!

#### 🔍 Finding an Order
1. **Click "Search Orders"** at the bottom
2. **Enter the order number** you're looking for
3. **Click "Search Order"**
4. **See who packed it and when**

### Tips for Packers
- ✅ **Use your real name** - this helps track your work
- ✅ **Double-check order numbers** - typos can cause issues
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
Data is stored in `packer_data.txt` in the same folder as the executable:
```
packer_name|order_number|timestamp
```

**Example data:**
```
John Smith|ORD-12345|2024-01-15 14:30:25
Jane Doe|ORD-12346|2024-01-15 14:35:10
Mike Johnson|ORD-12347|2024-01-15 14:40:15
```

#### 📁 File Locations
- **Executable**: `PackerTracker_Console.exe`
- **Data file**: `packer_data.txt` (created automatically)
- **Both files** are in the same folder

#### 🔄 Data Operations

**Backup Data:**
```bash
# Copy the data file to backup location
copy packer_data.txt backup_packer_data_2024-01-15.txt
```

**Move to New Location:**
```bash
# Copy both files together
copy PackerTracker_Console.exe new_location\
copy packer_data.txt new_location\
```

**Merge Data from Multiple Stations:**
```bash
# Combine data files (use text editor)
# Copy all lines from station2_data.txt to main_data.txt
```

**View Data in Excel:**
1. Open `packer_data.txt` in Notepad
2. Copy all content
3. Paste into Excel
4. Use "Text to Columns" with "|" as delimiter

### Monitoring & Maintenance

#### 📈 Daily Checks
- **Verify app is running** on all stations
- **Check data file size** (should grow daily)
- **Backup data** at end of shift

#### 📊 Weekly Tasks
- **Review data** for accuracy
- **Backup all data files**
- **Check for duplicate entries**
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
1. Open `packer_data.txt` in Excel
2. Split columns by "|" delimiter
3. Create pivot tables for:
   - Orders per packer
   - Orders per day
   - Packing speed analysis

**Command Line Analysis:**
```bash
# Count total orders
find /c "|" packer_data.txt

# Find orders by specific packer
findstr "John Smith" packer_data.txt

# Find orders from today
findstr "2024-01-15" packer_data.txt
```

### Security Considerations

#### 🔒 Data Protection
- **Local storage only** - no network access
- **Plain text format** - easily readable
- **No encryption** - suitable for trusted environments
- **Regular backups** recommended

#### 🛡️ Best Practices
- **Use on trusted computers only**
- **Regular data backups**
- **Monitor for unusual activity**
- **Keep executables updated**

### Support & Training

#### 📚 Training Packers
1. **Show them the app** - 5 minute demo
2. **Explain the process** - record then search
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
- **Record**: Name + Order Number → "Record Order"
- **Search**: Click "Search Orders" → Enter Order Number
- **Stop**: Close the console window

### For Administrators
- **Install**: Copy executable to station
- **Monitor**: Check `packer_data.txt` file
- **Backup**: Copy data file regularly
- **Update**: Replace executable when needed

### File Locations
- **App**: `PackerTracker_Console.exe`
- **Data**: `packer_data.txt` (same folder)
- **Backup**: Create copies with date in filename

---

**Need help? Check the troubleshooting section or contact your IT support.** 