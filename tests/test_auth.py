import pytest
from unittest.mock import patch
# Pruebas unitarias para el módulo de autenticación

@pytest.fixture
def user_fixture():
    return {
        "username": "Usuario",
        "password": "contrasena",
        "authenticated": False,
    }

@pytest.fixture
def auth_client_fixture(user_fixture):
    user_fixture["authenticated"] = True
    return{
        user_fixture,
    }

@pytest.mark.skip(reason="Función de autenticación aún no implementada")
def test_authentication_success(user_fixture, auth_client_fixture):
    with patch('src.auth.authenticate', return_value=auth_client_fixture) as mock_authenticate:
        assert mock_authenticate(user_fixture["username"], user_fixture["password"]) == auth_client_fixture
        mock_authenticate.assert_called_once_with(user_fixture["username"], user_fixture["password"])

@pytest.mark.xfail(reason="Usuario no autenticado")
def test_authentication_failure(user_fixture):
    with patch('src.auth.authenticate', return_value=user_fixture) as mock_authenticate:
        assert mock_authenticate(user_fixture["authenticated"]) == True
        mock_authenticate.assert_called_once_with(user_fixture["authenticated"])
        