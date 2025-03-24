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
def test_eliminar_tarea_normal_1(gestor):
    gestor, gestor_tareas = gestor
    gestor_tareas.eliminar_tarea("juan23", "Comprar pan", gestor)
    assert not any(t.txt_tarea == "Comprar pan" for t in gestor.usuarios["juan23"].tareas)

def test_eliminar_tarea_normal_2(gestor):
    gestor, gestor_tareas = gestor
    gestor_tareas.eliminar_tarea("maria99", "Hacer informe", gestor)
    assert not any(t.txt_tarea == "Hacer informe" for t in gestor.usuarios["maria99"].tareas)

def test_eliminar_tarea_normal_3(gestor):
    gestor, gestor_tareas = gestor
    gestor_tareas.eliminar_tarea("usr", "Ejercicio", gestor)
    assert not any(t.txt_tarea == "Ejercicio" for t in gestor.usuarios["usr"].tareas)

# 🔴 Casos de Error
def test_eliminar_tarea_usuario_no_existe(gestor):
    gestor, gestor_tareas = gestor
    with pytest.raises(ValueError, match="Usuario no encontrado"):
        gestor_tareas.eliminar_tarea("usuario_inexistente", "Cualquier tarea", gestor)

def test_eliminar_tarea_no_existe(gestor):
    gestor, gestor_tareas = gestor
    with pytest.raises(ValueError, match="Tarea no encontrada"):
        gestor_tareas.eliminar_tarea("juan23", "Tarea inexistente", gestor)

def test_eliminar_tarea_no_pertenece(gestor):
    gestor, gestor_tareas = gestor
    with pytest.raises(ValueError, match="No puedes eliminar una tarea que no te pertenece"):
        gestor_tareas.eliminar_tarea("maria99", "Ejercicio", gestor)

# 🟡 Casos Extremos
def test_eliminar_tarea_texto_maximo(gestor):
    gestor, gestor_tareas = gestor
    nombre_largo = "A" * 255
    gestor_tareas.crear_tarea("juan23", nombre_largo, "Trabajo", "Por hacer", gestor)
    gestor_tareas.eliminar_tarea("juan23", nombre_largo, gestor)
    assert not any(t.txt_tarea == nombre_largo for t in gestor.usuarios["juan23"].tareas)

def test_eliminar_tarea_categoria_maxima(gestor):
    gestor, gestor_tareas = gestor
    nombre_largo = "Tarea con nombre largo de 50 caracteres"
    gestor_tareas.crear_tarea("maria99", nombre_largo, "Trabajo", "Por hacer", gestor)
    gestor_tareas.eliminar_tarea("maria99", nombre_largo, gestor)
    assert not any(t.txt_tarea == nombre_largo for t in gestor.usuarios["maria99"].tareas)

def test_eliminar_tarea_ultima(gestor):
    gestor, gestor_tareas = gestor
    gestor_tareas.eliminar_tarea("usr", "Ejercicio", gestor)
    assert len(gestor.usuarios["usr"].tareas) == 0

