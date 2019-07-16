import socket
ip = '127.0.0.1'
port = 1022
sk = socket.socket()
sk.connect((ip, port)) 
while True:
    
    
    rec = sk.recv(1024).decode()
    if (rec=='exit'):
        print('Recieved : Bye')
        sk.close()
        break
    else:
        print ('Recieved : ',rec )
    
    
    
    inn = input('Send : ')
    sk.sendall(inn.encode())
    
    if (inn=='exit'):
        sk.close()
        break
   
    