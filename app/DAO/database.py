import mysql.connector

def get_db():
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = "123456",
        database="Empresa"
    )
    return connection