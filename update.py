
import subprocess

updates = ["apt-get update","apt-get upgrade -y","apt-get dist-upgrade -y","apt-get clean","apt-get autoremove -y"]

def update(lst):

        for i in lst:

                command = ["bash", "-c", i]

                try:
                        subprocess.run(command, check=True)
                        print(f"Success: {i}")
                except subprocess.CalledProcessError:
                        print(f"Failed: {i}")


update(updates)