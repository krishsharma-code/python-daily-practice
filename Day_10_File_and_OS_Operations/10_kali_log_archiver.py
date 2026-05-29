"""
Day 10: Kali Log Archiver
Concept: System utility to find .log files and zip them for backup.
"""

import os
import shutil
import zipfile
from datetime import datetime

# Setup a mock log environment
log_dir = "logs"
if not os.path.exists(log_dir):
    os.mkdir(log_dir)
    # Create some dummy log files
    for i in range(3):
        with open(f"{log_dir}/system_{i}.log", "w") as f:
            f.write(f"Log entry {i} - {datetime.now()}")

def archive_logs(directory):
    log_files = [f for f in os.listdir(directory) if f.endswith('.log')]
    
    if not log_files:
        print("No log files found to archive.")
        return

    archive_name = f"log_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    
    with zipfile.ZipFile(archive_name, 'w') as zipf:
        for file in log_files:
            file_path = os.path.join(directory, file)
            zipf.write(file_path, file)
            print(f"Added {file} to archive.")

    print(f"\nSuccessfully archived logs into {archive_name}")

if __name__ == "__main__":
    archive_logs(log_dir)
