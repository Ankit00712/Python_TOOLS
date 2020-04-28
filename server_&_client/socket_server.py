#try to use this to avoid unwanted input it might help  socket.shutdown(how)  or  sock.setblocking(True)
#https://docs.python.org/3/library/socket.html#socket-objects
import socket     
import time

SRV_ADDR = "192.168.70.130"
SRV_PORT = 44444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
print("Server started! Waiting for connections...")
connection, address = s.accept()
print('Client connected with address:', address)

while 1:
    connection.sendall(input("Your msg:").encode())     
    time.sleep(1)
    data = connection.recv(1024)     # confirmation from client
    print(data.decode('utf-8'))
    print('\nClient is sending :', end = '')   #not printing with new line
    data = connection.recv(1024)
    print(data.decode('utf-8'))
    if not data: break
    connection.sendall(b'-- Message Received by server--\n')
    
connection.close()
