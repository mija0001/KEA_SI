from fastapi import FastAPI, Request, Response
import json

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request, response: Response):
    payload = await request.body()
    data = json.loads(payload)
    print("Message type: " + data['messageType'])
    print("Event type: " + data['eventType'])
    print("Message: " + data['message'])
    response.status_code = 200