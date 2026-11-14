import os
import sys
import subprocess
from datetime import datetime

updates = ["dnf update","dnf upgrade -y","dnf dist-upgrade -y","dnf clean all","dnf autoremove -y"]

log_path = "/var/log/SysAdmin-Logs"
log_file = "updates.log"
file_path = os.path.join(log_path,log_file)

def check_root():
    if os.getuid() != 0:
        print("This script must be run as root", file=sys.stderr)
        sys.exit(1)

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validateLogPath(path):        
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except Exception as e:
            print(f"An error has occured in creating log path: {e}")

def validateLogFile(path):
    if not os.path.isfile(path):
        try:
            with open(path, "w") as f:
                pass
        except Exception as e:
            print(f"An error has occured in creating log file: {e}")

def main():

    check_root()
    validateLogPath(log_path)
    validateLogFile(file_path)
    
    for i in updates:
        command = ["bash", "-c", i]
        try:
            subprocess.run(command, check=True)
            current_time = timestamp()
            with open(file_path, "a") as f:
                f.write(f"{current_time} - Success: {i}\n")
            print(f"Success: {i}")
        except subprocess.CalledProcessError:
            current_time = timestamp()
            with open(file_path, "a") as f:
                f.write(f"{current_time} - Failed: {i}\n")
            print(f"Failed: {i}")

if __name__ == "__main__":
    main()



