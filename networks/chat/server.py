import socket

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("127.0.0.1", 7070))
server_socket.listen()

user_db = {}

while(1):
    client_socket, addr = server_socket.accept()
    data = client_socket.recv(100).decode('ascii')
    print(data)
    if(data == "REGISTER"):
        print(addr)
        server_socket.connect(addr)
        prompt = "Enter your Username: "
        server_socket.send("prompt")
#         username = server_socket.recv(100)
#         user_db[username]=(client_socket, addr)
#         user_db.append()
#         print(user_db)

# client_socket.close()
# server_socket.close()