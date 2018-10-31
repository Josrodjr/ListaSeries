# ListaSeries - BACKEND

### pasar los requirements a un nuevo env
```
pip install -r requirements.txt
```

### correr server localhost
```
python manage.py runserver
```

### request JWT ejemplo desde shell

```
curl -X POST -d "username=admin&password=password123" http://localhost:8000/api-token-auth/
```

### POSTMAN pruebas
 importar la coleccion de acciones de postman /series_api.postman_collection
 ejemplo de request JWT 
 ejemplo de postman
 ejemplo de get
 