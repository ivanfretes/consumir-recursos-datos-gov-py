-- https://www.datos.gov.py/dataset


-- Listado de tablas a consultar
-- Ejecutar sentencia como GET
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema='public' 
AND table_type='BASE TABLE';


-- Consulta a una tabla (aleatoria) - Ejemplo
-- Este paso ya lo hace el archivo consumir-tablas.py
SELECT * FROM "8b487581-ce57-4d9f-b559-3252b3e31d54";


