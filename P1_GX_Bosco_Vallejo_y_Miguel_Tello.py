__author__ = 'Bosco_Vallejo-Nágera y Miguel Tello'
adresses = {}
from pymongo import MongoClient
import json
from time import sleep
def getCityGeoJSON(adress):
    """ Devuelve las coordenadas de una direcciion a partir de un str de la direccion
    Argumentos:
        adress (str) -- Direccion
    Return:
        (str) -- GeoJSON
    """
    if adress in adresses:
        return adresses[adress]
    else:
        from geopy.geocoders import Nominatim
        geolocator = Nominatim(user_agent="practica-abbdd")
        location = geolocator.geocode(adress)
        sleep(5)
        geojson = json.dumps({'type': 'Point', 'coordinates' : [location.latitude, location.longitude]})
        adresses[adress] = geojson
        return geojson

class ModelCursor(object):
    """ Cursor para iterar sobre los documentos del resultado de una
    consulta. Los documentos deben ser devueltos en forma de objetos
    modelo.
    """

    def __init__(self, model_class, command_cursor):
        """ Inicializa ModelCursor
        Argumentos:
            model_class (class) -- Clase para crear los modelos del
            documento que se itera.
            command_cursor (CommandCursor) -- Cursor de pymongo
        """
        self.model_class = model_class
        self.command_cursor = command_cursor
        #TODO
        #pass #No olvidar eliminar esta linea una vez implementado

    def next(self):
        """ Devuelve el siguiente documento en forma de modelo
        """
        #TODO
        pass #No olvidar eliminar esta linea una vez implementado

    @property
    def alive(self):
        """True si existen más modelos por devolver, False en caso contrario
        """
        #TODO
        pass #No olvidar eliminar esta linea una vez implementado

class Model(object):
    """ Prototipo de la clase modelo
        Copiar y pegar tantas veces como modelos se deseen crear (cambiando
        el nombre Model, por la entidad correspondiente), o bien crear tantas
        clases como modelos se deseen que hereden de esta clase. Este segundo
        metodo puede resultar mas compleja
    """
    required_vars = []
    admissible_vars = []
    db = None

    def __init__(self, **kwargs):
        for k, v in kwargs:
            if k not in required_vars:
                if k not in admissible_vars:
                    print ("No admitida")
                    #TODO excepcion
                else:
                    self.k = v
            else:
                required_vars.remove(k)
                self.k = v
        if required_vars:
            print ("No tiene lo necesario")
            #TODO excepcion
        #TODO
        pass #No olvidar eliminar esta linea una vez implementado


    def save(self):
        #TODO
        pass #No olvidar eliminar esta linea una vez implementado

    def update(self, **kwargs):
        #TODO
        pass #No olvidar eliminar esta linea una vez implementado

    @classmethod
    def query(cls, query):
        """ Devuelve un cursor de modelos
        """
        cls()
        #TODO
        # cls() es el constructor de esta clase
        pass #No olvidar eliminar esta linea una vez implementado

    @classmethod
    def init_class(cls, db, vars_path="model_name.vars"):
        """ Inicializa las variables de clase en la inicializacion del sistema.
        Argumentos:
            db (MongoClient) -- Conexion a la base de datos.
            vars_path (str) -- ruta al archivo con la definicion de variables
            del modelo.
        """
        #TODO
        # cls() es el constructor de esta clase
        pass #No olvidar eliminar esta linea una vez implementado



# Q1: Listado de todas las compras de un cliente
nombre_cliente = "Definir"
Q1 = []

# Q2: etc...

if __name__ == '__main__':
    print ()
