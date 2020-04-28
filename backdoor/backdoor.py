#Set Socket Options
#https://www.ibm.com/support/knowledgecenter/en/ssw_ibm_i_71/apis/ssocko.htm
#https://docs.microsoft.com/en-us/windows/win32/winsock/sol-socket-socket-options
#https://www.gnu.org/software/libc/manual/html_node/Socket_002dLevel-Options.html#Socket_002dLevel-Options
#Allows a socket to bind to an address and port already in use. The SO_EXCLUSIVEADDRUSE option can prevent this.

import socket, platform, os

SRV_ADDR = ""
SRV_PORT = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
connection, address = s.accept()
while 1:
    try:
        data = connection.recv(1024)
    except:continue
    
    if(data.decode('utf-8') == '1'):
        tosend = platform.platform() + " " + platform.machine()
        connection.sendall(tosend.encode())
    elif(data.decode('utf-8') == '2'):
        data = connection.recv(1024)
        print(data.decode('utf-8'))
        try:
            filelist = os.listdir(data.decode('utf-8'))
            tosend = ""
            for x in filelist:
                tosend += "," + x
        except:
            tosend = "Wrong path"
        connection.sendall(tosend.encode())
    elif(data.decode('utf-8') == '0'):
        connection.close()
        connection, address = s.accept()
