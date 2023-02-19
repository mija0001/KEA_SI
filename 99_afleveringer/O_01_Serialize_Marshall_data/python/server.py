from fastapi import FastAPI
from fastapi import APIRouter, Response
import uvicorn
import pickle
from classes import Person # Import class to be serialized


app = FastAPI()


rick = Person("Rick", "C-137") # Create instance of Person to be serialized
pickle_rick = pickle.dumps(rick) # Serialize instance of Person


# Create route to serve serialized data
@app.get("/pickle_rick")
def root() -> bytes: # Return type is bytes
    return Response(pickle_rick) # Serve serialized data


# Start server with uvicorn on port 8000
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
