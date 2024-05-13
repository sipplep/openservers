import subprocess
from pathlib import Path
from os import getenv

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
    # Install dagster-quickstart package if environmental variable for DAGSTER_PACKAGE_NAME is missing
    if getenv("DAGSTER_PACKAGE_NAME") is None:
        subprocess.run(["pip", "install", "-e", "git+https://github.com/dagster-io/dagster-quickstart.git"])
        command = ["dagster", "dev", "-m", "dagster_quickstart", "--port", f"{port}"]
    else:
        command = ["dagster", "dev", "--port", f"{port}"]

    return {
        "command": command, 
        "timeout": 120,
        "launcher_entry": {"icon_path": str((ICON_PATH / "dagster.svg").absolute())},
    }
