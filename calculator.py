import socket
import signal
import sys

ClientSocket = socket.socket()
host = '192.168.56.105'
port = 8080

print('Connecting to server......')
print('Connected YEAYY!!!')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response.decode("utf-8"))
while True:

    Input = input('\t\t\t   Enter the function with  number: ')
 
    if Input == 'exit':
        break
    else:
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode("utf-8"))

ClientSocket.close()
