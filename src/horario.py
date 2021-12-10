#----------------------------------------------------------------------------
# Este archivo producto.py contiene la implementación de la clase Horario.
#----------------------------------------------------------------------------
# @author: Antonio Caño @eantoniocalo18 
# @created_date: 29/11/2021
# @version: '2.0'
# ---------------------------------------------------------------------------


class Horario:
    """
    Clase utilizada para representar un Horario.
    ...
    Atributos
    ----------
   
    Publicos
    id: str
        uuid o id que identifica cada horario único
    usuario_relacionado : str
        uuid o id que identifica el usuario asociado al
    horas_trabajadas : int
	entero que lleva la sumatoria de las horas que ha ido trabajando un usuario

    Métodos
    -------
        get_horas_trabajadas():
            " Método que devolverá las horas_trabajadas por el usuario"
	to_CSV(): 
	    "Método que permitirá exportar a formato CSV los datos referentes a un horario" 
 """
    def __init__(self, id, usuario_relacionado, horas_trabajadas):
        self.id = id
        self.nombre = usuario_relacionado
	self.horas_trabajadas = horas_trabajadas

    def get_horas_trabajadas():
	" Método que devolverá las horas_trabajadas por el usuario"
	pass

    def to_CSV():
        " Método que devolverá las horas trabajadas por el usuario en este horario"
	pass
