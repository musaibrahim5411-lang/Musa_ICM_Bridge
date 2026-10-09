"""Adds Musa_ICM_Bridge to Claude Desktop's config (keeps any existing servers)."""
import json, os, sys, shutil

here = os.path.dirname(os.path.abspath(__file__))
server = os.path.join(here, "icm_mcp_server.py")
cfg_dir = os.path.join(os.environ["APPDATA"], "Claude")
cfg = os.path.join(cfg_dir, "claude_desktop_config.json")
os.makedirs(cfg_dir, exist_ok=True)

data = {}
if os.path.exists(cfg):
    shutil.copy2(cfg, cfg + ".bak")
    with open(cfg, "r", encoding="utf-8") as f:
        txt = f.read().strip()
        data = json.loads(txt) if txt else {}

data.setdefault("mcpServers", {})["Musa_ICM_Bridge"] = {
    "command": sys.executable,
    "args": [server],
}
with open(cfg, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Musa_ICM_Bridge registered in:", cfg)
print("python :", sys.executable)
print("server :", server)
