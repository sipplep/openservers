from pathlib import Path
from os import getenv

DIR = Path(getenv('CONDA_DIR')) / "icons"


def setup_openstreamlit():
    # Create app.py file if it doesn't exist
    Path("app.py").touch(exist_ok=True)
    return {
        "command": ["streamlit", "run", "app.py", "--server.port={port}", "--browser.gatherUsageStats=false"], 
        "timeout": 120,
        "launcher_entry": {"icon_path": str(DIR / "streamlit.svg")},
    }

    
def setup_openvscode():
    return {
        "command": ["code-server", "--port={port}","--auth=none", "--disable-telemetry"], 
        "timeout": 120,
        "launcher_entry": {"icon_path": str(DIR / "vscode.svg")},
    }
