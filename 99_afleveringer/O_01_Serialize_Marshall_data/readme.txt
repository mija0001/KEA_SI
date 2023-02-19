--- Task ---
Try it out in any language or just look into it.
For Python look into how to serialize and marshall with Pickle.

---Python solution---
99_afleveringer\O_01_Serialize_Marshall_data\python\classes.py:
Contains a Person class with a introduce() method, for testing.

99_afleveringer\O_01_Serialize_Marshall_data\python\server.py:
Starts a webserver on port 8000 that serves a serialized Person object on the /pickle_rick endpoint

99_afleveringer\O_01_Serialize_Marshall_data\python\main.py:
Requests the serialized Person object from the webserver, 
deserializes the object, and executes the Person.introduce() on the object