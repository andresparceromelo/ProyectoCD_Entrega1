import pytest
from src.main import GestorUsuario


@pytest.fixture
def gestor():
    gestor = GestorUsuario()
    gestor.crear_cuenta("juan23", "abc12345")
    gestor.crear_cuenta("maria99", "pass98765")
    gestor.crear_cuenta("usr", "abc45678")
    return gestor

# 🟢 Casos Normales
def test_iniciar_sesion_normal_1(gestor):
    assert gestor.iniciar_sesion("juan23", "abc12345") == "Inicio de sesión exitoso"

def test_iniciar_sesion_normal_2(gestor):
    assert gestor.iniciar_sesion("maria99", "pass98765") == "Inicio de sesión exitoso"

def test_iniciar_sesion_normal_3(gestor):
    assert gestor.iniciar_sesion("usr", "abc45678") == "Inicio de sesión exitoso"

# 🔴 Casos de Error
def test_iniciar_sesion_usuario_no_existe(gestor):
    with pytest.raises(ValueError, match="Usuario no encontrado"):
        gestor.iniciar_sesion("usuario_inexistente", "pass12345")

def test_iniciar_sesion_contraseña_incorrecta(gestor):
    with pytest.raises(ValueError, match="Contraseña incorrecta"):
        gestor.iniciar_sesion("juan23", "contraseñaIncorrecta")

def test_iniciar_sesion_credenciales_vacias(gestor):
    with pytest.raises(ValueError, match="Credenciales inválidas"):
        gestor.iniciar_sesion("", "")

# 🟡 Casos Extremos
def test_iniciar_sesion_usuario_maximo(gestor):
    usuario_extremo = "A" * 50
    with pytest.raises(ValueError, match="Usuario no encontrado"):
        gestor.iniciar_sesion(usuario_extremo, "pass12345")

def test_iniciar_sesion_contraseña_maxima(gestor):
    contraseña_extrema = "B" * 50
    with pytest.raises(ValueError, match="Contraseña incorrecta"):
        gestor.iniciar_sesion("juan23", contraseña_extrema)

def test_iniciar_sesion_usuario_minimo(gestor):
    assert gestor.iniciar_sesion("usr", "abc45678") == "Inicio de sesión exitoso"
