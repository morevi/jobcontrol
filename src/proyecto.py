'''Proyecto.py'''

class Proyecto:
    '''Represent a project'''

    def __init__(self, nombre: str, planificacion: float, recuento: dict):
        '''Initialize the object'''
        self.nombre = nombre
        self.planificacion = planificacion
        self.recuento = recuento 

        # El recuento tendrá que tener todos sus valores a 0 puesto 
        # que el proyecto se crea antes de que ningún usuario introduzca sus horas
        
    def add_horas(usuario, horas):
        '''Register hours worked on this project to an user'''
