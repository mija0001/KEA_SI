import mysql.connector
import credentials # Local credentials file to prevent publishing credentials to GitHub
import datetime

# Database commander class, used to add, update and delete entries, only has INSERT and SELECT privileges
class DatabaseCommander:
    def connect_to_database():
        # Connect to the database
        db = mysql.connector.connect(
            host=credentials.host,
            user=credentials.command_user,
            password=credentials.command_password,
            database=credentials.database
        )
        # Create a cursor
        cursor = db.cursor()
        return db, cursor


    # Add new product to database
    def add_new_product(guid, name, description, image_hash):
        db, cursor = DatabaseCommander.connect_to_database()
        create_time = datetime.datetime.now()
        sql = "INSERT INTO product (id, guid, create_time) " \
                "SELECT NULL, %s, %s " \
                "WHERE NOT EXISTS (SELECT 1 FROM product WHERE guid = %s)"
        val = (guid, create_time, guid)
        cursor.execute(sql, val)
        db.commit()
        db.close()
        print("Product added to database")
        DatabaseCommander.add_product_snapshot(guid, name, description, image_hash) # Create a snapshot of the product


    # Add product snapshot to database
    def add_product_snapshot(guid, name, description, image_hash):
        db, cursor = DatabaseCommander.connect_to_database()
        timestamp = datetime.datetime.now()
        print(timestamp)
        sql = "INSERT INTO product_data (id, guid, timestamp, name, description, image_hash) " \
                "SELECT NULL, %s, %s, %s, %s, %s "
        val = (guid, timestamp, name, description, image_hash)
        cursor.execute(sql, val)
        db.commit()
        db.close()
        print("Product snapshot added to database")


    # Delete product from database
    def delete_product(guid):
        db, cursor = DatabaseCommander.connect_to_database()
        timestamp = datetime.datetime.now()
        sql = "INSERT INTO product_delete (id, guid, timestamp) " \
                "SELECT NULL, %s, %s " \
                "WHERE NOT EXISTS (SELECT 1 FROM product_delete WHERE guid = %s)"
        val = (guid, timestamp, guid)
        cursor.execute(sql, val)
        db.commit()
        db.close()
        print("Product deleted")