import socket

server_ip = "localhost"
port = 7658

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, port))

while True:
    msg_from_botnet = s.recv(1024)
    print(msg_from_botnet.decode("utf-8"))