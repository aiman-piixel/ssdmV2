import os
from pathlib import Path
import shutil

currentPath = Path.cwd()
configPath = currentPath / "config.json"
csvPath = currentPath / "data"

def split_folder(initial_folder, output_folder_base, num_folders):
    # Get the list of CSV files in the input folder
    csv_files = [f for f in os.listdir(initial_folder) if f.endswith('.csv')]

    # Calculate the number of files to put in each new folder
    files_per_folder = len(csv_files) // num_folders

    # Create new folders
    for i in range(num_folders):
        output_folder = os.path.join(output_folder_base, f'ssdm_{i + 1}')
        os.makedirs(output_folder, exist_ok=True)

        # Move files to the new folder
        start_index = i * files_per_folder
        end_index = (i + 1) * files_per_folder if i < num_folders - 1 else None
        for csv_file in csv_files[start_index:end_index]:
            src_path = os.path.join(initial_folder, csv_file)
            dst_path = os.path.join(output_folder, csv_file)
            shutil.copy(src_path, dst_path)
            
def split(folder):
    initial_folder = csvPath
    output_folder_base = currentPath / "ssdm_split"
    
    if os.path.exists(str(output_folder_base)):
        shutil.rmtree(str(output_folder_base))  # Remove the existing directory and its contents
    os.makedirs(str(output_folder_base))
    
    num_folders = folder

    split_folder(initial_folder, output_folder_base, num_folders)
    print(f"CSV files has been distributed to { num_folders } different folder(s)")


