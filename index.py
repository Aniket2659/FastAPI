from fastapi import FastAPI
app = FastAPI()
from routes.employee import user
app.include_router(user)  
