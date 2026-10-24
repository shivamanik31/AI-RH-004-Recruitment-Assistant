
"""AI Recruitment Assistant - Main Entry Point."""

import subprocess
import sys

def main():
    print("=" * 45)
    print("       AI RECRUITMENT ASSISTANT")
    print("       Project: AI-RH-004")
    print("       Student Code: DAS011046")
    print("=" * 45)
    print("\nStarting the Streamlit application...\n")

    subprocess.run([
        sys.executable,
        "-m",
        "streamlit",
        "run",
        "app.py"
    ], check=False)

if __name__ == "__main__":
    main()
