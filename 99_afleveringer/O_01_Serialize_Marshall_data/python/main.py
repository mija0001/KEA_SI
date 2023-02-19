import requests
import pickle
from classes import Person # Import Person class, since only the instance is serialized, not the class definition

pickle_rick = requests.get("http://localhost:8000/pickle_rick").content # Get serialized data from server

rick = pickle.loads(pickle_rick) # Deserialize data

rick.introduce() # Test if deserialization worked
# OBS: Executing serialized code is a security risk and generally considered bad practice