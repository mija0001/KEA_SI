from fastapi import FastAPI
from datetime import datetime
import requests

app = FastAPI()

@app.get("/date")
def get_date():
    return datetime.now()

@app.get("/datefromexpress")
def get_date_from_express():
    response = requests.get("http://127.0.0.1:8080/date")
    return response.json()

@app.get("/datefromtobias")
def get_date_from_tobias():
    response = requests.get("https://11a6-195-249-146-101.ngrok.io/date")
    return response.json()