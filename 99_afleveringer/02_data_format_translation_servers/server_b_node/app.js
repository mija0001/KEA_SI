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


app.listen(8001, () => {
    console.log("Server running on port 8001");
    })