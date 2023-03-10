import express from "express"
const app = express()

import swaggerUi from "swagger-ui-express"
import swaggerJsdoc from "swagger-jsdoc"

// Swagger configuration
const swaggerDefinition = {
    openapi: "3.0.0",
    info: {
        title: "Convert API",
        version: "1.0.0",
        description: "A simple API for converting units of length",
    },
}

// Options for the swagger docs
const options = {
    swaggerDefinition,
    apis: ["./routers/*.js"], // files to include in the documentation
}

app.use("/docs", swaggerUi.serve, swaggerUi.setup(swaggerJsdoc(options))) // serve the documentation at /docs
app.use(express.json()) // parse JSON bodies
import unitsRouter from "./routers/unitsRouter.js" // import the units router
app.use(unitsRouter) // use the units router

app.listen(8080, () => console.log("Server running on port 8080")) // start the server