import subprocess
import os
## this will show the directory listing
## for linux

if os.name == "nt":
    subprocess.call("dir",shell=True)
else:
    subprocess.call("ls",shell=True)
    

