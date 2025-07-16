#!/usr/bin/env python3
"""
Build script to create a standalone executable for Packer Tracker (with console)
"""

import os
import subprocess
import sys
import shutil

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("✅ PyInstaller is already installed")
    except ImportError:
        print("📦 Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller installed successfully")

def build_executable():
    """Build the executable using PyInstaller (with console)"""
    print("🔨 Building executable (with console)...")
    
    # PyInstaller command with options (no --windowed flag to show console)
    cmd = [
        "pyinstaller",
        "--onefile",                    # Create a single executable file
        "--name=PackerTracker_Console", # Name of the executable
        "--add-data=../frontend;frontend",  # Include frontend folder
        "--add-data=controllers;controllers",  # Include controllers
        "--add-data=models;models",     # Include models
        "--icon=icon.ico",              # Add icon if available
        "--distpath=../dist",           # Output directory (go up one level)
        "startup.py"                    # Main script
    ]
    
    # Remove icon option if icon doesn't exist
    if not os.path.exists("icon.ico"):
        cmd.remove("--icon=icon.ico")
    
    try:
        subprocess.check_call(cmd)
        print("✅ Executable built successfully!")
        print(f"📁 Executable location: {os.path.abspath('../dist/PackerTracker_Console.exe')}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error building executable: {e}")
        return False
    
    return True

def create_launcher_script():
    """Create a simple launcher script for easier access"""
    launcher_content = '''@echo off
title Packer Tracker
color 0A
echo.
echo ========================================
echo           PACKER TRACKER
echo ========================================
echo.
echo Starting application...
echo The browser will open automatically.
echo.
echo Keep this window open while using the app.
echo Close this window to stop the application.
echo.
echo ========================================
echo.
'''
    
    with open("../dist/Launch_PackerTracker_Console.bat", "w") as f:
        f.write(launcher_content)
    
    print("✅ Launcher script created: ../dist/Launch_PackerTracker_Console.bat")

def main():
    print("🚀 Packer Tracker - Build Script (Console Version)")
    print("=" * 50)
    
    # Install PyInstaller
    install_pyinstaller()
    
    # Build executable
    if build_executable():
        # Create launcher script
        create_launcher_script()
        
        print("\n🎉 Build completed successfully!")
        print("\n📋 Next steps:")
        print("1. Go to the 'dist' folder")
        print("2. Copy 'PackerTracker_Console.exe' to your packing stations")
        print("3. Double-click to run (no installation needed)")
        print("4. The app will automatically open in the browser")
        print("5. Users can see the application status in the console window")
        print("\n💡 Tip: You can also use 'Launch_PackerTracker_Console.bat' for easier access")
        print("\n🔍 Console version shows application status - recommended for users!")
    else:
        print("\n❌ Build failed. Please check the error messages above.")

if __name__ == "__main__":
    main() 