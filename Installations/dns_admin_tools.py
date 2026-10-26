import os
import sys
import subprocess
import shutil
from datetime import datetime

admin_tools = ["nmap", "mtr", "rsync", "git"]
updates = ["dnf update","dnf upgrade -y","dnf dist-upgrade -y","dnf clean all","dnf autoremove -y"]

log_path = "/var/log/SysAdmin-Logs"
update_file = "updates.log"
update_path = os.path.join(log_path,update_file)
software_file = "software.log"
software_path = os.path.join(log_path,software_file)
file_paths = [software_path, update_path]

def check_root():
    if os.getuid() != 0:
        print("This script must be run as root", file=sys.stderr)
        sys.exit(1)

def validateLogPath(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except Exception as e:
            print(f"An error has occured in creating log path: {e}")

def validateLogFile(path_lst):
    for i in path_lst:
        if not os.path.isfile(i):
            try:
                with open(i, "w") as f:
                    pass
            except Exception as e:
                print(f"An error has occurred in creating log file: {e}")

def update(lst):
    for i in lst:
        command = ["bash", "-c", i]
        try:
            subprocess.run(command, check=True)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(update_path, "a") as f:
                f.write(f"{timestamp} - Success: {i}\n")
            print(f"Success: {i}")
        except subprocess.CalledProcessError:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(update_path, "a") as f:
                f.write(f"{timestamp} - Failed: {i}\n")
            print(f"Failed: {i}")

def install_admin_tools(lst):
    for i in lst:
        command = ["dnf", "install", "-y", i]
        if shutil.which(i) is not None:
            print(f"{i} is already installed.")
        try:
            subprocess.run(command, check=True)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(software_path, "a") as f:
                f.write(f"{timestamp} - Success: dnf install -y {i}\n")
            print(f"Success: {i} installed")
        except subprocess.CalledProcessError:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(software_path, "a") as f:
                f.write(f"{timestamp} - Failed: dnf install -y {i}\n")
            print(f"Failed: {i} installation")

check_root()
validateLogPath(log_path)
validateLogFile(file_paths)
update(updates)
install_admin_tools(admin_tools)

