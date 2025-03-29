# main.py
from fastapi import FastAPI
from controllers.user import user_router


app = FastAPI(title='Task API')

app.include_router(user_router)
