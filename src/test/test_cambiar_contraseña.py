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
def test_cambiar_contraseña_normal_1(gestor):
    gestor.cambiar_contraseña("juan23", "newpass99")
    assert gestor.usuarios["juan23"].contraseña == "newpass99"

def test_cambiar_contraseña_normal_2(gestor):
    gestor.cambiar_contraseña("maria99", "secure4567")
    assert gestor.usuarios["maria99"].contraseña == "secure4567"

def test_cambiar_contraseña_normal_3(gestor):
    gestor.cambiar_contraseña("usr", "zxcvbn789")
    assert gestor.usuarios["usr"].contraseña == "zxcvbn789"

# 🔴 Casos de Error
def test_cambiar_contraseña_incorrecta(gestor):
    with pytest.raises(ValueError, match="Contraseña actual incorrecta"):
        gestor.cambiar_contraseña("juan23", "incorrecta")

def test_cambiar_contraseña_usuario_no_existe(gestor):
    with pytest.raises(ValueError, match="Usuario no encontrado"):
        gestor.cambiar_contraseña("usuario_inexistente", "newpass99")

def test_cambiar_contraseña_sin_numeros(gestor):
    with pytest.raises(ValueError, match="La contraseña debe tener al menos 7 caracteres y 2 números"):
        gestor.cambiar_contraseña("maria99", "abcdefg")

# 🟡 Casos Extremos
def test_cambiar_contraseña_usuario_largo(gestor):
    gestor.crear_cuenta("usuario_muy_muy_largo_12345", "longpass99")
    gestor.cambiar_contraseña("usuario_muy_muy_largo_12345", "88NewPass")
    assert gestor.usuarios["usuario_muy_muy_largo_12345"].contraseña == "88NewPass"

def test_cambiar_contraseña_solo_numeros(gestor):
    gestor.cambiar_contraseña("usr", "87654321")
    assert gestor.usuarios["usr"].contraseña == "87654321"

def test_cambiar_contraseña_minima_valida(gestor):
    gestor.cambiar_contraseña("maria99", "abc99999")
    assert gestor.usuarios["maria99"].contraseña == "abc99999"
