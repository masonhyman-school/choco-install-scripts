import os
import hashlib
import zipfile

def get_executables(directory):
    executables = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".exe"):
                executables.append(os.path.join(root, file))
    return executables

def compute_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            data = f.read(65536)  # 64 KB buffer
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def copy_to_zip(executables):
    with zipfile.ZipFile("executables.zip", "w") as zip_file:
        for exe in executables:
            hash_value = compute_hash(exe)
            zip_file.write(exe, arcname=hash_value + ".exe")

if __name__ == "__main__":
    directory = "C:\\Program Files"  # Change this to the directory you want to search for executables
    executables = get_executables(directory)
    if executables:
        copy_to_zip(executables)
        print("Executable files copied to executables.zip")
    else:
        print("No executable files found.")

