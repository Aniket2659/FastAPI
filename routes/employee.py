from fastapi import APIRouter
from models.model import Employee
from schemas.serializer import user_entity,user_entities
from config.db import conn 
from bson import ObjectId

user=APIRouter()

@user.post('/')
async def create_employee(emp:Employee):
    conn.local.user.insert_one(dict(emp))
    return user_entities(conn.local.user.find())

@user.get("/")
async def list():
    return user_entities(conn.local.user.find())

@user.put('/{id}')
async def update(id,emp:Employee):
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(emp)})
    return user_entity(conn.local.user.find_one({"_id":ObjectId(id)}))

from fastapi import HTTPException

@user.delete("/{id}")
async def delete_user(id: str):
    user = conn.local.user.find_one({"_id": ObjectId(id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    conn.local.user.find_one_and_delete({"_id": ObjectId(id)})
    return user_entity(user)                                                                                       
              