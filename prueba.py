from pymongo import MongoClient

# Establecer la conexión con el servidor MongoDB
conn = MongoClient("mongodb://root:example@localhost:27017/")

# Seleccionar la base de datos


# Datos a insertar
data = {
    "id": "1",
    "name": "erney",
    "email": "sdf",
    "password": "jdhd"
}

# Insertar un documento en la colección
conn.erney.second_db_in_mongo.insert_one(data)

print("Documento insertado correctamente.")
