#!/usr/bin/env python3
import socket
from datetime import datetime

def iniciarCliente(host, puerto):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((host, puerto))
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    stamp = datetime.fromtimestamp(timestamp)
    c.send(str(stamp).encode("utf-8"))
    c.close()

def reciv(host,puerto):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, puerto))
    s.listen(5) 

    while True:

        (c, addr) = s.accept()

        print("Se estableció conexión con: %s" % str(addr))

        msg = 'Conexión establecida con : %s' % socket.gethostname() + "\r\n"
        c.send(msg.encode('utf8'))
        msg_rec = c.recv(1024)
        print(msg_rec.decode("ascii"))  
        c.close()
    
    

if __name__ == "__main__":
    
    hostprocesoB = "172.17.33.38" 
    puertoprocesoB = 44440
    hostprocesoC = "10.251.44.187"
    puertoprocesoC = 58695

    iniciarCliente(hostprocesoB, puertoprocesoB)
    reciv(hostprocesoC,puertoprocesoC)
    