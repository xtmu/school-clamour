@echo off 
if "%1"=="h" goto begin 
start mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit 
:begin 
::
start /b cmd /k "C:\Users\init\Documents\GitHub\school-clamour\Scripts\pythonw.exe C:\Users\init\Documents\GitHub\school-clamour\clamour.py"