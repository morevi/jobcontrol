#----------------------------------------------------------------------------
# Este archivo cliente.py contiene la implementaciÃ³n de la clase Producto.
#----------------------------------------------------------------------------
# @author: Antonio Caño @eantoniocalo18 
# @created_date: 29/11/2021
# @version: '2.0'
# ---------------------------------------------------------------------------



class usuario:
    """
    Clase utilizada para representar un Proyecto.
    ...
    Atributos
    ----------
   
    Publicos
    id: str
        uuid o id que identifica cada usuario único
    email : str
        email del usuario
    nombre : str
        nombre del usuario
    apellidos : srt
        apellidos del usuario
    horarios : Horario []
        array que almacenará los horarios que tenga el usuario
    Métodos
    -------
        crear_horario():
            "Método que creará un objeto de tipo Horario"
        actualizar_horario():
            "Método que modificará los datos de un Horario"
        confirmar_horario():
            "Método que permitirá confirmar un Horario"
    """
    def __init__(self, id, email, nombre, apellidos, horarios):
        self.id = id
        self.email = email
        self.nombre = nombre
        self.apellidos = apellidos
        self.horarios = horarios

    def crear_horario():
        "Método que creará un objeto de tipo Horario"
        pass
    def actualizar_horario():
        "Método que modificará los datos de un Horario"
        pass
    def confirmar_horario():
        "Método que permitirá confirmar un Horario"
        pass
    