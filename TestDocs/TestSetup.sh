#!/bin/bash
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
mongoimport --db data --collection compras --drop --file compras.json
mongoimport --db data --collection productos --drop --file productos.json
mongoimport --db data --collection proveedores --drop --file proveedores.json
mongoimport --db data --collection clientes --drop --file clientes.json
