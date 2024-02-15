# Start Applio

import codecs
import os
import subprocess

def main():
    applio_script = codecs.decode("ncc.cl", "rot_13")

    # Start the TensorBoard server in the background with subprocess
    tensorboard_process = subprocess.Popen(['tensorboard', '--logdir', 'logs', '--bind_all'])

    # Run the Applio script
    subprocess.call(['python', applio_script, '--share'])

    # Keep the script running to allow TensorBoard and Applio to continue running
    # You might want to handle this differently depending on your needs.
    try:
        tensorboard_process.wait()
    except KeyboardInterrupt:
        # Terminate TensorBoard when the user interrupts (Ctrl+C)
        tensorboard_process.terminate()

if __name__ == "__main__":
    main()
