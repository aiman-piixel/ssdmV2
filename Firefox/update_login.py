import os
import json
import glob
from pathlib import Path
import pandas as pd
import csv

# Set paths and filenames
currentPath = Path.cwd()
current_dir = currentPath
config_dir = currentPath / "config.json"
output_folder_base = currentPath / "ssdm_split"

def state_num(region_num):
    if region_num == 1:
        return "PAHANG"
    elif region_num == 2:
        return "PERAK"
    elif region_num == 3:
        return "TERENGGANU"
    elif region_num == 4:
        return "PERLIS"
    elif region_num == 5:
        return "SELANGOR"
    elif region_num == 6:
        return "NEGERI SEMBILAN"
    elif region_num == 7:
        return "JOHOR"
    elif region_num == 8:
        return "KELANTAN"
    elif region_num == 9:
        return "KEDAH"
    elif region_num == 10:
        return "PULAU PINANG"
    elif region_num == 11:
        return "MELAKA"
    elif region_num == 12:
        return "SABAH"
    elif region_num == 13:
        return "SARAWAK"
    elif region_num == 14:
        return "W.P KUALA LUMPUR"
    elif region_num == 15:
        return "W.P LABUAN"
    elif region_num == 16:
        return "W.P PUTRAJAYA"
    elif region_num == 17:
        return "MALAYSIA"
    else:
        return "Invalid state"

def updateLogin(num_of_folders, region):
    while num_of_folders != 0:
        csv_dir = currentPath / f"ssdm_split/ssdm_{num_of_folders}"
        login_path = output_folder_base / f"login_{num_of_folders}.csv"

        # Read data from the JSON file
        with open(config_dir, 'r') as jsonfile:
            config = json.load(jsonfile)
        school = config.get(state_num(region), [])  # Use get() to handle missing key gracefully

        # Find all CSV files in data_ssdm directory
        csvFiles = glob.glob(os.path.join(str(csv_dir), "*.csv"))
        csvFiles.sort()

        csvNames = []
        for file in csvFiles:
            clean = file.replace(str(csv_dir)+'/','').replace('.csv','')
            csvNames.append(clean)

        # Define the list of headers
        headers = ['NAME', 'ssdmID', 'ssdmPass', 'done']  # Replace with your actual headers

        # Create and write to the CSV file
        with open(str(login_path), 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            
            # Write the headers to the CSV file
            csv_writer.writerow(headers)

        name_to_index = {name: index for index, name in enumerate(csvNames)}

        df = pd.read_csv(str(login_path))

        index = 0
        for row in school:
            name = row.get('NAME')
            if name in name_to_index:
                count = name_to_index[name]
                setName = row.get('NAME')
                setID = row.get('ID')
                setPass = row.get('PASS')
                df.at[count, 'NAME'] = setName
                df.at[count, 'ssdmID'] = setID
                df.at[count, 'ssdmPass'] = setPass
                print(row['NAME'] + f" detail has been included in login_{num_of_folders}.csv ")
                index += 1

        # Reset completion value
        df['done'] = 0

        df.to_csv(str(login_path), index=False)
        num_of_folders -= 1
        print("Login csv has been updated successfully")
        
    print("Update process completed successfully")



