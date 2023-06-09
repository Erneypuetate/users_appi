from fastapi import APIRouter, Response, status
from config.db import conn
from schemas. user import userentity, usersentity
from models.user import User
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user=APIRouter()

@user.get('/users', response_model=list[User], tags=["users"])
def fidn_all_user():
    return usersentity(conn.erney.second_db_in_mongo.find())


   
@user.post('/users', response_model=User, tags=["users"])
def create_user(user:User):
    new_user = dict(user)
    new_user["password"]=sha256_crypt.encrypt(new_user["password"])

    id= conn.erney.second_db_in_mongo.insert_one(new_user).inserted_id

    user=conn.erney.second_db_in_mongo.find_one({"_id":id})

    return userentity(user)



@user.get('/users/{id}', response_model=User, tags=["users"])
def find_user(id:str):
    return userentity(conn.erney.second_db_in_mongo.find_one({"_id":ObjectId(id)}))



@user.put('/users/{id}', response_model=User, tags=["users"])
def update_user(id:str, user:User):
    conn.erney.second_db_in_mongo.find_one_and_update({"_id":ObjectId(id)}, {"$set":dict(user)})
    
    return userentity(conn.erney.second_db_in_mongo.find_one({"_id":ObjectId(id)}))



@user.delete('/users/{id}', status_code=HTTP_204_NO_CONTENT, tags=["users"])
def delate_user(id:str):
    conn.erney.second_db_in_mongo.find_one_and_delete({"_id":ObjectId(id)})
  
    return Response(status_code=HTTP_204_NO_CONTENT)
