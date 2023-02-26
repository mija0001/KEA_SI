import express from "express";
import { importBookFromJSON } from "./parser.js";
import { importBookFromYAML } from "./parser.js";

const app = express();

app.get("/", (req, res) => {
    res.send("Hello World!");
    });


app.get("/book_from_json", (req, res) => {
    res.json(importBookFromJSON("data/book.json"));
    });


app.get("/book_from_yaml", (req, res) => {
    res.json(importBookFromYAML("data/book.yaml"));
    });


app.get("/book_from_other_server", async (req, res) => {
    const response = await fetch("http://127.0.0.1:8000/book_from_json");
    const book = await response.json();
    res.send(book);
    });


app.listen(8001, () => {
    console.log("Server running on port 8001");
    })