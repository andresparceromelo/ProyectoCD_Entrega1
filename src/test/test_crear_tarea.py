import pytest
from src.main import GestorTarea, GestorUsuario

@pytest.fixture
def gestor():
    gestor = GestorUsuario()
    gestor.crear_cuenta("juan23", "abc12345")
    gestor.crear_cuenta("maria99", "pass98765")
    gestor.crear_cuenta("usr", "abc45678")
    return gestor

@pytest.fixture
def gestor_tareas():
    return GestorTarea()

# 🟢 Casos Normales
def test_crear_tarea_normal_1(gestor, gestor_tareas):
    gestor_tareas.crear_tarea("juan23", "Comprar comida", "Personal", "Por hacer", gestor)
    assert len(gestor.usuarios["juan23"].tareas) == 1

def test_crear_tarea_normal_2(gestor, gestor_tareas):
    gestor_tareas.crear_tarea("maria99", "Revisar reporte", "Trabajo", "En progreso", gestor)
    assert len(gestor.usuarios["maria99"].tareas) == 1

def test_crear_tarea_normal_3(gestor, gestor_tareas):
    gestor_tareas.crear_tarea("usr", "Ir al gimnasio", "Salud", "Completada", gestor)
    assert len(gestor.usuarios["usr"].tareas) == 1

# 🔴 Casos de Error
def test_crear_tarea_usuario_no_existe(gestor, gestor_tareas):
    with pytest.raises(ValueError, match="Usuario no encontrado"):
        gestor_tareas.crear_tarea("usuario_inexistente", "Nueva tarea", "Trabajo", "Por hacer", gestor)

def test_crear_tarea_texto_vacio(gestor, gestor_tareas):
    with pytest.raises(ValueError, match="El texto de la tarea no puede estar vacío"):
        gestor_tareas.crear_tarea("juan23", "", "Personal", "Por hacer", gestor)

def test_crear_tarea_categoria_vacia(gestor, gestor_tareas):
    with pytest.raises(ValueError, match="Debe especificar una categoría"):
        gestor_tareas.crear_tarea("maria99", "Leer libro", "", "Por hacer", gestor)

# 🟡 Casos Extremos
def test_crear_tarea_texto_maximo(gestor, gestor_tareas):
    texto_largo = "A" * 255
    gestor_tareas.crear_tarea("juan23", texto_largo, "Trabajo", "Por hacer", gestor)
    assert len(gestor.usuarios["juan23"].tareas) == 1

def test_crear_tarea_categoria_maxima(gestor, gestor_tareas):
    categoria_larga = "x" * 50
    gestor_tareas.crear_tarea("maria99", "Comprar leche", categoria_larga, "Completada", gestor)
    assert len(gestor.usuarios["maria99"].tareas) == 1

def test_crear_tarea_estado_maximo(gestor, gestor_tareas):
    estado_largo = "x" * 20
    gestor_tareas.crear_tarea("usr", "Estudiar", "Educación", estado_largo, gestor)
    assert len(gestor.usuarios["usr"].tareas) == 1

