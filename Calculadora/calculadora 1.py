#FUNCIOONES

def asuntosuma():
    operador = a.strip()[pop]
    valor1 = a.strip()[0:pop]
    valor2 = a.strip()[pop + 1:len(a)]
    resultado = int(valor1) + int(valor2)
    print('la suma de',valor1,'+',valor2, '=', resultado)
def asuntoresta():
    operador = a.strip()[pop]
    valor1 = a.strip()[0:pop]
    valor2 = a.strip()[pop + 1:len(a)]
    resultado = int(valor1) - int(valor2)
    print('la resta de',valor1,'-',valor2, '=', resultado)
def asuntomult():
    operador = a.strip()[pop]
    valor1 = a.strip()[0:pop]
    valor2 = a.strip()[pop + 1:len(a)]
    resultado = int(valor1) * int(valor2)
    print('la multiplicacion de',valor1,'X',valor2, '=', resultado)
def asuntodiv():
    operador = a.strip()[pop]
    valor1 = a.strip()[0:pop]
    valor2 = a.strip()[pop + 1:len(a)]
    resultado = int(valor1) / int(valor2)
    print('la division de',valor1,'/',valor2, '=', resultado)

#inicio de interaccion con teclado
a= input('ingresa una operacion matematica: ')

#operaciones que realiza la calculadora
operadores = ['+','-','*','/']

#Ciclo para seleccion de operacion
for i in operadores:
    if i in a:
        pop = a.find(i)
        pop2 = a.rfind(i)
        if pop != pop2 and i == '*' or i == '/':
            print('Si es multiplicacion o division solo se permite un solo signo')
            break
        elif i == '+':
            asuntosuma()
        elif i =='-':
            asuntoresta()
        elif i == '*':
            asuntomult()
        elif i == '/':
            asuntodiv()
        break