import socket
import datetime

class myMath:
    def get_Sumar(self, val1, val2):
        result = int(val1) + int(val2)
        return "{} + {} = {}".format(val1,val2,result)
    def get_Restar(self, val1, val2):
        result = int(val1) - int(val2)
        return "{} - {} = {}".format(val1,val2,result)
    def get_Multiplicar(self, val1, val2):
        result = int(val1) * int(val2)
        return "{} * {} = {}".format(val1,val2,result)
    def get_Dividir(self, val1, val2):
        result = int(val1) / int(val2)
        return "{} / {} = {}".format(val1,val2,result)
def main():
    HOST = socket.gethostbyname(socket.gethostname()) #Optiene la IP local si tiene interfaz de red
    PORT = 8080                                       #con virtual Box se debe desactivar.
    NOW = datetime.datetime.now()
    x = 0
    y = 0
    my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    my_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    my_socket.bind((HOST,PORT))
    my_socket.listen(1)
    mat = myMath()
    print('Serving on: {}:{}'.format(HOST,PORT))

    while True:
        connection,address = my_socket.accept()
        request = connection.recv(1024).decode('utf-8')
        try:
            params_list = request.split(' ')
            method = params_list[0]
            operationAndParams = params_list[1].split('?')
            operation = operationAndParams[0].lstrip('/')
            params = operationAndParams[1].split('&')
            if (params[0].split('=')[0].lower() == 'x'):
                x = params[0].split('=')[1]
                y = params[1].split('=')[1]
            elif (params[0].split('=')[0].lower() == 'y'):
                y = params[0].split('=')[1]
                x = params[1].split('=')[1]
            
            if (operation.lower() == 'sumar'):
                result = mat.get_Sumar(x, y)
            elif (operation.lower() == 'restar'):
                result = mat.get_Restar(x, y)
            elif (operation.lower() == 'multiplicar'):
                result = mat.get_Multiplicar(x, y)
            elif (operation.lower() == 'dividir'):
                result = mat.get_Dividir(x, y)
            else:
                header = 'HTTP/1.1 404 Not Found\n\n'
                response = '<!DOCTYPE html><html lang="en"><title>Error</title><meta charset="UTF-8"><body><center><h3>Error 404: Operation not found</h3><p>Python HTTP Server</p></center></body></html>'.encode('utf-8')

            header = 'HTTP/1.1 200 OK\n'
            header += 'Date: {}\n'.format(NOW.ctime())
            header += 'Server: Laboratorio 1 - Webservers\n'
            header += 'Connection: close\n'
            header += 'Content-Type: text/html\n\n'
            response = '<!DOCTYPE html><html lang="en"><title>Éxito</title><meta charset="UTF-8"><body><center><h3>Calculo Realizado</h3><p>Operación {}</p></center></body></html>'.format(result).encode('utf-8')
        except Exception: 
            header = 'HTTP/1.1 404 Not Found\n\n'
            response = '<!DOCTYPE html><html lang="en"><title>Error</title><meta charset="UTF-8"><body><center><h3>Error : Exeption</h3><p>Python HTTP Server</p></center></body></html>'.encode('utf-8')
    
        final_response = header.encode('utf-8')
        final_response += response
        connection.send(final_response)
        connection.close()

if __name__== "__main__":
    main()