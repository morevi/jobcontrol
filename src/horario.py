'''Horario.py'''

class Horario:
    '''Represent a weekly timetable'''

    def __init__(self, fecha_inicio, usuario_relacionado, horas_trabajadas: float):
        '''Initialize the object'''
        self.fecha_inicio = fecha_inicio
        self.nombre = usuario_relacionado
        self.horas_trabajadas = horas_trabajadas

    def get_horas_trabajadas() -> float:
        '''Counts the number of hours worked'''

    def to_CSV() -> str:
        '''Export this timetable on a human readable format'''
