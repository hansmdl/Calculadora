lista=[4,1,4,2,3]
suma=0
cuenta =0
for elemento in lista:
    cuenta = cuenta+1
    suma = suma + elemento
print(suma/cuenta)

print(sum(lista)/len(lista))