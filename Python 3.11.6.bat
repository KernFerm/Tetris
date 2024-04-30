@echo off

echo This script will install Python 3.11.6 on your system.
echo Do you want to continue with the installation? (Y/N)

set /p choice=
if /i "%choice%"=="Y" (
    echo Installing Python 3.11.6...
    python-3.11.6.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    echo Python 3.11.6 has been installed.
) else (
    echo Installation cancelled.
)

pause
