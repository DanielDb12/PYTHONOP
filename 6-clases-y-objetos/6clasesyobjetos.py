#CLASES Y OBJETOS
#CLASE DINAMICA
'''class Dino:
	_luz = True

	def encendido(self):
		self._luz = True

	def apagado(self):
		self._luz = False

	def isEncendido(self):
		return self._luz
#instancia
d = Dino()
d.encendido()
print(d.isEncendido())

#CLASE ESTATICA
class Estatica:
	numero = 1

	def incrementa():
		Estatica.numero+=1

Estatica.incrementa()
print(Estatica.numero)
'''

#HERENCIA


class juguete:

	_endendido = True

	def __init__(self,nombre, x):
		print("constructor juguete(PADRE)", x)

	def encendido(self):
		self._endendido = True

	def apaga(self):
		self._encendido = False

	def isEncendido(self):
		return self._endendido;	

class CaraPapa(juguete):

	def quitarOreja():
		pass

	def ponerOreja():
		pass

class Dino(juguete):
#crear constructor
	'''def __init__(self, nombre):
	 	print("constructor dino")
	   self.color = "Verde"
	    self.nombre = nombre'''
	def __init__(self,nombre):
		super().__init__(nombre)
		print("constructor dino")
	 
	   
	def verEscama(self):
		 pass

#p = CaraPapa()
#p.encendido()
#print(p.isEncendido())

'''d = Dino()
print(dir(d))
'''
##d = Dino('nombre')
#print(d.color)
#print(d.nombre)

#clase abstracta

from abc import ABC, abstractmethod

class Animal(ABC):
	@abstractmethod
	def sonido(self):
		pass


class Perro(Animal):
	"""docstring for Perro"""
	def sonido(self):
		print("guau")

class Gato(Animal):
	"""docstring for Perro"""
	def sonido(self):
		print("miau")
		
	



g = Perro()
g.sonido()

m = Gato()
m.sonido()


##composicion




class Motor:
	tipo = "Diesel"	
class Ventana:
	cantidad = 5

	def cambiarValor(self,valor):
		self.cantidad = valor 


class Rueda:
	rueda = 5
class Carroceria:
	ventana = Ventana()
	ruedad = Rueda()
class Coche:
	motor = Motor()
	carroceria = Carroceria()

q = Coche()
print("Motor es", q.motor.tipo)
q.carroceria.ventana.cambiarValor(2)
print("Ventana", q.carroceria.ventana.cantidad)


class Categorias:
	idcategoria = 20
	nombre = ""

class Proveedor:
	idProveedor = print("juan")
	nombre = 0 

class Productos:
	idproducto = 0
	CategoriaProducto = Categorias() 
	Precio = 0 
	Tamaño = 0 
	TipoDeProducto = 0 
	CIDProveedor = Proveedor()	

p = Productos() 
p.CIDProveedor.idProveedor 
p.CategoriaProducto.idcategoria



