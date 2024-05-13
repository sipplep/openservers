import subprocess
from pathlib import Path

ICON_PATH = Path(__file__).parent / "icons"

def setup_openstreamlit():
    # Create app.py file if it doesn't exist
    Path("app.py").touch(exist_ok=True)
    return {
        "command": ["streamlit", "run", "app.py", "--server.port={port}", "--browser.gatherUsageStats=false"], 
        "timeout": 120,
        "launcher_entry": {"icon_path": str((ICON_PATH / "streamlit.svg").absolute())},
    }


def setup_openvscode():
    return {
        "command": ["code-server", "--port={port}","--auth=none", "--disable-telemetry"], 
        "timeout": 120,
        "launcher_entry": {"icon_path": str((ICON_PATH / "vscode.svg").absolute())},
    }

def setup_opendagster():
    subprocess.run(["chmod", "+x", "dagster_init.sh"])
    return {
        "command": ["./dagster_init.sh", "{port}"], 
        "timeout": 120,
        "launcher_entry": {"icon_path": str((ICON_PATH / "dagster.svg").absolute())},
    }
