from ast import Num
from pathlib import Path
import subprocess
import time
import multiprocessing
import threading

currentPath = Path.cwd()
scriptPath = currentPath / "syncSSDM.py"
target = str(scriptPath)
    
    
""" def run_target_script():
    while True:
        try:
            # Launch the target script using subprocess
            completed_process = subprocess.run(["python", AppDirectory.target])
            
            # Check if the target script completed successfully
            if completed_process.returncode == 0:
                print("Target script completed successfully.")
                break  # End the loop
            else:
                print(f"Target script returned non-zero exit code: {completed_process.returncode}")
            
        except Exception as e:
            print(f"Error encountered: {e}")
        
        # Wait for a certain duration before restarting
        print("Restarting the target script in 2 seconds...")
        time.sleep(2)  # You can adjust the duration as needed """

""" if __name__ == "__main__":
    #run_target_script()

 """

