@echo off
setlocal

REM Function to check and handle errors
:check_error
if %errorlevel% neq 0 (
    echo Error occurred: %1
    call :cleanup
    exit /b %errorlevel%
)

REM Function to clean up in case of failure
:cleanup
if exist venv (
    echo Cleaning up...
    rmdir /s /q venv
)
goto :EOF

REM Check if Python is installed
echo Checking for Python installation...
python --version >nul 2>&1
call :check_error "Python is not installed. Please install Python before running this script."

REM Check for pip installation
echo Checking for pip installation...
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Pip is not installed. Installing pip...
    python -m ensurepip --upgrade
    call :check_error "Failed to install pip."
)

REM Create a virtual environment
echo Creating virtual environment...
python -m venv venv
call :check_error "Failed to create virtual environment."

REM Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
call :check_error "Failed to activate virtual environment."

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip
call :check_error "Failed to upgrade pip."

REM Install pygame and pyarmor
echo Installing pygame==2.4.0 and pyarmor...
pip install pygame==2.4.0 pyarmor
call :check_error "Failed to install one or more packages."

REM Deactivate the virtual environment
echo Deactivating virtual environment...
deactivate
call :check_error "Failed to deactivate virtual environment."

echo Installation complete.
pause

endlocal
exit /b 0
