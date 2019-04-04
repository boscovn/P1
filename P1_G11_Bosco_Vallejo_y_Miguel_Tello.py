# coding=utf-8
__author__ = 'Bosco_Vallejo-Nágera y Miguel Tello'
from pymongo import MongoClient, errors
import json
from time import sleep
addresses = {}
CLIENT_VARS_PATH = "Vars/client.ini"
PRODUCT_VARS_PATH = "Vars/product.ini"
PROVIDER_VARS_PATH = "Vars/provider.ini"
SALE_VARS_PATH = "Vars/sale.ini"
SLEEP_TIME = 5
ADDRESS_SUBSTRING = "direccion"


def getCityGeoJSON(address):
    """ Devuelve las coordenadas de una direccion a partir de un str de la direccion
    Argumentos:
        address (str) -- Direccion
    Return:
        (str) -- GeoJSON
    """
    if address in addresses:
        return addresses[address]
    else:
        from geopy.geocoders import Nominatim
        geolocator = Nominatim(user_agent="practica-abbdd")
        location = geolocator.geocode(address)
        sleep(SLEEP_TIME)
        geojson = json.dumps({'type': 'Point', 'coordinates': [
                             location.latitude, location.longitude]})
        addresses[address] = geojson
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
        if self.alive:
            try:
                return self.model_class(**self.command_cursor.next())
            except AttributeError as err:
                print(err)
            except StopIteration:
                print("No more documents available in cursor")
        else:
            print("No more documents avaliable in cursor")

    @property
    def alive(self):
        """True si existen más modelos por devolver, False en caso contrario
        """
        return self.command_cursor.alive


class Model:
    db = None
    address_coordinates = []

    def __init__(self, **kwargs):
        required_check = []
        additional_ad = []
        required_check.extend(self.required_vars)
        self._id = None
        for k, v in kwargs.items():
            if ADDRESS_SUBSTRING in k:
                dict = {}
                for addr in v:
                    dict[v][addr] = getCityGeoJSON(addr)
                    # self.address_coordinates.append(getCityGeoJSON(addr))
                setattr(self, k, dict)
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
            raise AttributeError(
                "Not all the required attributes were given, missing {}".format(required_check))
            return
        self.admissible_vars.clear()
        self.admissible_vars.extend(additional_ad)
        if self._id is None:
            self.save()

    def save(self):
        doc = {}
        for v in self.required_vars + self.admissible_vars:
            doc[v] = getattr(self, v)
        try:
            x = db[self.collection].insert_one(doc)
        except errors.DuplicateKeyError as err:
            print(err)
            for k, v in db[self.collection].find_one({'_id': self._id}).items():
                if doc[k] == v:
                    del doc[k]
            self.update(**doc)
        else:
            self._id = x.inserted_id
            self.admissible_vars.append("_id")

    def update(self, **kwargs):
        for k, v in kwargs.items():
            db[self.collection].update_one(
                {'_id': self._id}, {'$set': {k: v}})

    @classmethod
    def query(cls, query):
        cursor = db[cls.collection].aggregate(query)
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
    collection = 'compras'

    def allocate():
        closest_warehouse = {}
        warehouses = []
        """
        ACOPLAMIENTO!!
        """
        for product in self.productos:
            for provider in db.productos.find_one('nombre': product)["proveedores"]:
                for addr in db.productos.find_one('nombre': provider)["direcciones"]:
                    pass


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
nombre_cliente = "Ramon"
Q1 = []
pipeline = [{'$match': {'cliente': nombre_cliente}}]
Q1_cursor = Sale.query(pipeline)
while Q1_cursor.alive:
    instance = Q1_cursor.next()
    if instance is not None:
        Q1.append(instance)
# Q2: Listado de todos los proveedores para un producto
nombre_producto = "tv"
Q2 = []
pipeline = [{'$match': {'nombre': nombre_producto}}]
Q2_cursor = Product.query(pipeline)
while Q2_cursor.alive:
    instance = Q2_cursor.next()
    if instance is not None:
        Q2.extend(instance.proveedores)
Q2 = list(dict.fromkeys(Q2))
# Q3 Listado de todos los productos diferentes comprados por un cliente
nombre_cliente = "Emilia"
Q3 = []
pipeline = [{'$match': {'cliente': nombre_cliente}}]
Q3_cursor = Sale.query(pipeline)
while Q3_cursor.alive:
    instance = Q3_cursor.next()
    if instance is not None:
        Q3.extend(instance.productos)
Q3 = list(dict.fromkeys(Q3))

if __name__ == '__main__':
    for k in Q1:
        print("{} {}".format(k._id, k.precio_de_compra))
    print(Q2)
    print(Q3)
