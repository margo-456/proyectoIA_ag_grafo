import math

class Vertice:
	"""Clase que define los vértices de los gráficas"""
	def __init__(self, i):
		"""Método que inicializa el vértice con sus atributos
		id = identificador
		vecinos = lista de los vértices con los que está conectado por una arista
		visitado = para saber si fue visitado o no
		padre = vértice visitado un paso antes
		costo = valor que tiene recorrerlo"""
		self.id = i
		self.vecinos = []
		self.visitado = False
		self.padre = None
		#atributo costo o distancia inicializado con infinito,cuando creamos un vertice tiene el atribto distancia con inf

		self.costo = float('inf')

	def agregarVecino(self, v, p):
		"""Método que agrega los vertices que se encuentre conectados por una arista a la lista de vecinos 
		de un vertice, revisando si éste aún no se encuentra en la lista de vecinos"""
		if v not in self.vecinos:
			# recibe los valores del vertice vecino y el peso
			#almacena lista de vecino indice 0 contiene la lista de vecinos y en el indice 1 contiene el peso.
			self.vecinos.append([v, p])

class Grafica:
	"""Clase que define los vértices de las gráficas"""
	def __init__(self):
		"""vertices = diccionario con los vertices de la grafica"""
		self.vertices = {}

	def agregarVertice(self, id):
		"""Método que agrega vértices, recibiendo el índice y revisando si éste no existe en el diccionario
		de vértices"""
		if id not in self.vertices:
			self.vertices[id] = Vertice(id)

	def agregarArista(self, a, b, p):# a y b vertices que conforman una arista y p el peso
		"""Método que agrega aristas, recibiendo el índice de dos vertices y revisando si existen estos en la lista
		de vertices, además de recibir el peso de la arista , el cual se asigna a ambos vértices por medio del método
		agregar vecino"""
		if a in self.vertices and b in self.vertices:
			self.vertices[a].agregarVecino(b, p)
			self.vertices[b].agregarVecino(a, p)

	def imprimirGrafica(self):
		"""Método que imprime el gráfo completo arista por arista con todas sus características(incluye heurística)"""
		for v in self.vertices:
			print("El costo del vértice "+str(self.vertices[v].id)+" es "+ str(self.vertices[v].costo)+" llegando desde "+str(self.vertices[v].padre))
			
	
	def camino(self, a, b):
		"""Método que va guardando en la lista llamada 'camino' los nodos en el orden que sean visitados y actualizando dicha
		lista con los vértices con el menor costo"""
		camino = []
		actual = b
		while actual != None:
			camino.insert(0, actual)#actualizar la lista con los vertices de menor costo
			actual = self.vertices[actual].padre
		return [camino, self.vertices[b].costo]

	def minimo(self, l):
		"""Método que recibe la lista de los vertices no visitados, revisa si su longitud es mayor a cero(indica que 
		aún hay vértices sin visitar), y realiza comparaciones de los costos de cada vértice en ésta lista para encontrar
		el de menor costo"""
		if len(l) > 0:# si la lista es mayor acero contiene elemetos
			m = self.vertices[l[0]].costo # tomamos la distancia del elemto de la posicion cero,primer vertice
			v = l[0] #variable v nodo posicion cero 
			for e in l: 
				if m > self.vertices[e].costo: #si la distancia de un elemento de la lista es menor a m
					m = self.vertices[e].costo #actualiza m con el menor vlor
					v = e # actualiza v con el vertice que tiene menor distancia
			return v # retornamos el nodo v
		return None
     # esta en la clase grafica para ser llamado como un objeto mas
	def recorrido(self, a): #recibe  a es el vertice donde inicia el recorrido
		"""Método que sigue el algortimo 
		1. Asignar a cada nodo una distancia tentativa: 0 para el nodo inicial e infinito para todos los nodos restantes. Predecesor nulo para todos.
		2. Establecer al nodo inicial como nodo actual y crear un conjunto de nodos no visitados.
		3. Para el nodo actual, considerar a todos sus vecinos no visitados con peso w.
			a) Si la distancia del nodo actual sumada al peso w es menor que la distancia tentativa actual de ese vecino,
			sobreescribir la distancia con la suma obtenida y guardar al nodo actual como predecesor del vecino
		4. Cuando se termina de revisar a todos los vecino del nodo actual, se marca como visitado y se elimina del conjunto no  visitado
		5. Continúa la ejecución hasta vaciar al conjunto no visitado
		6. Seleccionar el nodo no visitado con menor distancia tentativa y marcarlo como el nuevo nodo actual. Regresar al punto 3
		"""

		if a in self.vertices:#verificar el nodo a se encuentre en el conjunto de vertices de la grafica
			# 1 y 2
			self.vertices[a].costo = 0 #establecer la distancia del nodo inicial como cero
			actual = a      #actual es el nodo a
			noVisitados = []  #lista vacia de nodos no visitados
			
		
			for v in self.vertices: 
				if v != a: # si no encuentra a establece distancia como inf
					self.vertices[v].costo = float('inf')#se estable las distancia inf
				self.vertices[v].padre = None #los predecesores como none
				noVisitados.append(v) # agregar al conjunto no visitados los vertives  v

			while len(noVisitados) > 0: #mientras no visitados tenga elementos 
				#3
				for vec in self.vertices[actual].vecinos: # recorremos a cada vecino de actual
					if self.vertices[vec[0]].visitado == False: #obtener el id del vecino y verificar si es visitado
						# 3.a
						if self.vertices[actual].costo + vec[1] < self.vertices[vec[0]].costo:# si se cumple que la distancia del vertice actual + la suma de la arista con el vecino es menor a la distancia que tiene el vecino almacenado en el momento intercambia 
							self.vertices[vec[0]].costo = self.vertices[actual].costo + vec[1] 
							self.vertices[vec[0]].padre = actual

				# 4
				self.vertices[actual].visitado = True  #nodo actual marca como visitaso 
				noVisitados.remove(actual) #eliminamos del conjunto de vertices no visitados

				# 5 y 6
				actual = self.minimo(noVisitados) #actualizamos la variable actual enviando el conjunto de no visitados
		else:
			return False

	#metodo main del programa

class main:
	g = Grafica()# objeto de tipo grafica g
	#agregamos los vertices 
	g.agregarVertice(1)
	g.agregarVertice(2)
	g.agregarVertice(3)
	g.agregarVertice(4)
	g.agregarVertice(5)
	g.agregarVertice(6)
	g.agregarVertice(7)
	g.agregarVertice(8)
	g.agregarVertice(9)
	g.agregarVertice(10)
	g.agregarVertice(11)
	g.agregarVertice(12)
	g.agregarVertice(13)
	g.agregarVertice(14)
	#agregamos los vertices que conforma una arista y su peso
	g.agregarArista(1, 6, 14)
	g.agregarArista(14, 10, 1)
	g.agregarArista(1, 2, 7)
	g.agregarArista(1, 3, 9)
	g.agregarArista(7, 13, 4)
	g.agregarArista(2, 4, 15)
	g.agregarArista(3, 4, 11)
	g.agregarArista(3, 6, 2)
	g.agregarArista(4, 5, 6)
	g.agregarArista(5, 8, 2)
	g.agregarArista(7, 6, 1)
	g.agregarArista(8, 3, 9)
	g.agregarArista(8, 7, 3)
	g.agregarArista(5, 9, 9)
	g.agregarArista(9, 6, 3)
	g.agregarArista(11,9, 3)
	g.agregarArista(11,10,9)
	g.agregarArista(10,12,2)
	g.agregarArista(13,14,1)
	g.agregarArista(12, 13,1)
   

	print("\n\nLa ruta más rápida  junto con su costo es:")
	#llamado a las funcion recorrido con indice 1 para iniciar el recorrido
	g.recorrido(1)
	# imprime el camino q hay de el nodo 1 al 13
	print(g.camino(1, 13))
	print("\nLos valores finales de la gráfica son los siguietes:")
	g.imprimirGrafica()