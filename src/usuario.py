'''Usuario.py'''

from .horario import Horario
from datetime import time, date, timedelta

class Usuario():
    '''Represent an user'''

    def __init__(self, name: str, horarios=None):
        '''Initialize the object'''
        self.name = name
        self.horarios = horarios if horarios else []

    def search_horario(self, fecha) -> Horario:
        '''Search in horarios for the specified week, an returns it, or, in if it was not found, a replacement
        '''

        if fecha.weekday() != 0 or not self.horarios:
            return Horario(fecha)

        self.horarios.sort(key=lambda h: h.fecha_inicio, reverse=False)

        #before first
        found = Horario(fecha)
        h = self.horarios[0]
        if fecha < h.fecha_inicio:
            found.dias = h.dias
            return found

        #after first
        for h in self.horarios:
            if fecha >= h.fecha_inicio:
                found.dias = h.dias
                return found
            else:
                found.dias = h.dias

        return found

    def get_horarios_between(self, first, last):
        '''Search and generate horarios between those mondays.
        '''
        serie = []

        if first <= last:
            ptr = first
            while ptr <= last:
                serie.append(self.search_horario(ptr))
                ptr += timedelta(days=7)

        return serie



        
