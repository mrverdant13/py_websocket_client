@echo off
cls
echo:Setting up...

if not exist .\venv\ (
    cls
    echo:Creating virtual venv...
    py -m virtualenv venv
)

cls
echo:Installing packages (venv scope)...
call .\venv\Scripts\activate.bat
py -m pip install -r windows-requirements.txt

REM if not exist .\app\secrets.py (
REM     cls
REM     echo:Generating 'secrets.py' file...
REM     xcopy .\app\secrets_schema.py .\app\secrets.py
REM )

REM notepad .\app\secrets.py

REM cls
REM echo:All done!
REM py ./app/app.py