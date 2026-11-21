import os
import sys
import subprocess
from datetime import datetime

hostname_file = "/etc/hostname"
log_path = "/var/log/SysAdmin-Logs"
log_file = "system.log"
log_file_path = os.path.join(log_path,log_file)

def check_root():
    if os.getuid() != 0:
        print("This script must be run as root", file=sys.stderr)
        sys.exit(1)

def validate_hostname_path(path):
    if not os.path.exists(path):
        print("/etc/hostname does not exist. Unable to proceed", file=sys.stderr)
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

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    check_root()
    validate_hostname_path(hostname_file)
    validateLogPath(log_path)
    validateLogFile(log_file_path)

    command = ["reboot"]

    try:
        current_time = timestamp()
        with open(hostname_file, "w") as file:
            file.write("dnsserver1")
        with open(log_file_path, "a") as f:
            f.write(f"{current_time} - Hostname set to dnsserver1\n")
        print(f"Hostname set to dnsserver1")
        print("Rebooting machine")
        subprocess.run(command, check=True)
    except Exception as e:
        current_time = timestamp()
        with open(log_file_path, "a") as f:
            f.write(f"{current_time} - Hostname failed to update to dnsserver1\n")
            print(f"Hostname failed to update to dnsserver1: {e}")
        print(f"Hostname failed to update to dnsserver1: {e}")

if __name__ == "__main__":
    main()
