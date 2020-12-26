@echo off
title AutoBuild
@rem echo -----------------------------------------------------------------
@rem echo This is auto-build programm for convert MineAutoServer.py to .exe
@rem echo -----------------------------------------------------------------
rmdir /s /q %CD%\__pycache__
rmdir /s /q %CD%\build
rmdir /s /q %CD%\dist
@rem del /p %CD%\MineAutoServer.spec
pyinstaller MineAutoServer.py -F --console