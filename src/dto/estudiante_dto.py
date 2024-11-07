# src/dto/estudiante_dto.py
class EstudianteDTO:
    def __init__(self, cedula, nombres, apellidos, direccion_residencia, lat_res, lon_res, direccion_trabajo, lat_trab, lon_trab):
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion_residencia = direccion_residencia
        self.lat_res = lat_res
        self.lon_res = lon_res
        self.direccion_trabajo = direccion_trabajo
        self.lat_trab = lat_trab
        self.lon_trab = lon_trab
0