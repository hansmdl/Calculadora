#verificar si un numero es positivo, negativo o neutro.

p = input('Su numero es un decimal? ')
if p == ('Y'):
    a = float(input('Digite el numero que desea revisar:'))
    if a == 0:
        print(a,' Es un numero decimal neutro')
    elif a < 0:
        print(a,' Es un numero decimal negativo')
    elif a > 0:
        print(a,' Es un numero decimal positivo')
else:
    b = int(input('Digite el numero que desea revisar:'))
    if b == 0:
        print(b,' Es un numero natural neutro')
    elif b < 0:
        print(b,' Es un numero natural negativo')
    elif b > 0:
        print(b,' Es un numero natural positivo')