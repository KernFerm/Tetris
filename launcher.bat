@echo off
REM Save the current directory
pushd %~dp0

REM Check if tetris.py exists
if not exist tetris.py (
    echo Error: tetris.py not found in the current directory.
    popd
    pause
    exit /b 1
)

REM Run the Python script and check for errors
echo Running tetris.py...
python tetris.py
if %errorlevel% neq 0 (
    echo Error: tetris.py did not run successfully. Error level: %errorlevel%
    popd
    pause
    exit /b %errorlevel%
)

REM Provide success feedback
echo tetris.py ran successfully.

REM Return to the original directory
popd
pause
