__author__ = 'Bosco_Vallejo-Nágera y Miguel Tello'
from pymongo import MongoClient
import json
from time import sleep
adresses = {}
necvars_client = []
advars_client = []
necvars_product = []
advars_product = []
necvars_sale = []
advars_sale = []
necvars_provider = []
advars_provider = []
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
        for k, v in kwargs.items():
            if k not in self.required_vars:
                if k not in self.admissible_vars:
                    print ("Variable {} no admitida".format(k))
                else:
                    self.k = v
            else:
                self.required_vars.remove(k)
                self.k = v
        if self.required_vars:
            print ("No tiene lo necesario")
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
    def init_class(cls, db, vars_path="model_name.vars"):
        """ Inicializa las variables de clase en la inicializacion del sistema.
        Argumentos:
            db (MongoClient) -- Conexion a la base de datos.
            vars_path (str) -- ruta al archivo con la definicion de variables
            del modelo.
        """
        self.db = db
        #TODO
        # cls() es el constructor de esta clase
        pass #No olvidar eliminar esta linea una vez implementado


class Client(Model):
    """Clase cliente, hereda de Model"""
    def __init__(self, **kwargs):
        super().required_vars.extend(necvars_client)
        super().admissible_vars.extend(advars_client)
        super().__init__(**kwargs)


class Product(Model):
    """Clase producto, hereda de Model"""
    def __init__(self, **kwargs):
        super().required_vars.extend(necvars_product)
        super().admissible_vars.extend(advars_product)
        super().__init__(**kwargs)


class Sale(Model):
    """Clase venta, hereda de Model"""
    def __init__(self, **kwargs):
        super().required_vars.extend(necvars_sale)
        super().admissible_vars.extend(advars_sale)
        super().__init__(**kwargs)

    def allocate():
        pass


class Provider(Model):
    """Clase proveedor, hereda de Model"""
    def __init__(self, **kwargs):
        super().required_vars.extend(necvars_provider)
        super().admissible_vars.extend(advars_provider)
        super().__init__(**kwargs)


# Q1: Listado de todas las compras de un cliente
nombre_cliente = "Definir"
Q1 = []

# Q2: etc...

if __name__ == '__main__':
    cliente = Client(n="2", i="0")
