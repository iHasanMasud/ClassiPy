import os
import shutil
import time

# Directory to be monitored
directory = input("Please enter the directory full path: ")
directory = os.path.normpath(directory)
if not os.path.isdir(directory):
    raise Exception("The directory path entered is not a valid directory.")

print('Monitoring directory: ' + directory)

# Dictionary of file categories and their extensions
categories = {
    'Images': ['jpeg', 'jpg', 'png'],
    'PDFs': ['pdf'],
    'Datasets': ['csv', 'xlsx', 'json'],
    'Videos': ['mp4'],
    'Zips': ['zip', 'rar'],
    'Executables': ['exe', 'msi'],
    'Documents': ['docx', 'txt'],
    'Audio': ['mp3'],
    'Database': ['sql'],
    'Others': []
}

# Create a loop to create directories and classify files using categories keys
for category in categories.keys():
    # Create directory if not exists
    if not os.path.exists(os.path.join(directory, category)):
        os.makedirs(os.path.join(directory, category))
    # os.makedirs(os.path.join(directory, category), exist_ok=True)


# Function to classify a file
def classify_file(filename):
    source_path = os.path.join(directory, filename)
    # check if its directory then return
    if os.path.isdir(source_path):
        return
    # Find the file extension
    extension = filename.split('.')[-1]
    # Iterate over the categories
    for category, extensions in categories.items():
        # If the extension matches one of the extensions in the category, move the file
        if extension in extensions:
            # Construct the file paths
            dest_path = os.path.join(directory, category, filename)
            # check if file already exist in the destination
            if os.path.exists(dest_path):
                i = 1
                while True:
                    root, ext = os.path.splitext(dest_path)
                    temp_path = f"{root}_{i}{ext}"
                    if not os.path.exists(temp_path):
                        dest_path = temp_path
                        break
                    i += 1
                shutil.copy2(source_path, dest_path)
                print(f'{filename} already exist, Copy made with name {os.path.basename(dest_path)}')
            else:
                os.rename(source_path, dest_path)
                print(f'Moved {filename} to {category}')
            break
    else:
        dest_path = os.path.join(directory, 'Others', filename)
        if os.path.exists(dest_path):
            i = 1
            while True:
                root, ext = os.path.splitext(dest_path)
                temp_path = f"{root}_{i}{ext}"
                if not os.path.exists(temp_path):
                    dest_path = temp_path
                    break
                i += 1
            # shutil.copy2(source_path, dest_path)
            os.rename(source_path, dest_path)
            print(f'{filename} already exist, Copy made with name {os.path.basename(dest_path)}')
        else:
            os.rename(source_path, dest_path)
            print(f'Moved {filename} to Others')


# Classify all existing files in the directory
for filename in os.listdir(directory):
    classify_file(filename)

# Initial list of files in the directory
initial_files = os.listdir(directory)

while True:
    # List of files in the directory after a short sleep
    time.sleep(5)
    current_files = os.listdir(directory)

    # Find the new files
    new_files = list(set(current_files) - set(initial_files))

    # Classify the new files
    for filename in new_files:
        classify_file(filename)

    # Update the initial list of files
    initial_files = current_files
