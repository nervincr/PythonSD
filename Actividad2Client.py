import xml.etree.ElementTree as ET
import socket
from noticia import Noticia

def print_menu():
    print( 67 * "-")
    print( "1. Run Client")
    print( "2. Exit")
    print( 67 * "-")

def main():
    loop = True
    lNoticias = []
    HOST = '172.17.117.131'
    PORT = 65432

    while loop:
        print_menu()
        choice = input("Enter your choice [1-2]: ")

        if choice=='1':
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                data = s.recv(1024)

            print('Received', repr(data))
            lNoticias = []
            templNoticias = ET.fromstring(data)
            for noticia in templNoticias:
                lNoticias.append(Noticia(noticia.attrib["codigo"], noticia.attrib["ambito"], noticia.attrib["fecha"], noticia.attrib["descripcion"]))

            for lnoticia in lNoticias:
                lnoticia.visualizar()
    
        elif choice=='2':
            print ("Menu 2 has been selected")
            
            loop=False

if __name__== "__main__":
    main()