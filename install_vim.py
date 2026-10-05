import os
import sys
import shutil
import subprocess
from datetime import datetime

log_path = "/var/log/SysAdmin-Logs"
software_log_file = "software.log"
update_log_file = "update.log"
software_path = os.path.join(log_path,software_log_file)
update_path = os.path.join(log_path,update_log_file)
updates = ["dnf update","dnf upgrade -y","dnf dist-upgrade -y","dnf clean all","dnf autoremove -y"]

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

def validateLogFile(path):
    if not os.path.isfile(path):
        try:
            with open(path, "w") as f:
                pass
        except Exception as e:
            print(f"An error has occured in creating log file: {e}")

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


def intall_vim():
        install_vim = ["dnf", "install", "-y", "vim"]
        if shutil.which("vim") is not None:
                print("Vim is already installed.")
        try:
                subprocess.run(install_vim, check=True)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(software_path, "a") as f:
                        f.write(f"{timestamp} - Success: dnf install -y vim\n")
                print(f"Success: Vim installed")
        except subprocess.CalledProcessError:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(software_path, "a") as f:
                        f.write(f"{timestamp} - Failed: dnf install -y vim\n")
                print(f"Failed: Vim installation")


check_root()
validateLogPath(log_path)
validateLogFile(file_path)
update(updates)
install_vim()
