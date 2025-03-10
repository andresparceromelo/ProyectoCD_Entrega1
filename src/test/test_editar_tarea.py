import pytest
from src.main import GestorUsuario, GestorTarea
@pytest.fixture
def gestor():
    gestor = GestorUsuario()
    gestor.crear_cuenta("juan23", "abc12345")
    gestor.crear_cuenta("maria99", "pass98765")
    gestor.crear_cuenta("usr", "abc45678")
    
    gestor_tareas = GestorTarea()
    gestor_tareas.crear_tarea("juan23", "Comprar pan", "Personal", "Por hacer", gestor)
    gestor_tareas.crear_tarea("maria99", "Hacer informe", "Trabajo", "Por hacer", gestor)
    gestor_tareas.crear_tarea("usr", "Ejercicio", "Salud", "Por hacer", gestor)
    
    return gestor, gestor_tareas

# 🟢 Casos Normales
def test_editar_tarea_normal_1(gestor):
    gestor, gestor_tareas = gestor
    gestor_tareas.editar_tarea("juan23", "Comprar pan", "Comprar comida", "Personal", "En progreso", gestor)
    assert gestor.usuarios["juan23"].tareas[0].txt_tarea == "Comprar comida"

def test_editar_tarea_normal_2(gestor):
    gestor, gestor_tareas = gestor
    gestor_tareas.editar_tarea("maria99", "Hacer informe", "Terminar informe", "Trabajo", "Completada", gestor)
    assert gestor.usuarios["maria99"].tareas[0].txt_tarea == "Terminar informe"

def test_editar_tarea_normal_3(gestor):
    gestor, gestor_tareas = gestor
    gestor_tareas.editar_tarea("usr", "Ejercicio", "Ir al gimnasio", "Salud", "Por hacer", gestor)
    assert gestor.usuarios["usr"].tareas[0].txt_tarea == "Ir al gimnasio"

# 🔴 Casos de Error
def test_editar_tarea_usuario_no_existe(gestor):
    gestor, gestor_tareas = gestor
    with pytest.raises(ValueError, match="Usuario no encontrado"):
        gestor_tareas.editar_tarea("usuario_inexistente", "Cualquier tarea", "Nuevo texto", "Trabajo", "Por hacer", gestor)

def test_editar_tarea_no_existe(gestor):
    gestor, gestor_tareas = gestor
    with pytest.raises(ValueError, match="Tarea no encontrada"):
        gestor_tareas.editar_tarea("juan23", "Tarea inexistente", "Nuevo texto", "Personal", "Por hacer", gestor)

def test_editar_tarea_texto_vacio(gestor):
    gestor, gestor_tareas = gestor
    with pytest.raises(ValueError, match="El texto de la tarea no puede estar vacío"):
        gestor_tareas.editar_tarea("maria99", "Hacer informe", "", "Trabajo", "Por hacer", gestor)

# 🟡 Casos Extremos
def test_editar_tarea_texto_maximo(gestor):
    gestor, gestor_tareas = gestor
    texto_largo = "A" * 255
    gestor_tareas.editar_tarea("juan23", "Comprar pan", texto_largo, "Trabajo", "Por hacer", gestor)
    assert gestor.usuarios["juan23"].tareas[0].txt_tarea == texto_largo

def test_editar_tarea_categoria_maxima(gestor):
    gestor, gestor_tareas = gestor
    categoria_larga = "x" * 50
    gestor_tareas.editar_tarea("maria99", "Hacer informe", "Leer libros y artículos", categoria_larga, "Completada", gestor)
    assert gestor.usuarios["maria99"].tareas[0].categoria == categoria_larga

def test_editar_tarea_estado_maximo(gestor):
    gestor, gestor_tareas = gestor
    estado_largo = "x" * 20
    gestor_tareas.editar_tarea("usr", "Ejercicio", "Aprender Python", "Educación", estado_largo, gestor)
    assert gestor.usuarios["usr"].tareas[0].estado == estado_largo

