## Consumir todos datos.gov.py

- **`scripts.sql`**: Es un archivo de recuperacion de listado de tablas del portal datos.gov.py, y lo almacena en utils/listado-de-tablas.json

- **`datasets`**: Carpeta con JSONs recuperados de cada endpoint 

- **`utils`**: Carpeta con el script para consumir las tablas y generar los archivos JSON


## Consumir y generar datasets

```sh
$ cd ./utils

$ python3 ./consumir-tablas.py 
```


## Actualizar el listado endpoint
1. Consultar 
	https://www.datos.gov.py/api/action/datastore_search_sql?sql=SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE';

2. Actualizar `utils/listado-de-tablas.json `


### Requisito

- [**Python3.x**](https://www.python.org/downloads/)


