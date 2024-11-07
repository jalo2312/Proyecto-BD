import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        user='root',
        password='2312',
        host='localhost',
        database='registro_usuarios',
        auth_plugin='mysql_native_password'
    )
