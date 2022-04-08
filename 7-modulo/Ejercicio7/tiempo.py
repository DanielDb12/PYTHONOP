'''
En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. 
Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.


En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario,haréis una operación para 
calcular el tiempo que queda de trabajo.


'''

from time import strftime, localtime, gmtime, strptime, asctime,struct_time

import pprint



horaInt = localtime()
horaString = strftime("%-I:%M:%S %p ")

print(horaString)





if horaString >= "7:00:00 PM":


	h = horaInt[3]
	
	if h <= 19:
		print("queda por culminar",(h - 19) * -1,"horas")

	else:
		print("culmino la hora de trabajo")

	
		
				
	