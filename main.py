import sys
import os
import subprocess

if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.abspath(__file__))
    subprocess.run(
        [sys.executable, "-m", "streamlit", "run", "app.py"],
        cwd=root_dir
    )
