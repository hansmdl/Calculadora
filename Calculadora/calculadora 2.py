import string

#FUNCIOONES

def asuntosuma():
    operador = a.strip()[pop1]
    valor1 = a.strip()[0:pop1]
    valor2 = a.strip()[pop1 + 1:len(a)]
    resultado = int(valor1) + int(valor2)
    print('la suma de',valor1,'+',valor2, '=', resultado)
def asuntoresta():
    operador = a.strip()[pop2]
    valor1 = a.strip()[0:pop2]
    valor2 = a.strip()[pop2 + 1:len(a)]
    resultado = int(valor1) - int(valor2)
    print('la resta de',valor1,'-',valor2, '=', resultado)
def asuntomult():
    operador = a.strip()[pop3]
    valor1 = a.strip()[0:pop3]
    valor2 = a.strip()[pop3 + 1:len(a)]
    resultado = int(valor1) * int(valor2)
    print('la multiplicacion de',valor1,'X',valor2, '=', resultado)
def asuntodiv():
    operador = a.strip()[pop4]
    valor1 = a.strip()[0:pop4]
    valor2 = a.strip()[pop4 + 1:len(a)]
    resultado = int(valor1) / int(valor2)
    print('la division de',valor1,'/',valor2, '=', resultado)

#seleccion de operaciones

a = input(' inserte la operacion a realizar: ')
pop1 = a.find('+')
if pop1 > 0:
    try:
        asuntosuma()
    except:
        print('mete la vaina bien')
pop2 = a.find('-')
if pop2 > 0:
    try:
        asuntoresta()
    except:
        print('mete la vaina bien')

pop3 = a.find('*')
if pop3 > 0:
    try:
        asuntomult()
    except:
        print('mete la vaina bien')
pop4 = a.find('/')
if pop4 > 0:
    try:
        asuntodiv()
    except:
        print('mete la vaina bien')




