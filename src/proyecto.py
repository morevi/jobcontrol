#----------------------------------------------------------------------------
# Este archivo producto.py contiene la implementación de la clase Proyecto.
#----------------------------------------------------------------------------
# @author: Antonio Caño @eantoniocalo18 
# @created_date: 29/11/2021
# @version: '2.0'
# ---------------------------------------------------------------------------



class Proyecto:
    """
    Clase utilizada para representar un Proyecto.
    ...
    Atributos
    ----------
   
    Publicos
    id: str
        uuid o id que identifica cada Proyecto único
    planificacion : int
        cantidad de horas estimadas para la realización del proyecto
    horarios : Horario []
        array con los horarios en los que se almacena la información de las horas trabajads por cada usuario
    """
    def __init__(self, id, planificacion, horarios):
        self.id = id
        self.planificacion = planificacion
        self.horarios = horarios
