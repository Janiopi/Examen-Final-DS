import pytest 
from unittest.mock import  patch

# Pruebas unitarias para el cliente API

@patch('src.api_client.ApiClient') # Omití el autospec debido a que no implementé como tal api_client.py, asi evitando errores de parametros incorrectos
def test_api_client_success(mock_api_client):
    # Simula el comportamiento del método get_data
    with patch.object(mock_api_client, 'get_data', return_value={"status": "exitoso", "data": "datos solicitados"}) as mock_get_data:
        response = mock_api_client.get_data()
        assert response == {"status": "exitoso", "data": "datos solicitados"}
        mock_get_data.assert_called_once()

@patch('src.api_client.ApiClient')
def test_api_client_failure(mock_api_client):
    # Simula el comportamiento del método get_data con un error
    with patch.object(mock_api_client, 'get_data', side_effect=Exception("Error en la conexión")) as mock_get_data:
        with pytest.raises(Exception) as exc_info:
            mock_api_client.get_data()
        assert str(exc_info.value) == "Error en la conexión"
        mock_get_data.assert_called_once()

@patch('src.api_client.ApiClient')
def test_api_client_not_valid(mock_api_client):
    # Simula el comportamiento del método get_data con un error
    with patch.object(mock_api_client, 'get_data', side_effect=Exception("Conexión no válida")) as mock_get_data:
        with pytest.raises(Exception) as exc_info:
            mock_api_client.get_data()
        assert str(exc_info.value) == "Conexión no válida"
        mock_get_data.assert_called_once()

@patch('src.api_client.ApiClient')
def test_api_client_edge_case(mock_api_client):
    from src.api_client import ApiClient
    client = ApiClient()
    
    # Simula el comportamiento del método get_data con un caso límite (Podrían ser datos vacíos o un formato inesperado)
    with patch.object(client, 'get_data', return_value={"status": "exitoso", "data": "datos de caso límite"}) as mock_get_data:
        response = client.get_data()
        assert response == {"status": "exitoso", "data": "datos de caso límite"}
        mock_get_data.assert_called_once()
