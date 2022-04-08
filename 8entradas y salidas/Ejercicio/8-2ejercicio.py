'''
En este segundo ejercicio, tendréis que crear un archivo py
 y dentro crearéis una clase Vehículo, haréis un objeto de ella, 
 lo guardaréis en un archivo y luego lo cargamos.

'''
import pickle


class Vehiculo:

	marca = ""
	precio = 0.0

	def __init__(self,marca,precio):
		self.marca = marca
		self.precio = precio

	def getNombre(self):
		return self.marca

'''
c1 = Vehiculo("Mercedes", 20.5)
f = open('datos.bin','wb')
pickle.dump(c1,f)
f.close()
'''

f = open('datos.bin','rb')
mercedes = pickle.load(f)
f.close()
print(mercedes.getNombre(), "precio ", mercedes.precio )
