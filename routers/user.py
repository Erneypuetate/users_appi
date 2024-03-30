from fastapi import APIRouter, Response, status, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from config.db import conn
from schemas.user import userentity, usersentity
from models.user import User, verificar_contrasena
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user=APIRouter()

templates = Jinja2Templates(directory="templates")


@user.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@user.post("/login")#, response_class=RedirectResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    
   
    
    usuarios = conn.erney.second_db_in_mongo.find({"name": username})
    for user in usuarios:
        
        if verificar_contrasena(password, user["password"]):

            return RedirectResponse(url="/inicio") 
        
    return templates.TemplateResponse("login_fail.html", {"request": request})


    

@user.post("/inicio", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("inicio.html", {"request": request})


@user.get("/register", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("create_user.html", {"request": request})


@user.post('/register', response_class=HTMLResponse) #, response_model=User, tags=["users"])
def create_user(request: Request, username: str = Form(...), password: str = Form(...), email:str = Form(...)):#user:User):
    

    new_user={"name":username, "password":password, "email":email}
    new_user["password"]=sha256_crypt.encrypt(new_user["password"])
    print(new_user["password"])

    conn.erney.second_db_in_mongo.insert_one(new_user)
    

    return templates.TemplateResponse("user_criet.html", {"request": request})




@user.get('/users', response_model=list[User], tags=["users"])
def fidn_all_user():
    return usersentity(conn.erney.second_db_in_mongo.find())


   




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
