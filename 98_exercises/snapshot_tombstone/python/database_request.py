import mysql.connector
import credentials # Local credentials file to prevent publishing credentials to GitHub

# Database requester class, used to get entries, only has SELECT privileges
class DatabaseRequester:
    def connect_to_database():
        # Connect to the database
        db = mysql.connector.connect(
            host=credentials.host,
            user=credentials.request_user,
            password=credentials.request_password,
            database=credentials.database
        )
        # Create a cursor
        cursor = db.cursor()
        return db, cursor


    # Get product from database
    def get_product(guid):
        if not DatabaseRequester.is_product_deleted(guid):
            # Get product data
            db, cursor = DatabaseRequester.connect_to_database()
            sql = "SELECT product_data.name, product_data.description, product_data.image_hash, product_data.timestamp " \
                    "FROM product INNER JOIN product_data ON product.guid=product_data.guid " \
                    "WHERE product.guid = %s " \
                    "ORDER BY timestamp DESC " \
                    "LIMIT 1"
            val = (guid,)
            cursor.execute(sql, val)
            result = cursor.fetchone()
            db.close()
            return result
        else:
            print("Product has been deleted")
            return ()
        

    # Check if product has been deleted
    def is_product_deleted(guid):
        db, cursor = DatabaseRequester.connect_to_database()
        sql = "SELECT 1 FROM product_delete WHERE guid = %s"
        val = (guid,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        db.close()
        if result is not None:
            return True # Product has been deleted
        else:
            return False # Product has not been deleted