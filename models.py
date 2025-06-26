import db
from sqlalchemy import Column, Integer, String, Boolean

'''
Creamos una clase llamada Tarea
Esta clase va a ser nuestro modelo de datos de la tarea (el cual nos servirá
luego para la base de datos)
Esta clase va a almacenar toda la información referente a una tarea
'''


class Tarea(db.Base):
    __tablename__ = "tarea"
    id = Column(Integer, primary_key=True)  # Identificador único de cada tarea
    contenido = Column(String(200), nullable=False)  # Contenido de la tarea, un
    hecha = Column(Boolean)  # Booleano que indica si una tarea ha sido hecha o no


    def __init__(self, contenido, hecha):
        self.contenido = contenido
        self.hecha = hecha


    def __repr__(self):
        return "Tarea {}: {} ({})".format(self.id, self.contenido, self.hecha)


    def __str__(self):
        return "Tarea {}: {} ({})".format(self.id, self.contenido, self.hecha)
