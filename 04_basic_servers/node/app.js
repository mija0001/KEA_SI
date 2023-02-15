import express from "express";
const app = express();

app.get("/", (req, res) => {
    res.send({ message: "Our first Expresss route" });
});

app.get("/newroute", (req, res) => {
    res.send({ message: "Our second Expresss route" });
});

app.listen(8080, () => console.log("Server is running on port", 8080));
