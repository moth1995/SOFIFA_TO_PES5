@echo on
pyinstaller "main.py" --name "SoFIFA to PES5_WE9_LE" --noconsole
xcopy "mdb_template\" "dist\SoFIFA to PES5_WE9_LE\mdb_template\"
pause