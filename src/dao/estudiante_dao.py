# src/dao/estudiante_dao.py
import mysql.connector
from dto.estudiante_dto import EstudianteDTO

class DatabaseConnectionSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if DatabaseConnectionSingleton._instance is None:
            DatabaseConnectionSingleton._instance = mysql.connector.connect(
                user='root',
                password='2312',
                host='localhost',
                database='registro_usuarios',
                auth_plugin='mysql_native_password'
            )
        return DatabaseConnectionSingleton._instance

class EstudianteDAO:
    def __init__(self):
        self.db_connection = DatabaseConnectionSingleton.get_instance()

    def add_estudiante(self, estudiante):
        cursor = self.db_connection.cursor()
        sql = """
            INSERT INTO usuarios (cedula, nombres, apellidos, direccion_residencia, ubicacion_residencia, direccion_trabajo, ubicacion_trabajo)
            VALUES (%s, %s, %s, %s, POINT(%s, %s), %s, POINT(%s, %s))
        """
        data = (estudiante.cedula, estudiante.nombres, estudiante.apellidos,
                estudiante.direccion_residencia, estudiante.lat_res, estudiante.lon_res,
                estudiante.direccion_trabajo, estudiante.lat_trab, estudiante.lon_trab)
        cursor.execute(sql, data)
        self.db_connection.commit()
        cursor.close()

    