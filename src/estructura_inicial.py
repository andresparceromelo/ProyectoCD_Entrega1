class Tarea:
    
    def __init__(self, txt_tarea, categoria, estado) -> None:
        self.tareas: Tarea = []
        self.txt_tarea : str = txt_tarea
        self.estado : str = estado
        pass
    
class GestorTarea:
    
    def crear_tarea(self):
        pass
    
    def editar_tarea(self):
        pass
    
    def eliminar_tarea(self):
        pass
    
class Usuario:
    def __init__(self, id_usuario, contraseña):
        self.id_usuario = id_usuario
        self.contraseña = contraseña
        self.tareas = []


class GestorUsuario:
    def __init__(self) -> None:
       self.usuarios = {}
        
    def crear_cuenta(self, id, contraseña):
        pass
    
    def iniciar_sesion(self):
        pass
    
    def cambiar_contraseña(self):
        pass

    