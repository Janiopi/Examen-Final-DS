#!/bin/bash

function analizar( ){
    # Simula el análisis de un archivo y devuelve un código de estado basado en el argumento proporcionado.
    # Argumento $1: Puede ser "problem", "error", "error_with_problem" o vacío.
    # Si no se proporciona ningún argumento, se asume que no hay problemas.

# Exit 0: No se encontró ningún problema
    if [ -z "$1" ]; then
        echo "exit status 0"
        return 0
    fi
# Exit 1: Se encontró un problema
    if [ "$1" == "problem" ]; then
        echo "exit status 1"
        return 1
# Exit 2: Error al analizar el archivo
    elif [ "$1" == "error" ]; then
        echo "exit status 2"
        return 2
    fi
# Exit 3: Error al analizar el archivo, pero se detectó un problema (Este lo estoy considerando como caso limite)
    elif [ "$1" == "error_with_problem" ]; then
        echo "exit status 3"
        return 3
    fi

}
        