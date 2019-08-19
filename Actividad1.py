import time
import xml.etree.ElementTree as ET
from noticia import Noticia

def print_menu():
    print( 30 * "-")
    print( "1. Agregar Noticia")
    print( "2. Exportar XML")
    print( "3. Importar XML")
    print( "4. Exit")
    print( 67 * "-")

def agregarNoticia(parameter_list):
    print("")
    
def main():
    loop=True      
    lNoticias = [Noticia('1', '1', '1', '1')]
    templNoticias = []

    while loop:
        print_menu()
        choice = input("Enter your choice [1-5]: ")
        
        if choice=='1':     
            print("Menu 1 has been selected")
            codigo = input("Ingrese el codigo: ")
            ambito = input("Ingrese el ambito: ")
            fecha = input("Ingrese el fecha: ")
            descripcion = input("Ingrese el descripcion: ")
            lNoticias.append(Noticia(codigo, ambito, fecha, descripcion))
                
        elif choice=='2':
            print ("Menu 2 has been selected")
            xmlNoticias = ET.Element("Noticias")
            for lNoticia in lNoticias:
                xmlNoticia = ET.SubElement(xmlNoticias, "Noticia")
                xmlNoticia.set('codigo',lNoticia.codigo)
                xmlNoticia.set('ambito',lNoticia.ambito)
                xmlNoticia.set('fecha',lNoticia.fecha)
                xmlNoticia.set('descripcion',lNoticia.descripcion)
            
            xmlTree = ET.ElementTree(xmlNoticias)
            xmlTree.write('noticias.xml', encoding='utf-8', method='xml', xml_declaration=True)
            
                
            
        elif choice=='3':
            print ("Menu 3 has been selected")
            templNoticias = ET.parse("./noticias.xml").getroot()
            for noticia in templNoticias:
                lNoticias.append(noticia)
                print(noticia.tag, noticia.attrib)
                
        elif choice=='4':
            print ("Menu 5 has been selected")
            
            loop=False

if __name__== "__main__":
    main()