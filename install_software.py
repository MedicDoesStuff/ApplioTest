import codecs
import os
import subprocess
import time

def main():
    # Decoded repository name and program name
    repo_name = codecs.decode("Nccyvb", "rot_13")
    program_name = codecs.decode("cebtenz", "rot_13")
    
    # Decoded GitHub URL of the repository to clone
    repo_url = codecs.decode("uggcf://tvguho.pbz/VNUvfcnab/Nccyvb.tvg", "rot_13")
    
    # Decoded name of the script to execute within the cloned repository directory (unused in this script)
    script_name = codecs.decode("ncc.cl", "rot_13")

    # Clone the repository
    subprocess.call(['git', 'clone', '--depth', '1', repo_url])

    # Rename the cloned directory
    os.rename(repo_name, program_name)

    # Change the current working directory
    os.chdir(program_name)

    # Install dependencies from requirements.txt
    subprocess.call(['pip', 'install', '-r', 'requirements.txt', '--quiet'])
    
    # Inform user that installation is complete
    print("Finished installing {} requirements!".format(program_name))

if __name__ == "__main__":
    main()
