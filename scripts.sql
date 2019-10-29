-- https://www.datos.gov.py/dataset


-- Listado de tablas a consultar
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema='public' 
AND table_type='BASE TABLE';


-- Consulta a una tabla (aleatoria) - Ejemplo
SELECT * FROM "8b487581-ce57-4d9f-b559-3252b3e31d54";


