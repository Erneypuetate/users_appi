from typing import Optional
from pydantic import BaseModel
from passlib.hash import sha256_crypt

class User(BaseModel):
    id:Optional[str]
    name:str
    email:str
    password:str

def verificar_contrasena(contrasena_usuario, contrasena_encriptada):
    try:
        return sha256_crypt.verify(contrasena_usuario, contrasena_encriptada)
    except Exception as e:
        print("Error al verificar la contraseña:", e)
        return False
