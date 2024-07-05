@echo off
echo Checking for Python installation...
python --version
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    exit /b 1
)

echo Checking for pip installation...
pip --version
if %errorlevel% neq 0 (
    echo Pip is not installed. Installing pip...
    python -m ensurepip --upgrade
)

echo Installing pygame==2.4.0...
pip install pygame==2.4.0

echo Installing pyarmor...
pip install pyarmor

echo Installation complete.
pause
