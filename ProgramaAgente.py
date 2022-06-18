


def identificarveredasAlimpiar(estado):
    """
    Comprende cuales son las veredas que se deben limpiar

    Selecciona las veredas sucias "1" y las agrega a un array
    """
    arrayVeredaSucias=[]
    for k, v in estado.items():
        #seleciona las veredas y las agrega al array
        if(v[0]=='1'):# veredas sucias con valor de 1
            arrayVeredaSucias.append(v[1])
        #retorna el array de veredas sucias
    return arrayVeredaSucias

def redirigirAlprimero(costo, posicion, menor):
    """
    Redirecciona a la primera posición del arreglo

    Al no estar en la primera posición del entorno redirige al agente
    a la primera posición y suma uno de costo por el movimiento realizado
    """
    if(posicion==menor):#posicion cero del arreglo
        pass
    else:
        print()
        #imprime el mensaje de verificacion si ya esta en la posicion menor
        for i in range(posicion,menor,-1):
            print('redirigiendo un puesto de vereda '+str(posicion)+' a posicion '+str(i-1))
            #suma al costo uno por la accion realizada
            costo+=1
        posicion=menor
        #retorna el costo y la posicion
    return costo, posicion

def contievereda(numero, veredaAlimpiar, estado):
    """
   Este es el docstring de la funcion contiene veredas
   Parametros: numero, veredaAlimpiar, estado
   Retornos : False
    """

    # Verifica si la vereda está conenida en el array de las veredas sucias
  
    keys = list(estado.keys())
    for x in veredaAlimpiar:
          # Recorre las veredas para ser limpiadas
        if(numero==x):
            print('Limpiando la vereda: '+keys[x-1])
            return True
    return False

def limpiezaVereda(veredasAlimpiar, posicion_maquina, estado,costo):
    """
    Limpia las veredas y recorre el arreglo

    En el caso de estar la vereda registrada como sucia, se procede a realizar la
    limpieza de la vereda, es decir cambiar el estado de sucia a limpia 

    Para las acciones de parar y limpiar se hace una suma de 2 al costo por las dos acciones,
    cuando solo pasa por una vereda limpia solo suma 1
    """
    for i in range(posicion_maquina ,veredasAlimpiar[len(veredasAlimpiar)-1]+1,+1):
        print(i)
        #if que identifica si la vereda esta sucia, procede a limpiar
        if(contievereda(i, veredasAlimpiar, estado)):
            #suma al costo 2 por la accion de limpiar 
            costo+=2
            print('Para y limpia')
        else:
            #suma al costo uno y solo sigue si la vereda esta limpia
            costo+=1
            print('Sigue')
    print('Todo se ha limpiado')
    return costo


#guardara la información de las veredas
estado={}
#ayudará a darle una posición de orden a los estados
valor=1
#nos ayudará a saber el costo de limpiar 
costo=0
#para guardar la posicion de la vereda
localizacion = 0
#permite determinar cuando se han recorrido todas las veredas
numeroVeredasSuma=1
numeroVeredas=input(print("Indique el número de veredas a limpiar:  ")).upper()
while(numeroVeredasSuma<=int(numeroVeredas)):
    """
    Se recorre el número de veredas ingresadas por el usuario.

    Para los estados se envía un valor de tipo string al arreglo de estado, el que corresponde a la localización,
    el estado en string y el valor por la posición de la vereda.
    
    Entrega el arreglo estado en el siguiente formato: {'0': ['1', i]}
    """
    estadoLimpieza = input("Ingrese el estado de la vereda "+ str(localizacion) +": ")
    estado[str(localizacion)] = [estadoLimpieza,valor]
    localizacion +=1
    valor+=1
    numeroVeredasSuma+=1
posicion = input("Digite la vereda en que se encuentra la máquina: ")
# Veredas que se deben limpiar
veredasSucias=identificarveredasAlimpiar(estado)
# Redirige al agente a la primera posición, pasa los valores costo por redirigir a la posicion cero. 
costo, posicion=redirigirAlprimero(int(costo), int(posicion)+1, int(veredasSucias[0]))
# El agente realiza la limpieza de las veredas y pasa el costo por limpiar 
costo=limpiezaVereda(veredasSucias, posicion, estado, costo)
# Se imprime el costo final del agente
print('El costo es de: '+str(costo))

