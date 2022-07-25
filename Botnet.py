import socket

server_ip = "localhost"
port = 7658
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server_ip, port))
s.listen(5)
clients = []

print("Waiting for Connections")

def send_msg(msg):
    for client in clients:
        client.send(bytes(f"{str(msg)}", "utf-8"))
    print(f"Sent to all clients")

while True:
    client, ip = s.accept()
    clients.append(client)
    print(f"{ip} Connected")
    message = input("Enter a message: ")
    send_msg(msg=message)