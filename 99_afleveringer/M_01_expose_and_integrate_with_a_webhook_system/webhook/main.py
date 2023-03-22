from fastapi import FastAPI, Request, Response
import uvicorn
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
    

# Start server with uvicorn on port 8000
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)