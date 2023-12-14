import pymongo
from sshtunnel import SSHTunnelForwarder

# SSH connection details
ssh_host = '3.1.2.90'
ssh_port = 22
ssh_username = 'ubuntu'
ssh_private_key = '/home/piixel/studentqr.pem'  # Replace with the actual path to your private key file

# MongoDB connection details
mongo_host = 'localhost'
mongo_port = 27017
mongo_database = 'musleh-api'

# Create an SSH tunnel
with SSHTunnelForwarder(
    (ssh_host, ssh_port),
    ssh_username=ssh_username,
    ssh_pkey=ssh_private_key,
    remote_bind_address=(mongo_host, mongo_port)
) as tunnel:
    # Connect to the MongoDB server through the SSH tunnel
    client = pymongo.MongoClient('localhost', tunnel.local_bind_port)
    db = client[mongo_database]
    
    # Print the list of collections
    print(db.list_collection_names())
    
    # Close the MongoDB connection
    client.close()

