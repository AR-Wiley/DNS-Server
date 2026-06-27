import os
import sys

log_dir = "/var/log/SysAdmin-Logs"
log_file = ["updates.log", "intall.log"]


def check_root():

        if os.getuid() != 0:
                print("This sript must be run as root", file=sys.stderr)
                sys.exit(1)


def validate_path(path):

        if not os.path.exists(path):
                print("Path does not exist")
                print("Creating path")
                try:
                        os.makedirs(path)
                        print("Path has been created")
                        print(path)
                except Exception as e:
                        print(f"An error has occured: {e}")


def validate_file(path, files):

        for i in files:

                file_path = os.path.join(path, i)

                if not os.path.isfile(file_path):
                        print(f"Log file {i} does not exist")
                        print(f("Creating file {i}")

                        try:
                                with open(file_path, "x") as f:
                                        f.write(f"{i} ceated")

                                print(f"Created: {i}")

                        except FileExistsError:
                                print(f"{i} already exits.")

                        except Exception as e:
                                print(f"An error has occured: {e}")