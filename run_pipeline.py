from pathlib import Path 
from datetime import datetime
import subprocess
import sys 
import logging

logging.basicConfig(
    filename=Path(__file__).resolve().parent / "pipeline.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
) 

project_folder = Path(__file__).resolve().parent

for script in ["main.py", "inspect_data.py", "query_data.py"]:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] Running {script}...", flush=True) 
    logging.info("Starting %s", script)
    try:
        subprocess.run(
        [sys.executable, script],
        cwd=project_folder,
        check=True,
    )
    except subprocess.CalledProcessError:
        logging.exception("Failed %s", script)
        raise 

    logging.info("Completed %s", script) 
print("Pipeline completed!")
