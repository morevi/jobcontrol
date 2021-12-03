#----------------------------------------------------------------------------
# Este archivo horario.py contiene la implementaciÃ³n de la clase Horario.
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
        uuid o id que identifica el usuario asociado 
    horas_semanales: int
        entero que determinará las horas que tiene que trabajar un usuario en una semana
    dias_trabajados : Dia []
        array de objetos dia que contendrá el horario
    Métodos
    -------
        horas_trabajadas():
            "Método que devolverá las horas trabajadas por el usuario en este horario"
        add_dia():
            "Método que añadirá un nuevo día al vector de días trabajados"
        get_dias_trabajados():
            "Método que devolverá el vector de días que se han trabajado"
        get_horas_restantes():
            "Método que devolverá las horas que le quedan por trabajar al usuario en la semana actual"
        to_CSV():
            "Método que pasa los datos referentes al horario al formato .csv"
    """
    def __init__(self, id, usuario_relacionado,horas_semanales, dias_trabajados):
        self.id = id
        self.id_usuario = usuario_relacionado
        self.horas_semanales = horas_semanales
        self.dias_trabajados = dias_trabajados

    def horas_trabajadas():
        "Método que devolverá las horas trabajadas por el usuario en este horario"
        pass
    def  add_dia():
        "Método que añadirá un nuevo día al vector de días trabajados"
        pass
    def  get_dias_trabajados():
        "Método que devolverá el vector de días que se han trabajado"
        pass
    def  get_horas_restantes():
        "Método que devolverá las horas que le quedan por trabajar al usuario en la semana actual"
        pass
    
    
