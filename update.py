
import subprocess

updates = ["dnf update","dnf upgrade -y","dnf dist-upgrade -y","dnf clean","dnf autoremove -y"]

def update(lst):

        for i in lst:

                command = ["bash", "-c", i]

                try:
                        subprocess.run(command, check=True)
                        print(f"Success: {i}")
                except subprocess.CalledProcessError:
                        print(f"Failed: {i}")


update(updates)
