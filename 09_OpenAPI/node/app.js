import express from "express";
const app = express();

app.use(express.json());

import swaggerUi from "swagger-ui-express";
import swaggerJsdoc from "swagger-jsdoc";

const swaggerDefinition = {
    openapi: "3.0.0",
    info: {
        title: "Users API",
        version: "1.0.0",
        description: "A simple Express Users API",
    },
};

const options = {
    swaggerDefinition,
    apis: ["./routers/*.js"],
};

app.use("/docs", swaggerUi.serve, swaggerUi.setup(swaggerJsdoc(options)))


import usersRouter from "./routers/usersRouter.js";
app.use(usersRouter)
import spacecraftRouter from "./routers/spacecraftRouter.js";
app.use(spacecraftRouter)

app.listen(8080, () => console.log("Server running on port 8080"));