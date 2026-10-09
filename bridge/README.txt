Musa_ICM_Bridge  -  Claude <-> InfoWorks ICM (MCP)
===================================================

REQUIREMENTS
  - Windows, InfoWorks ICM (with Ruby scripting)
  - Python 3.10+ on PATH (python.org installer, tick "Add to PATH")
  - Claude Desktop app

INSTALL
  1. Unzip this folder somewhere permanent, e.g. C:\Musa_ICM_Bridge
     (don't run it from inside the zip or Downloads you'll clean later).
  2. Double-click install.bat
       - installs mcp + pywinauto
       - adds "Musa_ICM_Bridge" to %APPDATA%\Claude\claude_desktop_config.json
         (existing servers are kept; a .bak backup is made)
  3. Fully quit Claude Desktop (system tray > Quit) and reopen it.
  4. Settings > Developer should show Musa_ICM_Bridge as "running".

USING IT
  1. Open InfoWorks ICM and open a network.
  2. Open the Ruby Script window (Network > Run Ruby Script...) and leave it
     visible - the bridge types code into it and presses Run.
  3. Ask Claude e.g. "give me the ICM network summary".

TOOLS
  icm_run_ruby(ruby_code)   run any Ruby inside ICM, returns printed output
  icm_network_summary()     counts of nodes / links / conduits / etc.

NOTES
  - Results are passed back via C:\icm_mcp_poc\result.txt (auto-created).
  - Default timeout is 30 s per script (run_timeout in icm_controller_final2.py).
  - Error messages are in Arabic: "can't find ICM window" = ICM not open;
    "can't find Run button" = Ruby Script window not open.
  - Don't touch mouse/keyboard on the ICM window while a script is typing.

MANUAL CONFIG (if install.bat isn't used) - add under "mcpServers":
  "Musa_ICM_Bridge": {
    "command": "python",
    "args": ["C:\\Musa_ICM_Bridge\\icm_mcp_server.py"]
  }
