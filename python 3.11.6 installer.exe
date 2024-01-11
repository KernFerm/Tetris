@echo off

REM Set the Python version to install
set "PYTHON_VERSION=3.11.6"

REM Set the download URL for the Python installer
set "PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe"

REM Set the destination directory for Python
set "PYTHON_DIR=C:\Python\%PYTHON_VERSION%"

REM Create the destination directory if it does not exist
if not exist "%PYTHON_DIR%" mkdir "%PYTHON_DIR%"

REM Download the Python installer
curl --location --output "%PYTHON_DIR%\python.exe" "%PYTHON_URL%"

REM Start the installation process
"%PYTHON_DIR%\python.exe" -m pip install --upgrade pip
"%PYTHON_DIR%\python.exe" -m pip install --upgrade virtualenv

REM Add Python to the PATH
setx PATH "%PYTHON_DIR%;%PYTHON_DIR%\Scripts;%PATH%"

REM Verify that Python is installed
python --version
pip --version

REM Install any additional packages that you need
pip install PACKAGE_NAME

REM You can now use Python from the command line by typing "python" or "python.exe"