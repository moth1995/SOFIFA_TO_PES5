@echo on
pyinstaller "main.py" --name "SoFIFA to PES5_WE9_LE" --noconsole
xcopy "src\" "dist\SoFIFA to PES5_WE9_LE\src\"
pause