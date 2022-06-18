import ProgramaAgente as Agente
import unittest

class Test(unittest.TestCase):
    
    def testCostoVeredas(self):

        """ 
        Se crea un Agente al cual se le pasa un arreglo para el estado, conformado por un arreglo de arreglos,

        Para el uso de los métodos del agente se recurre a usar los métodos del agente creado
        Se ingresan valores estáticos como el inicio del arreglo '0' , la posición del agente '4' y el arreglo delas veredas sucias,
        en donde se escoge el valor de laposición cero de 'veredaSucia'

        Luego se obtiene le costo por redirección y por acciones de frenado y limpieza del agente,
        al finalizar se verifica que el costo sea igual a 15.

        """
        test1 = Agente
        # arreglo que contiene el estado limpio o sucio  junto con cada vereda, valores estaticos
        estado={'0': ['1', 1], '1': ['0', 2], '2': ['0', 3], '3': ['0', 4], '4': ['1', 5], '5': ['1', 6], '6': ['1', 7]}
        veredaSucias=test1.identificarveredasAlimpiar(estado)
        costo, posicion=test1.redirigirAlprimero(5, 5, int(veredaSucias[0]))
        costo=test1.limpiezaVereda(veredaSucias, 5, estado, costo)
        #verificacion del costo e total 15
        self.assertEqual(costo,15)

if __name__ == '__main__':
    unittest.main()