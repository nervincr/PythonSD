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

        recv = c.recv(1024).decode("utf-8").split(',')

        if arreglo[0] < int(recv[0]):
            arreglo[0] = int(recv[0])
        if arreglo[1] < int(recv[1]):
            arreglo[1] = int(recv[1])
        if arreglo[2] < int(recv[2]):
            arreglo[2] = int(recv[2])

        arreglo[proceso] = arreglo[proceso] + 1

        c.close()

        logging.critical(",".join(str(e) for e in arreglo))
        f=open("log.txt","a+")
        f.write(",".join(str(e) for e in arreglo) + "\n")
        f.close()

if __name__ == "__main__":
    ipsprocesos = ["172.17.117.131", "172.17.117.148", "172.17.117.145"]
    # ipsprocesos = ["172.17.117.131", "172.17.117.131", "172.17.117.131"]
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
        c.send(",".join(str(e) for e in arreglo).encode("utf-8"))
        c.close()

        logging.critical(",".join(str(e) for e in arreglo))
        f=open("log.txt","a+")
        f.write(",".join(str(e) for e in arreglo) + "\n")
        f.close()
    