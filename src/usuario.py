'''Usuario.py'''

from typing import List
from horario import Horario

class Usuario():
    '''Represent an user'''

    def __init__(self, name: str, horarios=None: List[Horario]):
        '''Initialize the object'''
        self.name = name
        self.horarios = horarios if horarios else []

    def search_horarios(semana) -> Horario:
        '''Search in horarios for the specified week, an returns it of a 
        replacement
        '''

    def generate_control_horario(desde, hasta) -> str:
        '''Generate the control for this user between the specified dates
        '''
