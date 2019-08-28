import Pyro4

uri = input("Cargar URL: ").strip()
valor1 = int(input("Introducir valor 1: "))
valor2 = int(input("Introducir valor 2: "))
operación = input("Que operación desea realizar? 1.Sumar 2.Multiplicar ").strip()
greeting_maker = Pyro4.Proxy(uri)

if operación == '1':
    print("Resultado: {}".format(greeting_maker.get_Sumar(valor1,valor2)))
if operación == '2':
    print("Resultado: {}".format(greeting_maker.get_Multiplicar(valor1,valor2))) 
else:
    print("Opción Invalida")