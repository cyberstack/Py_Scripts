# This script unzips a files in dir_name and delets the zip file
# when done.


import os, zipfile

dir_name = "C:\\Users\\Folder_To_Use" #Folder Name

extension = ".zip" # Extention

os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name): # Loop through items in dir_name
    if item.endswith(extension): # Check for files ending in .zip
        file_name = os.path.abspath(item) # Get full path name of files
        zip_ref = zipfile.ZipFile(file_name) # Create zipfile object
        zip_ref.extractall(dir_name) # Extract file to dir_name
        zip_ref.close() # Close file
        os.remove(file_name) # Delete zipped file
