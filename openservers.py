from pathlib import Path


def setup_openstreamlit():
    # Create app.py file if it doesn't exist
    Path("app.py").touch(exist_ok=True)
    return {
        "command": ["streamlit", "run", "app.py", "--server.port={port}", "--browser.gatherUsageStats=false"], 
        "timeout": 120,
    }


def setup_openvscode():
    return {
        "command": ["code-server", "--port={port}","--auth=none", "--disable-telemetry"], 
        "timeout": 120,
    }
    
