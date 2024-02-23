import os
import zipfile

def find_exe_files(directory):
    exe_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".exe"):
                exe_files.append(os.path.join(root, file))
    return exe_files

def copy_to_zip(files, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))

if __name__ == "__main__":
    directory = input("Enter the directory to search for exe files: ")
    zip_filename = input("Enter the name of the zip file to create: ")
    
    exe_files = find_exe_files(directory)
    if exe_files:
        copy_to_zip(exe_files, zip_filename)
        print("Exe files copied to", zip_filename)
    else:
        print("No exe files found in the directory.")
