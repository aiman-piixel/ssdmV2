import json
import pymongo
from sshtunnel import SSHTunnelForwarder
import pandas as pd
import os
import shutil
from bson import ObjectId
from datetime import datetime
from pathlib import Path

# Define a function to update column 'syncedBySchool' based on the values in column 'status'
def update_column(row):
    if row['status'] == 2:
        return 1  # Set 'syncedBySchool' to 1 when 'status' is 2
    else:
        return 0  # Set 'syncedBySchool' to 0 when 'status' is 1
    
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

def downnload(startYear, startMonth, startDay, endYear, endMonth, endDay, region):
    
    #datetime(day, month, year)
    start_date = datetime(startDay, startMonth, startYear)
    end_date = datetime(endDay, endMonth, endYear)

    current_dir = Path.cwd()
    config_dir = current_dir / "config.json"
    #this will configure your download folder
    download_dir = current_dir / "data"
    ssh_private_key = current_dir / "studentqr.pem"

    # Save the DataFrame to a CSV file
    if os.path.exists(str(download_dir)):
        shutil.rmtree(str(download_dir))  # Remove the existing directory and its contents
    os.makedirs(str(download_dir))

    # Read data from the JSON file
    with open(config_dir, 'r') as jsonfile:
        config = json.load(jsonfile)
        
    db = config['DATABASE']
    # SSH connection details
    sshHost = db['ssh_host']
    sshPort = db['ssh_port']
    sshUsername = db['ssh_username']

    # MongoDB connection details
    mongoHost = db['mongo_host']
    mongoPort = db['mongo_port']
    
    with SSHTunnelForwarder(
        (sshHost, sshPort),
        ssh_username=sshUsername,
        ssh_pkey=str(ssh_private_key),
        remote_bind_address=(mongoHost, mongoPort)
    ) as tunnel:
        # Connect to the MongoDB server through the SSH tunnel
        client = pymongo.MongoClient(mongoHost, tunnel.local_bind_port)
        database = client[db['database']]
        collection = database[db['collection']]

        #load school detail from config
        school = config[state_num(region)]
        synced = 0

        for row in school:
            # Define the filter criteria using the ObjectId instance
            filter_criteria = {"schoolID": ObjectId(row['mongoDB_ID']),
                            "created_at": {"$gte": start_date, "$lte": end_date}
                            }

            # Define the projection to exclude specific fields (e.g., "field_to_exclude")
            exclude = {"_id": 0, "tempat":0, "ic":0, "userID":0, "schoolID":0, "teacherID":0,
            "studentID":0, "kelasID":0, "positiveID":0, "method":0, "updated_at":0,
            "created_at":0, "submissionID":0, "year":0}
            results = collection.find(filter_criteria, exclude)
            
            #turn query result into dataframe
            df = pd.DataFrame(list(results))
            df['synced'] = synced
            
            #do not print to csv if empty
            if df.empty:
                print(row['NAME'] + " has no submissions")
                continue
            
            #output to csv
            df.to_csv(str(download_dir) + "/" + row['NAME'] + ".csv", index=False)
            print(row['NAME'] + " data has been generated")
            
            #set all filtered item to inactive (1:active, 2:inactive)
            results = collection.update_many(filter_criteria, {"$set": {"status": 2}})
            
        client.close()


