import os 
folders = input("enter folder names separated by spaces: ").split()  # convert string into list
print(folders)

for folder in folders: 
    try:
       files = os.listdir(folder) 
    except FileNotFoundError:
        print(f"Folder '{folder}' not found. Skipping...  ")
    except PermissionError:
        print(f"Permission denied to access folder '{folder}'. Skipping...  ")
    else:
        for file in files: 
            print(f"Processing file: {file} in folder: {folder}")
