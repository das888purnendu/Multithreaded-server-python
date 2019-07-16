from _thread import *
import socket
stop = False
port = 1022
sk = socket.socket()
sk.bind(('', port))
clients = set()
var = 0

def send(inn):
    global clients
    for c in clients:
        c.sendall(inn.encode())
        

def threaded (con):
    global var
    global clients
    global stop
    while True:
        rec = con.recv(1024).decode()
        if (rec=='exit'):
            print('Recived : Bye')
            clients.remove(con)
            con.close()
            break
        else:
            var+=1
            print('Recived : ',rec)
            if var==len(clients):
                inn = input('Send : ')
                send(inn)
                var = 0
                if (inn=='exit'):
                    stop = True
                    break
    sk.close()
    
    
sk.listen(5)
while True:
    if stop== True:
        break
    con, adr = sk.accept()
    print ('Connected with ip : ', adr)  
    con.send('Connection is established, Now you can send message to the server'.encode())
    clients.add(con)
    start_new_thread(threaded, (con,))