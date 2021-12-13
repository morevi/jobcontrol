'''Horario.py'''
from typing import Dict, List, Tuple
from datetime import time, date, timedelta

class Horario:
    '''Represent a weekly schedule'''

    def __init__(self, fecha_inicio, tabla=None):
        '''Initialize the object'''
        if not self.validate_horario(fecha_inicio, tabla):
            raise Exception('Este horario no es valido')

        self.fecha_inicio = fecha_inicio
        self.dias = tabla if tabla else {}

    def add_days(self, tabla):
        '''override the default table of days'''

        nuevo = self.dias
        nuevo.update(tabla)

        if not self.validate_horario(self.fecha_inicio, nuevo):
            Exception('Este horario no es valido')
        else:
            self.dias = nuevo

    def to_CSV() -> str:
        '''Export this timetable on a human readable format'''

    @staticmethod
    def get_horas_trabajadas(tabla) -> float:
        '''Counts the number of hours worked'''
        
        count = 0
        for k in tabla.keys():
            dia = tabla[k]

            for franja in dia:
                count += franja[1]

        return count

    @staticmethod
    def validate_horario(fecha, tabla=None):
        if fecha.weekday() != 0:
            # lunes
            return False

        if tabla:
            if len(tabla.keys()) > 7:
                # como mucho 7 dias
                return False

            for k in tabla.keys():
                # deben estar nombrados correctamente
                if not k in ['L', 'M', 'X', 'J', 'V', 'S', 'D']:
                    return False

            # nº horas trabajadas deben ser real
            if Horario.get_horas_trabajadas(tabla) > 24*7:
                return False

        return True
