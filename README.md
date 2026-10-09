# Musa_ICM_Bridge

Connect **Claude Desktop** to **Autodesk InfoWorks ICM** through an MCP server, so Claude can run Ruby scripts in your open network and read the results back.

### 👉 [Download and setup guide](https://musaibrahim5411-lang.github.io/Musa_ICM_Bridge/)

---

## How it works

```
Claude Desktop ──stdio──▶ Musa_ICM_Bridge (Python) ──paste + Run──▶ ICM Ruby Script window
       ▲                                                                  │
       └──────────────── C:\icm_mcp_poc\result.txt ◀──────────────────────┘
```

## Tools

| Tool | What it does |
|---|---|
| `icm_run_ruby(ruby_code)` | Runs any Ruby in the open ICM session and returns the printed output |
| `icm_network_summary()` | Network name and counts of nodes, links, conduits, culverts, pumps, weirs, orifices |

## Quick install

1. Install **Python 3.10+** (tick *Add to PATH*).
2. Download `Musa_ICM_Bridge.zip` from the [setup page](https://musaibrahim5411-lang.github.io/Musa_ICM_Bridge/) and unzip to `C:\Musa_ICM_Bridge`.
3. Double-click `install.bat`.
4. Quit Claude Desktop from the system tray and reopen it.
5. Open ICM, open a network, and keep the **Ruby Script** window visible.
6. Ask Claude: *"Use Musa_ICM_Bridge to give me a summary of the open ICM network."*

## Requirements

- Windows · InfoWorks ICM (tested on Ultimate 2027) · Python 3.10+ · Claude Desktop
- Python packages: `mcp`, `pywinauto`

## Author

**Musa Ibrahim** · Hydrology Engineer · [LinkedIn](https://www.linkedin.com/in/musa-ibrahim-0128421b6/)

Community project, not affiliated with or endorsed by Autodesk. InfoWorks ICM is a trademark of its owner.
