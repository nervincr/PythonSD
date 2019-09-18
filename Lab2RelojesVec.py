#!/usr/bin/env python3
import socket
import threading
import logging

def server(proceso, arreglo, host, puerto):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, puerto))
    s.listen()

    while True:
        (c, addr) = s.accept()

        recv = c.recv(1024).decode("utf-8")

        arreglo[int(recv.split(',')[0])] = int(recv.split(',')[1])
        arreglo[proceso] = arreglo[proceso] + 1

        c.close()

        logging.critical(','.join(str(e) for e in arreglo))
        f=open("log.txt","a+")
        f.write(','.join(str(e) for e in arreglo))
        f.close()

if __name__ == "__main__":
    ipsprocesos = ["172.17.117.131", "172.17.117.131", "172.17.117.131"]
    puertosprocesos = [8081, 8082, 8083]
    arreglo = [0, 0, 0]
    
    proceso = int(input("Definir numero de proceso: "))

    print("Iniciando servidor en: {} : {}".format(ipsprocesos[proceso], puertosprocesos[proceso]))

    x = threading.Thread(target=server, args=(proceso, arreglo, ipsprocesos[proceso], puertosprocesos[proceso]))
    x.start()

    while True:
        enviar = int(input("Indicar proceso para enviar peticion: "))

        arreglo[proceso] = arreglo[proceso] + 1

        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect((ipsprocesos[enviar], puertosprocesos[enviar]))
        c.send("{},{}".format(proceso, arreglo[proceso]).encode("utf-8"))
        c.close()

        logging.critical(','.join(str(e) for e in arreglo))
        f=open("log.txt","a+")
        f.write(','.join(str(e) for e in arreglo))
        f.close()
    