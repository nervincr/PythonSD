import xml.etree.ElementTree as ET
import socket
from noticia import Noticia

def print_menu():
    print( 67 * "-")
    print( "1. Agregar Noticia")
    print( "2. Run Server")
    print( "3. Exit")
    print( 67 * "-")
    
def main():
    loop=True      
    lNoticias = [Noticia('1', '1', '1', '1'),Noticia('2', '2', '2', '2'),Noticia('3', '3', '3', '3')]
    HOST = '172.17.117.131'
    PORT = 65432

    while loop:
        print_menu()
        choice = input("Enter your choice [1-3]: ")
        
        if choice=='1':     
            print("Menu 1 has been selected")
            codigo = input("Ingrese el codigo: ")
            ambito = input("Ingrese el ambito: ")
            fecha = input("Ingrese el fecha: ")
            descripcion = input("Ingrese el descripcion: ")
            temp = Noticia(codigo, ambito, fecha, descripcion)
            temp.visualizar()
            lNoticias.append(temp)

        elif choice=='2':
            print ("Menu 2 has been selected")
            xmlNoticias = ET.Element("Noticias")
            for lNoticia in lNoticias:
                xmlNoticia = ET.SubElement(xmlNoticias, "Noticia")
                xmlNoticia.set('codigo',lNoticia.codigo)
                xmlNoticia.set('ambito',lNoticia.ambito)
                xmlNoticia.set('fecha',lNoticia.fecha)
                xmlNoticia.set('descripcion',lNoticia.descripcion)
            
            xmlStrg = ET.tostring(xmlNoticias, encoding='utf-8', method='xml')

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((HOST, PORT))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    conn.sendall(xmlStrg)
            
        elif choice=='3':
            print ("Menu 3 has been selected")
            
            loop=False

if __name__== "__main__":
    main()