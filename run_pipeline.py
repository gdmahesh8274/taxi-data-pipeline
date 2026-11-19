from pathlib import Path
import subprocess
import sys

project_folder = Path(__file__).resolve().parent

for script in ["main.py", "inspect_data.py", "query_data.py"]:
    print(f"Running {script}...", flush=True)
    subprocess.run(
        [sys.executable, script],
        cwd=project_folder,
        check=True,
    )

print("Pipeline completed!")

