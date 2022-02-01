@echo on
pyinstaller "main.py" --name "SoFIFA to PES5_WE9_LE" --noconsole  --version-file file_version_info.txt
xcopy "mdb_template\" "dist\SoFIFA to PES5_WE9_LE\mdb_template\"
pause