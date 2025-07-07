# Examen Final DS 2025-1

## Ejercicio 1
- Creación de script `fake-analyzer.sh`: Este script tiene una lógica básica, dependiendo del argumento recibido, nos devolverá un código `exit status`
    - 0: Exito
    - 1: Operación no permitida
    - 2: Archivo/directorio no existente, etc

- Pruebas unitarias de `test_analyzer.py`: Mockeamos el comportamiento del analyzer (Porque no es necesario utilizar el original, y tampoco está implementado). Gracias al mock, tenemos control sobre el output de analyzer.analyze  y podemos evaluar varias situaciones.
    - Análisis exitoso (exit 0)
    - Error en el análisis (exit 1)
    - Argumento inválido (exit 2)

- Mocks de API: 
    - Del mismo modo que con el test_analyzer, se utilizan mocks para simular `get_data` de `api_client`
    - Se omitió el uso de `create_autospec=True`debido a que no implementé `api_client`, por lo que me daría error al momento de ejecutar tests al no haber una estructura definida (parámetros incorrectos)
    - Se utilizan los `fixtures` para simular data de usuario antes de ejecutar los tests, en `test_auth`. 

## Ejercicio 2

## Ejercicio 3

