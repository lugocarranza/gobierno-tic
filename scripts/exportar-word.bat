@echo off
setlocal

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0exportar-word.ps1" %*

echo.
echo Exportacion finalizada. Presione una tecla para cerrar.
pause > nul
