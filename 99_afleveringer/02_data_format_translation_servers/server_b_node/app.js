import express from "express";
const app = express();

app.get("/", (req, res) => {
    res.send("Hello World!");
    });


app.get("/book_from_json", (req, res) => {

    res.json({"Hello": "World!"});
    });


app.listen(8001, () => {
    console.log("Server running on port 8001");
    })