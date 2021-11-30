#----------------------------------------------------------------------------
# Este archivo proyecto.py contiene la implementaciÃ³n de la clase Proyecto.
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
    nombre : str
        el nombre del proyecto
    planificacion : int
        cantidad de horas estimadas para la realización del proyecto
    usuarios_asignados : Usuario []
        array con los usuarios que van a realizar el proyecto
    Métodos
    -------
        is_finalizado():
            "Método que devolverá true si el proyecto ha sido terminado"
        horas_restantes():
            "Método que devolverá las horas restantes que quedan según la planificación"
    """
    def __init__(self, id, nombre, planificacion, usuarios_asignados):
        self.id = id
        self.nombre = nombre
        self.planificacion = planificacion
        self.usuarios_asignados = usuarios_asignados

    def is_finalizado():
        "Método que devolverá true si el proyecto ha sido terminado"
        pass
    def horas_restantes():
        "Método que devolverá las horas restantes que quedan según la planificación"
        pass
    
