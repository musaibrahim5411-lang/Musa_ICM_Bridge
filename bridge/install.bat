@echo off
cd /d "%~dp0"
echo === Installing Python packages (mcp, pywinauto) ===
python -m pip install -r requirements.txt || goto :err
echo.
echo === Registering Musa_ICM_Bridge with Claude Desktop ===
python register_claude.py || goto :err
if not exist C:\icm_mcp_poc mkdir C:\icm_mcp_poc
echo.
echo Done. Fully quit Claude Desktop (system tray ^> Quit) and open it again.
pause
exit /b 0
:err
echo.
echo FAILED - make sure Python 3.10+ is installed and on PATH.
pause
exit /b 1
