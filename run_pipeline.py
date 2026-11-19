from pathlib import Path 
from datetime import datetime
import subprocess
import sys

project_folder = Path(__file__).resolve().parent

for script in ["main.py", "inspect_data.py", "query_data.py"]:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] Running {script}...", flush=True) 
    subprocess.run(
        [sys.executable, script],
        cwd=project_folder,
        check=True,
    )

print("Pipeline completed!")
