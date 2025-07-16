@echo off
echo Building Packer Tracker Executable...
echo.
cd backend
python build_exe_console.py
cd ..
echo.
pause 