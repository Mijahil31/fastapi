from fastapi import FastAPI
from app.api.api_v1.users.route import router 

app = FastAPI()
app.include_router(router)