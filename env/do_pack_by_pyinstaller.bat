pyinstaller.exe pyinstaller_pack_fw.spec
copy .\dist\pzh-knockout.exe ..\bin
rd /q /s .\build
rd /q /s .\dist