import socket
import sys
from datetime import datetime

def enviarC(host, puerto, msg_env):
	c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	c.connect((host, puerto))
	#msg_rec = c.recv(1024)
	#print (msg_rec.decode('utf8'))
	#timestamp
	now = datetime.now()
	timestamp = datetime.timestamp(now)
	stamp = datetime.fromtimestamp(timestamp)
	c.send(str(stamp).encode("utf-8"))
	#msg_rec = c.recv(1024)
	#print (msg_rec.decode('utf8'))
	c.close()

def iniciarServidor(host, puerto):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, puerto))
	s.listen(5) #hasta 5 peticiones

	while True:
		# establecer conexión
		(c, addr) = s.accept()
		print("Se estableció conexión con: %s" % str(addr))
		msg = 'Conexión establecida con : %s' % socket.gethostname() + "\r\n"
		c.send(msg.encode('utf8'))
		msg_rec = c.recv(1024)
		#calculo = seleccionarMetodo(msg_rec.decode('ascii'))
		print(msg_rec.decode('ascii'))
		enviarC("10.251.47.225", 7070, msg_rec)
		c.close()
    
if __name__ == "__main__":
    host = ""
    puerto = 44440
    iniciarServidor(host, puerto)