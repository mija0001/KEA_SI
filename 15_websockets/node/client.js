import WebSocket from "ws";

const webSocketClient = new WebSocket("ws://localhost:8080");

webSocketClient.on("open", () => {
    console.log("Connected to the server");
    webSocketClient.send("This message was sent for the client");
});