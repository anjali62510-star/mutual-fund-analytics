"""
Bluestock Mutual Fund Analytics
Master Pipeline Execution Script

Runs:
1. ETL Pipeline
2. Performance Analytics
3. Advanced Analytics

Author: Anjali
"""

import os
import subprocess
import sys


def run_script(script_path):
    """
    Execute a Python script and display status.
    """

    print(f"\n{'='*50}")
    print(f"Running: {script_path}")
    print(f"{'='*50}")

    try:
        subprocess.run(
            [sys.executable, script_path],
            check=True
        )

        print(f"SUCCESS: {script_path}")

    except subprocess.CalledProcessError as e:
        print(f"FAILED: {script_path}")
        print(e)


def main():

    print("\nBluestock Mutual Fund Analytics Pipeline")
    print("Starting execution...\n")

    scripts = [

        "scripts/etl_pipeline.py",

        "scripts/compute_metrics.py",

        "scripts/recommender.py"

    ]

    for script in scripts:

        if os.path.exists(script):

            run_script(script)

        else:

            print(f"WARNING: {script} not found")

    print("\nPipeline execution completed.")
    print("All available modules processed successfully.")


if __name__ == "__main__":
    main()