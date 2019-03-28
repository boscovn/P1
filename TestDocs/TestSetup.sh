#!/bin/bash
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
ls
mongoimport --db test --collection compras --drop --file compras.json
mongoimport --db test --collection productos --drop --file productos.json
mongoimport --db test --collection proveedores --drop --file proveedores.json
mongoimport --db test --collection clientes --drop --file clientes.json
