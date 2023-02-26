from fastapi import FastAPI
import uvicorn
import requests
from data_classes import BookData
from parser_classes import BookParser

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/book_from_json")
def book_from_json():
    book = BookParser().import_book_from_json("data/book.json")
    return book


@app.get("/book_from_yaml")
def book_from_yaml():
    book = BookParser().import_book_from_yaml("data/book.yaml")
    return book


@app.get("/book_from_xml")
def book_from_xml():
    book = BookParser().import_book_from_xml("data/book.xml")
    return book


@app.get("/book_from_csv")
def book_from_csv():
    book = BookParser().import_book_from_csv("data/book.csv")
    return book


@app.get("/book_from_txt")
def book_from_txt():
    book = BookParser().import_book_from_txt("data/book.txt")
    return book


@app.get("/book_from_other_server")
def book_from_txt():
    response = requests.get("http://127.0.0.1:8001/book_from_json")
    book = response.json()
    return book


# Start server with uvicorn on port 8000
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)