import os
import hashlib
import zipfile

def get_executables(directory):
    executables = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".exe"):
                executables.append(os.path.join(root, file))
    print('Found: ' + str(len(executables) + ' exe files.'))
    return executables

def compute_hash(file_path):
    hasher = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while True:
                data = f.read(65536)  # 64 KB buffer
                if not data:
                    break
                hasher.update(data)
    except IOError:
        print('Could not open ' + file_path + '. Moving on.')
    return hasher.hexdigest()

def copy_to_zip(executables, output_file):
    print('Zipping exe files, duplicates expected.')
    with zipfile.ZipFile(output_file, "w") as zip_file:
        for exe in executables:
            hash_value = compute_hash(exe)
            try:
                zip_file.write(exe, arcname=hash_value + ".exe")
            except:
                continue

if __name__ == "__main__":
    directory = input("Enter directory to search for exe files in (most likely C:\): ")  # Change this to the directory you want to search for executables
    output_file = input("Enter the location where the zip file containing the exe files should be written to: ")
    executables = get_executables(directory)
    if executables:
        copy_to_zip(executables, output_file)
        print("Executable files copied to executables.zip")
    else:
        print("No executable files found.")

