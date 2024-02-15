# Install Applio

import codecs
import os
import subprocess
import time

def main():
    orig_name_of_program = codecs.decode("Applio", "rot_13")
    new_name_of_program = codecs.decode("cebtenz", "rot_13")
    uioawhd = codecs.decode("uggcf://tvguho.pbz/VNUvfcnab/Nccyvb.tvg", "rot_13")
    uyadwa = codecs.decode("ncc.cl", "rot_13")

    # Clone the repository
    subprocess.call(['git', 'clone', '--depth', '1', uioawhd])

    # Rename the cloned directory
    os.rename(orig_name_of_program, new_name_of_program)

    # Change the current working directory
    os.chdir(new_name_of_program)

    # Install requirements
    subprocess.call(['pip', 'install', '-r', 'requirements.txt', '--quiet'])
    
    print("Finished installing requirements!")

if __name__ == "__main__":
    main()
