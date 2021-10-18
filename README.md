# Código desarrollado por _David Esteban Fajardo Torres_

Correo: destebanft@protonmail.com

Tel: +57 320 251 1039

Para el problema propuesto, plantee el siguiente modelo de datos:


Mediante docker compose se ejecuta postgres, django y un proxy(nginx), lo configure para que todas las peticiones y conexiones se hagan mediante el proxy. Con el sofware _Postman_ probé los endpoints.

Cree 5 endpoints:

- http://localhost:8100/api/owners/ obtener los propietarios (GET)
- http://localhost:8100/api/owners/ crear propietarios (POST)
- http://localhost:8100/api/properties/ obtener las propietades (GET)
- http://localhost:8100/api/properties/?real_estate_number=8&type=0&cadastral_id=123&address=calle&name_owner=David filtrar las propiedades (GET)
- http://localhost:8100/api/properties/assign_owners asignar propietarios a las propiedades (POST)

Pasos ara ejecutar el proyecto:

1. Agregue el archivo .env dentro del directorio api (a la altura del manage.py). Este archivo esta en el correo.
2. Instale la extención de docker en VsCode y luego de en la opción de abrir en contenedor. Esto le va solicitar un archivo para ejecutar el contenedor, seleccione _docker-compose.override.yml_. Este proceso puede tardar un poco.
3. Luego de que se ejecute el docker compose _docker-compose.override.yml_. Se abrira una terminal (_django@a0cc19f5f07b:/workspace$_). En ese momento vaya a su navegador, ingrese a la dirección http://localhost:8181 (dirección de pgAdmin), ingrese con el correo admin@gmail.com y la contraseña admin.
4. Cree un server con el nombre local_db, en la conexión use la siguiente configiración (password:postgres)
5En archivo quick.postman_collection.json están las peticiones para hacer pruebas en el api mediante el software postman. Enviado al correo.