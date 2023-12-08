from pathlib import Path
from multiprocessing import Process
import subprocess
import time
import update_login
import split
import download_data

startD = 0; startM = 0; startY = 0; endD = 0; endM = 0; endY = 0; region = ""; folder=0

class AppDirectory():    
    currentPath = Path.cwd()
    configPath = currentPath / "config.json"
    csvPath = currentPath / "data"
    target = currentPath / "syncSSDM.py"
    
class MainVariable:
    startDay = startD; startMonth = startM; endYear = startY
    endDay = endD; endMonth = endM; endYear = endY
    numFolder = folder; state=region

def run_target_script(folder_num):
    # Function to run the target script
    while True:
        try:
            completed_process = subprocess.run(["python", str(AppDirectory.target), str(folder_num)])
            if completed_process.returncode == 0:
                print("Target script completed successfully.")
                break
            else:
                print(f"Target script returned non-zero exit code: {completed_process.returncode}")
        except Exception as e:
            print(f"Error encountered: {e}")
        print("Restarting the target script in 2 seconds...")
        time.sleep(2)

def main():
    print("Starting script..."); time.sleep(1)
    print("Would you like to continue from previous session? [y/n]: ")
    restart = str(input())
    if restart == "no" or restart == "NO" or restart == "n":
        print("Key in a number based on state/district :")
        print("1. PAHANG")
        print("2. PERAK")
        print("3. TERENGGANU")
        print("4. PERLIS")
        print("5. SELANGOR")
        print("6. NEGERI SEMBILAN")
        print("7. JOHOR")
        print("8. KELANTAN")
        print("9. KEDAH")
        print("10. PULAU PINANG")
        print("11. MELAKA")
        print("12. SABAH")
        print("13. SARAWAK")
        print("14. W.P KUALA LUMPUR")
        print("15. W.P LABUAN")
        print("16. W.P PUTRJAYA")
        print("17. MALAYSIA***")
        i=0
        while i < 17:
            region = int(input())
            if region < 1 or region > 17:
                print("Please enter a number between 1 and 17")
                continue
            else:
                break
            
        print("Have you downloaded the required csv? [y/n]: ")
        skipDown = str(input())
        if skipDown == "no" or skipDown == "NO" or skipDown == "n":
            print("Do you have access to production DB? [y/n]: ")
            DBaccess = str(input())
            if DBaccess == "no" or DBaccess == "NO" or DBaccess == "n":
                print("Please manually download the required files or place them inside the 'data' folder in the main directory")
                print("Exiting the script...")
                exit(None)
            else:
                print("Please enter start date and end date")
                print("Enter the start day --> {day/#/#}")
                startD = int(input())
                print("Enter the start month --> {#/month/#}")
                startM = int(input())
                print("Enter the start year --> {#/#/year}")
                startY = int(input())
                print("Enter the end day --> {day/#/#}")
                endD = int(input())
                print("Enter the end month --> {#/month/#}")
                endM = int(input())
                print("Enter the end year --> {#/#/year}")
                endY = int(input())
                
                print(f"\nStart date: {startD}/{startM}/{startY}")
                print(f"Start date: {endD}/{endM}/{endY}")

                print("Press ENTER to confirm. Press any other key to exit script...")
                enter = str(input())
                if enter == "":
                    print("...\n")
                else:
                    print("Exiting script...")
                    exit(None)
                
                time.sleep(1)
                print("Initiating download...")
                download_data.downnload(startD, startM, startY, endD, endM, endY, region)
                
                print("Press ENTER to proceed with syncing. Press any other key to exit and stop syncing process")
                enter = str(input())
                if enter == "":
                    print("...\n")
                else:
                    print("Exiting script...")
                    exit(None)
                    
        else:
            print("...\n")


        print("How many instances do you want to run?")
        folder = int(input())

        split.split(folder)
        update_login.updateLogin(folder, region)

        print(f"\nRunning {folder} window(s) in parallel...")
        

    else:
        print("How many instance(s) from last session?")
        folder = int(input())
        print("Continuing sync from last session...")
        time.sleep(1)

    numList = list(range(1, folder + 1))

    # Create and start multiple processes for running the target script
    processes = []
    for var in numList:
        process = Process(target=run_target_script, args=(var,))
        process.start()
        processes.append(process)

    # Wait for all processes to complete (this won't happen in this case)
    for process in processes:
        process.join()

if __name__ == "__main__":
    main()