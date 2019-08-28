import Pyro4

valor1 = int(input("Introducir valor 1: "))
valor2 = int(input("Introducir valor 2: "))

operacion = int(input("Cual calculo desea realizar: 1- Suma, 2- Multiplicacion: "))
	
#calculo_maker = Pyro4.Proxy("PYRONAME:actividad5.calculo@192.168.0.105:33330")    # use name server object lookup uri shortcut

calculo_maker = Pyro4.core.Proxy('PYRO:actividad5.calculo@10.251.46.94:9090')

if operacion == 1:
	print(calculo_maker.calcularSuma(valor1, valor2))

if operacion == 2:
	print(calculo_maker.calcularMultiplicacion(valor1, valor2))

#print(calculo_maker)