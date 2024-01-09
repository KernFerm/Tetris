@echo off

REM Install dependencies
py -m pip install --upgrade pip
py -m pip install --upgrade wheel
py -m pip install --upgrade setuptools
set DISTUTILS_USE_SDK=1
set MSSdk=1
git clone https://github.com/pygame/pygame.git
cd pygame
py -m pip install --upgrade pip
py -m pip install --requirement requirements.txt
py -m buildconfig --download
py -m pip install .

REM Run example
py -m pygame.examples.aliens