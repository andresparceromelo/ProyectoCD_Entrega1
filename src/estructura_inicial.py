from datetime import datetime

class Tarea:
    def __init__(self, txt_tarea: str, usuario_creador: str, categoria: str, estado: str) -> None:
        self.txt_tarea: str = txt_tarea
        self.usuario_creador: str = usuario_creador
        self.fecha_creacion: datetime = datetime.now()
        self.categoria: str = categoria
        self.estado: str = estado  
    
    def __repr__(self):
        return f"Tarea('{self.txt_tarea}', '{self.usuario_creador}', '{self.categoria}', '{self.estado}')"


class GestorTarea:
    def __init__(self):
        self.tareas = []  
    
    def crear_tarea(self, tarea: Tarea):
        pass 
    
    def editar_tarea(self, tarea_id: int, nuevos_datos: dict):
        pass 
    
    def eliminar_tarea(self, tarea_id: int):
        pass  


class Usuario:
    def __init__(self, id_usuario: str, contraseña: str) -> None:
        self.id_usuario: str = id_usuario
        self.contraseña: str = contraseña
        self.tareas: list[Tarea] = []  
    
    def agregar_tarea(self, tarea: Tarea):
        self.tareas.append(tarea)
    
    def __repr__(self):
        return f"Usuario('{self.id_usuario}')"


class GestorUsuario:
    def __init__(self) -> None:
        self.usuarios: dict[str, Usuario] = {}  
    
    def crear_cuenta(self, id_usuario: str, contraseña: str):
        pass 
    
    def iniciar_sesion(self, id_usuario: str, contraseña: str):
        pass
    
    def cambiar_contraseña(self, id_usuario: str, nueva_contraseña: str):
        pass  
