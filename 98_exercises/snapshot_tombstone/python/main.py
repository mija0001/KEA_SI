import uuid
from database_command import DatabaseCommander as db_command
from database_request import DatabaseRequester as db_request
from database_initializer import DatabaseInitializer as db_init


### TEST CODE ###
db_init.reset_database() # Reset database
product_guid = uuid.uuid4() # Generate a new GUID
db_command.add_new_product(str(product_guid), "Test Product", "Test Description", "Test Image Hash") # Add a new product
db_command.add_product_snapshot(str(product_guid), "Test Product Update", "Test Description Update", "Test Image Hash Update") # Update the product
print(db_request.get_product(str(product_guid))) # Get the product, should return the updated product
print(db_command.delete_product(str(product_guid))) # Delete the product
print(db_request.get_product(str(product_guid))) # Get the product, should return nothing