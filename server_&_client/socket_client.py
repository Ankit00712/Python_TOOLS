import socket
import time

DES_ADDR = "192.168.70.130"         #input("Type the server IP address: ")
DES_PORT =  44444                   #int(input("Type the server port: "))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((DES_ADDR , DES_PORT))

print('Client connected to Server address:', DES_ADDR)
print('Server will be sending msg so wait\n')
while 1:
    print('\nServer is sending :', end = '')
    data = client.recv(1024)
    print(data.decode('utf-8')) 
    if not data: break
    client.sendall(b'-- Message Received by client--\n')   # b- converting to byte (encoding)
    client.sendall(input("Your msg:").encode())
    time.sleep(1)
    data = client.recv(1024)        #receiving confirmation from server
    print(data.decode('utf-8'))    
client.close()

#https://stackoverflow.com/questions/34252273/what-is-the-difference-between-socket-send-and-socket-sendall
