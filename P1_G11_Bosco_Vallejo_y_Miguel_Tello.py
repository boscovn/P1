__author__ = 'Bosco_Vallejo-Nágera y Miguel Tello'
from pymongo import MongoClient
import json
from time import sleep
adresses = {}

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
        El resto de clases modelo heredan de esta
    """
    required_vars = []
    admissible_vars = []
    db = None

    def __init__(self, **kwargs):
        required_check = []
        required_check.expand(self.required_vars)
        for k, v in kwargs.items():
            if k not in self.required_vars:
                if k not in self.admissible_vars:
                    print ("Variable {} no admitida".format(k))
                else:
                    setattr(self, k, v)
            else:
                required_check.remove(k)
                setattr(self, k, v)
        if required_check:
            print ("No tiene lo necesario, faltan variables: ")
            print (required_check)
            #TODO excepcion

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
    def init_class(cls, db, vars_path):
        """ Inicializa las variables de clase en la inicializacion del sistema.
        Argumentos:
            db (MongoClient) -- Conexion a la base de datos.
            vars_path (str) -- ruta al archivo con la definicion de variables
            del modelo.
        """
        self.db = db
        vars_path
        #TODO
        # cls() es el constructor de esta clase
        pass #No olvidar eliminar esta linea una vez implementado


class Client(Model):
    """Clase cliente, hereda de Model"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Product(Model):
    """Clase producto, hereda de Model"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Sale(Model):
    """Clase venta, hereda de Model"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def allocate():
        pass


class Provider(Model):
    """Clase proveedor, hereda de Model"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# Q1: Listado de todas las compras de un cliente
nombre_cliente = "Definir"
Q1 = []

# Q2: etc...

if __name__ == '__main__':
    #cliente = Client(n="2", i="0")
    client = MongoClient()
    db = client.data
    proveedores = db.proveedores
    p = Provider(**proveedores.find_one())
    print (p.direcciones_almacenes)
#mongoimport --db data --collection clientes --drop --file ~/Downloads/clientes(1).json
