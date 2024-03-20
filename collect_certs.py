import os
import sys
from OpenSSL import crypto

def extract_certificates(exe_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(exe_dir):
        if file_name.endswith(".exe"):
            file_path = os.path.join(exe_dir, file_name)
            try:
                cert = crypto.load_certificate(crypto.FILETYPE_PEM, crypto.verify(
                    file_path, None))
                cert_pem = crypto.dump_certificate(
                    crypto.FILETYPE_PEM, cert).decode('utf-8')
                cert_name = os.path.splitext(file_name)[0] + ".pem"
                cert_path = os.path.join(output_dir, cert_name)
                with open(cert_path, 'w') as f:
                    f.write(cert_pem)
                print(f"Certificate extracted from {file_name} and saved as {cert_name}")
            except Exception as e:
                print(f"Failed to extract certificate from {file_name}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_directory> <output_directory>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]

    if not os.path.isdir(input_directory):
        print("Input directory does not exist.")
        sys.exit(1)

    extract_certificates(input_directory, output_directory)
