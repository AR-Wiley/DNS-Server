import os
import sys

home_dir = "/home"
dns_admin_dir = "/home/dnsadmin"
dns_admin_sub_dir = ["backups", "config-mgmt", "dns", "docs", "scripts", "security", "staging", "tmp"]

def check_root():
    if os.getuid() != 0:
        print("This sript must be run as root", file=sys.stderr)
        sys.exit(1)

def home_dir_validation(path):
    if not os.path.exists(path):
        print(f"{path} does not exist...")
        sys.exit(1)

def dns_admin_dir_validation(path):
    if not os.path.exists(path):
        print("{path} does not exist")
        print("Creating {path}")
        try:
            os.makedirs(path)
            print("{path} has been created")
            print(path)
        except Exception as e:
            print(f"An error has occured in creating {path}: {e}")


def dns_admin_subdir_validation(adminDir, subDir):
    for i in subDir:
        if not os.path.exists(os.path.join(adminDir, i)):
            print(f"{i} does not exist...")
            print(f"Creating {i}...")
            try:
                os.makedirs(os.path.join(adminDir, i))
                print(f"{i} successfully created")
            except Exception as e:
                print(f"An error has occurred: {e}")
        else:
            print(f"{i} already exists")


check_root()
home_dir_validation(home_dir)
dns_admin_dir_validation(dns_admin_dir)
dns_admin_subdir_validation(dns_admin_dir, dns_admin_sub_dir)
