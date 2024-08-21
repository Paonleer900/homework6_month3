import sqlite3

conn = sqlite3.connect('db_main.db')
cursor = conn.cursor()

CREATE_TABLE_REGISTRATION = """
    CREATE TABLE IF NOT EXISTS registration
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id VARCHAR(255),
        firstname VARCHAR(255)
    )
"""

CREATE_TABLE_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS products
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255),
        size VARCHAR(255),
        price VARCHAR(255),
        id_product VARCHAR(255),
        photo TEXT
    )
"""

CREATE_TABLE_PRODUCTS_DETAILS = """
    CREATE TABLE IF NOT EXISTS products_details
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category VARCHAR(255),
        info_product VARCHAR(255),
        id_product VARCHAR(255)
    )
"""

CREATE_TABLE_COLLECTION_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS collection_products
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        productid INTEGER NOT NULL,
        collection TEXT NOT NULL
    )
"""

cursor.execute(CREATE_TABLE_REGISTRATION)
cursor.execute(CREATE_TABLE_PRODUCTS)
cursor.execute(CREATE_TABLE_PRODUCTS_DETAILS)
cursor.execute(CREATE_TABLE_COLLECTION_PRODUCTS)

INSERT_INTO_TABLE_REGISTRATION = """
    INSERT INTO registration(telegram_id, firstname)
    VALUES (?, ?)
"""

INSERT_PRODUCTS = """
    INSERT INTO products(name, size, price, id_product, photo)
    VALUES (?, ?, ?, ?, ?)
"""

INSERT_PRODUCTS_DETAILS = """
    INSERT INTO products_details(category, info_product, id_product)
    VALUES (?, ?, ?)
"""

INSERT_COLLECTION_PRODUCTS = """
    INSERT INTO collection_products(productid, collection)
    VALUES (?, ?)
"""

productid = 1
collection = 'Winter Collection'

cursor.execute(INSERT_COLLECTION_PRODUCTS, (productid, collection))

conn.commit()
conn.close()
