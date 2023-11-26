from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import signal
import os
import socket

class MyHandler(FTPHandler):
    def on_file_received(self, file):
        print(f"File '{file}' has been received and stored on the server.")

def get_ip_address():
    # Get the local IP address of the server
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't actually send data
        s.connect(('10.255.255.255', 1))
        ip_address = s.getsockname()[0]
    except Exception:
        ip_address = '127.0.0.1'
    finally:
        s.close()
    return ip_address 

def create_ftp_server():
    # Create an authorizer for user authentication
    authorizer = DummyAuthorizer()

    # Add users dynamically based on your requirements
    add_users(authorizer)

    # Create an FTP handler and associate the authorizer
    handler = FTPHandler
    handler.authorizer = authorizer
    
    # Create the FTP server with the handler and listen on a specific address and port
    server = FTPServer(("127.0.0.1", 21), handler)
    
    # Add a signal handler to quit the server on Ctrl+C
    signal.signal(signal.SIGINT, lambda signum, frame: server.stop())

    return server

def add_users(authorizer):
    # Add users with their respective permissions
    # perm=elr to read
    # perm=adfmwMT to write
    user_data = [
        {"username": "admin", "password": "admin", "directory": r"C:\Coding\ftp-py", "perm": "elradfmwMT"},
        {"username": "someuser", "password": "12345", "directory": r"C:\Coding\ftp-py\users\someuser", "perm": "elr"},
        # Add more users as needed
    ]

    for user in user_data:
        authorizer.add_user(user["username"], user["password"], user["directory"], perm=user["perm"])

if __name__ == "__main__":
    # Create and start the FTP server
    ftp_server = create_ftp_server()
    ip_address = get_ip_address()
    print(f"FTP server started. Connect to: ftp://{ip_address}:21")
    print("Press Ctrl+C to quit.")
    ftp_server.serve_forever()