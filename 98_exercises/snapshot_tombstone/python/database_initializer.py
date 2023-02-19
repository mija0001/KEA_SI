import mysql.connector
import credentials # Local credentials file to prevent publishing credentials to GitHub

# Database initializer class, used to create and reset tables, has full privileges, only used for testing purposes
class DatabaseInitializer:
    def connect_to_database():
        # Connect to the database
        db = mysql.connector.connect(
            host=credentials.host,
            user=credentials.crud_user,
            password=credentials.crud_password,
            database=credentials.database
        )
        # Create a cursor
        cursor = db.cursor()
        return db, cursor


    def create_product_table():
        db, cursor = DatabaseInitializer.connect_to_database()
        cursor.execute( \
        "CREATE TABLE product(" \
        "id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary key, not used'," \
        "guid char(36) NOT NULL COMMENT 'Product GUID'," \
        "create_time datetime(6) NOT NULL COMMENT 'Create time')" \
        )
        db.commit()
        db.close()


    def create_product_data_table():
        db, cursor = DatabaseInitializer.connect_to_database()
        cursor.execute( \
        "CREATE TABLE product_data(" \
        "id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary key, not used'," \
        "guid char(36) NOT NULL COMMENT 'Product GUID'," \
        "timestamp datetime(6) NOT NULL COMMENT 'Snapshot timestamp'," \
        "name varchar(255) NOT NULL COMMENT 'Product name'," \
        "description varchar(10000) NOT NULL COMMENT 'Product description'," \
        "image_hash char(64) NOT NULL COMMENT 'Product image hash')" \
        )
        db.commit()
        db.close()


    def create_product_delete_table():
        db, cursor = DatabaseInitializer.connect_to_database()
        cursor.execute( \
        "CREATE TABLE product_delete(" \
        "id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Primary key, not used'," \
        "guid char(36) NOT NULL COMMENT 'Product GUID'," \
        "timestamp datetime(6) NOT NULL COMMENT 'Snapshot timestamp')" \
        )
        db.commit()
        db.close()


    # Reset database for testing purposes
    # This will delete all data in the database!
    def reset_database():
        db, cursor = DatabaseInitializer.connect_to_database()
        cursor.execute("TRUNCATE TABLE product")
        cursor.execute("TRUNCATE TABLE product_data")
        cursor.execute("TRUNCATE TABLE product_delete")
        db.commit()
        db.close()
        print("¨-----[Database reset]-----")


    def create_tables():
        DatabaseInitializer.create_product_table()
        DatabaseInitializer.create_product_data_table()
        DatabaseInitializer.create_product_delete_table()