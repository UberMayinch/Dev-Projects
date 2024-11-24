import socket

socket = socket.socket()
socket.bind(("127.0.0.1", 8080))
socket.connect(("127.0.0.1", 7070))

buffer = "REGISTER"
socket.listen()
socket.accept()
socket.send(buffer.encode())
a = socket.recv(100)
# data = input()
# socket.send(data.encode())
# socket.recv()

# while(1):
#     socket.recv()
#     msg = input()
#     if(msg == 'EXIT'):
#         exit(1)
#     else:
#         socket.send(data.encode)

