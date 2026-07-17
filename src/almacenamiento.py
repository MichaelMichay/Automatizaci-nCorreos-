"""
Modulo de almacenamiento: guarda el historial de correos procesados
y las respuestas generadas (simulacion de base de datos en memoria).
"""

historial = {}


def guardar_respuesta(id_correo: str, categoria: str, respuesta: str) -> None:
    """Guarda el resultado del procesamiento de un correo."""
    if not id_correo:
        raise ValueError("El id_correo no puede estar vacio")

    historial[id_correo] = {
        "categoria": categoria,
        "respuesta": respuesta,
    }


def obtener_respuesta(id_correo: str):
    """Recupera el resultado guardado para un id_correo dado."""
    return historial.get(
        id_correo, "No se encontraron datos para el correo especificado."
    )
