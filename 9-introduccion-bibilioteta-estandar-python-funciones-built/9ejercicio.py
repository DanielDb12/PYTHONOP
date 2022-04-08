'''
Crea un script que le pida al usuario una lista de países (separados por comas). 
Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
 Finalmente,
 muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

'''


lista = set(['Venezuela','Colombia','España','Estados Unidos'])

ordenar = sorted(lista)

print(ordenar)


'''
En este segundo ejercicio, tenéis que crear una aplicación que obtendrá 
los elementos impares de una lista pasada por parámetro con filter y 
realizará una suma de todos estos elementos obtenidos mediante reduce.


from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]


def funcion(x):

    if x % 3 == 0:
        return x


def suma( a,b):
    return a+b


    
resultado = list(filter(funcion,numeros))
print(resultado)

resultado2 = reduce(suma, resultado)
print(resultado2)

'''













