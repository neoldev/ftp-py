# ftp-py
This Python script sets up a simple FTP server using the pyftpdlib library, allowing multiple users to connect and transfer files.

## Getting started
To get started, run the following command: 

```bash
# Start the server
py ftp_server.py
```

## Getting started
To get started, run the following command:

```bash
# Start the server
py ftp_server.py
```

Once connected should look like this from the client:

```bash
PS C:\Coding\> py ftp_server.py
FTP server started. Connect to: ftp://192.168.68.63:21
Press Ctrl+C to quit.
[I 2023-11-26 16:22:53] concurrency model: async
[I 2023-11-26 16:22:53] masquerade (NAT) address: None
[I 2023-11-26 16:22:53] passive ports: None
[I 2023-11-26 16:22:53] >>> starting FTP server on 127.0.0.0:21, pid=21604 <<<
```

To connect to it, use this command:

```bash
# Connect to it
ftp 127.0.0.1
admin
admin
```

Once connected should look like this from the client side:

```bash
C:\Users\Noel>ftp 127.0.0.1
Connected to 127.0.0.1.
220 pyftpdlib 1.5.9 ready.
530 Log in with USER and PASS first.
User (127.0.0.1:(none)): admin
331 Username ok, send password.
Password:
230 Login successful.
ftp>
```

Once connected should look like this from the server side:

```bash
[I 2023-11-26 16:22:53] >>> starting FTP server on 127.0.0.0:21, pid=21604 <<<
[I 2023-11-26 16:26:06] 127.0.0.1:52795-[] FTP session opened (connect)
[I 2023-11-26 16:26:12] 127.0.0.1:52795-[admin] USER 'admin' logged in.
```