import os
import subprocess
import win32api
import hashlib

def get_certificate_info(file_path):
    try:
        # Use Windows certutil command to extract certificate information
        output = subprocess.check_output(['certutil', '-v', '-dump', file_path], stderr=subprocess.STDOUT, shell=True)
        output = output.decode('utf-8')
        
        # Extracting relevant information
        issuer = output[output.find("Issuer:") + 8:output.find("NotBefore")]
        subject = output[output.find("Subject:") + 9:output.find("Issuer")]
        thumbprint = output[output.find("Thumbprint (SHA1):") + 20:output.find("Cert Hash")]
        
        return issuer.strip(), subject.strip(), thumbprint.strip()
    except subprocess.CalledProcessError as e:
        return None, None, None

def find_exe_files(directory):
    exe_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.exe'):
                exe_files.append(os.path.join(root, file))
    return exe_files

def main():
    directory_to_search = 'C:\\'  # Change this to the directory you want to search
    exe_files = find_exe_files(directory_to_search)
    
    for exe_file in exe_files:
        issuer, subject, thumbprint = get_certificate_info(exe_file)
        if issuer is not None:
            print("File:", exe_file)
            print("Issuer:", issuer)
            print("Subject:", subject)
            print("Thumbprint:", thumbprint)
            print("---------------------------------------")

if __name__ == "__main__":
    main()

