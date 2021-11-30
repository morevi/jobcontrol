#----------------------------------------------------------------------------
# Este archivo dia.py contiene la implementaciÃ³n de la clase dia.
#----------------------------------------------------------------------------
# @author: Antonio Caño @eantoniocalo18 
# @created_date: 29/11/2021
# @version: '2.0'
# ---------------------------------------------------------------------------



class Dia:
    """
    Clase utilizada para representar un día trabajado
    ...
    Atributos
    ----------
   
    Publicos
    id: str
        uuid o id que identifica cada día único
    usuario_relacionado: str
        uuid o id que identicada al usuario relacionado con el día trabajado
    fecha : date
        fecha del día trabajado
    hora_inicio : int
        Hora en la que el usuario ha comenzado a trabajar
    hora_fin : int
        Hora en la que el usuario ha terminado de trabajar
    horas_descanso : int
        Número de horas que han transcurrido desde el inicio hasta el fin de la jornada laboral y el usuario ha estado descansando
    Métodos
    -------
        calcular_horas():
            "Método que devolverá las horas trabajadas por el usuario en el día"

    """
    def __init__(self, id,usuario_relacionado, fecha, hora_inicio,hora_fin , horas_descanso):
        self.id = id
        self.fecha = fecha
	self.usuario_relacionado = usuario_relacionado
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.horas_descanso = horas_descanso

    def calcular_horas():
        "Método que devolverá las horas trabajadas por el usuario en el día"
        pass

    
