# coding=utf-8
__author__ = 'Bosco_Vallejo-Nágera y Miguel Tello'
from pymongo import MongoClient, errors
import json
from time import sleep
adresses = {}
CLIENT_VARS_PATH = "Vars/client.ini"
PRODUCT_VARS_PATH = "Vars/product.ini"
PROVIDER_VARS_PATH = "Vars/provider.ini"
SALE_VARS_PATH = "Vars/sale.ini"
SLEEP_TIME = 5


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
        sleep(SLEEP_TIME)
        geojson = json.dumps({'type': 'Point', 'coordinates': [
                             location.latitude, location.longitude]})
        adresses[adress] = geojson
        return geojson


class ModelCursor:
    """ Cursor para iterar sobre los documentos del resultado de una
    consulta. Los documentos deben ser devueltos en forma de objetos
    modelo.
    """

    def __init__(self, model_class, command_cursor):
        self.model_class = model_class
        self.command_cursor = command_cursor

    def next(self):
        """ Devuelve el siguiente documento en forma de modelo
        """
        try:
            return self.model_class(**self.command_cursor.next())
        except ValueError as err:
            print(err)

    @property
    def alive(self):
        """True si existen más modelos por devolver, False en caso contrario
        """
        return self.command_cursor.alive


class Model:
    db = None

    def __init__(self, **kwargs):
        required_check = []
        additional_ad = []
        required_check.extend(self.required_vars)
        for k, v in kwargs.items():
            if k not in self.required_vars:
                if k not in self.admissible_vars:
                    print("Variable {} not admitted for the {} class".format(
                        k, type(self).__name__))
                else:
                    additional_ad.append(k)
                    setattr(self, k, v)
            else:
                required_check.remove(k)
                setattr(self, k, v)
        if required_check:
            raise ValueError(
                "Not all the required attributes were given, missing {}".format(required_check))
            return
        self.admissible_vars.clear()
        self.admissible_vars.extend(additional_ad)

    def save(self):
        #check_existing = db[self.collection].find_one({'_id':self._id})
        # if check_existing.retrieved() > 0:
        #    self.update(**check_existing)
        # else:
        doc = {}
        for v in self.required_vars + self.admissible_vars:
            doc[v] = getattr(self, v)
        try:
            db[self.collection].insert_one(doc)
        except errors.DuplicateKeyError as err:
            print(err)
            """for k, v in **db[self.collection].find_one({'_id': self._id}):
                if doc[k] == v:
                    del doc[k]
            self.update(**doc)"""

    def update(self, **kwargs):
        for k, v in kwargs:
            db[collection].update_one(
                {'_id': self._id}, {'$set': {k: getattr(self, k)}})

    @classmethod
    def query(cls, query):
        """ Devuelve un cursor de modelos
        """
        cursor = db[self.collection].find(query)
        return ModelCursor(cls, cursor)

    @classmethod
    def init_class(cls, db, vars_path):
        cls.db = db
        import configparser
        config = configparser.ConfigParser(allow_no_value=True)
        config.read(vars_path)
        cls.required_vars.extend(config['Required Variables'])
        cls.admissible_vars.extend(config['Admitted Variables'])


class Client(Model):
    required_vars = []
    admissible_vars = []
    collection = 'clientes'


class Product(Model):
    required_vars = []
    admissible_vars = []
    collection = 'productos'


class Sale(Model):
    required_vars = []
    admissible_vars = []
    collection = 'ventas'

    def allocate():
        pass  # TODO


class Provider(Model):
    required_vars = []
    admissible_vars = []
    collection = 'proveedores'


client = MongoClient()
db = client.data
Provider.init_class(db, PROVIDER_VARS_PATH)
Client.init_class(db, CLIENT_VARS_PATH)
Sale.init_class(db, SALE_VARS_PATH)
Product.init_class(db, PRODUCT_VARS_PATH)

# Q1: Listado de todas las compras de un cliente
nombre_cliente = "Definir"
Q1 = []
# Q2: etc...

if __name__ == '__main__':
    pu = 'proveedores'
    proveedores = db[pu]
    n = ModelCursor(Provider, proveedores.find())
    p = n.next()
    print(p)
    for k in db[pu].find_one():
        print("{}".format(k))
    try:
        m = Provider(_id=1, nombre="dos", direcciones=["Madrid", "Salamanca"])
    except ValueError as err:
        print(err)
    else:
        m.save()
    #print (p.direcciones)
