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
    nombre: str
        nombre del Proyecto
    planificacion : int
        cantidad de horas estimadas para la realización del proyecto
    recuento : Diccionario { Usuario : horas }
        diccionario donde se recogerá
    
    Métodos 
    ----------
    
    add_horas(usuario, horas):
        " Método que añadirá las horas indicadas al recuento de horas del usuario "
    """
    def __init__(self, nombre, planificacion, recuento):
        self.nombre = nombre
        self.planificacion = planificacion
        self.recuento = recuento 

        # El recuento tendrá que tener todos sus valores a 0 puesto 
        # que el proyecto se crea antes de que ningún usuario introduzca sus horas
        
    def add_horas(usuario, horas):
        " Método que añadirá las horas indicadas al recuento de horas del usuario "
        pass
