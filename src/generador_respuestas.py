"""
Modulo de generacion de respuestas automaticas para correos electronicos,
segun la categoria y prioridad detectadas por el clasificador.
"""

PLANTILLAS = {
    "soporte": (
        "Hola, hemos recibido tu reporte y nuestro equipo tecnico "
        "lo revisara a la brevedad. Te contactaremos con una solucion."
    ),
    "ventas": (
        "Gracias por tu interes. Un asesor comercial te enviara "
        "la cotizacion y detalles del producto en breve."
    ),
    "reclamo": (
        "Lamentamos el inconveniente. Tu reclamo ha sido registrado "
        "y sera atendido de forma prioritaria por nuestro equipo."
    ),
    "informacion": (
        "Gracias por escribirnos. Adjuntamos la informacion solicitada "
        "y quedamos atentos a cualquier otra consulta."
    ),
    "general": (
        "Gracias por contactarnos. Hemos recibido tu mensaje y "
        "te responderemos a la brevedad posible."
    ),
}


def generar_respuesta(categoria: str, prioridad: str = "normal") -> str:
    """
    Genera el texto de respuesta automatica segun la categoria del correo.

    Args:
        categoria: categoria devuelta por clasificar_correo().
        prioridad: "alta" o "normal".

    Returns:
        Texto de la respuesta automatica.

    Raises:
        KeyError: si la categoria no existe en las plantillas.
    """
    if categoria not in PLANTILLAS:
        raise KeyError(f"Categoria no reconocida: {categoria}")

    respuesta = PLANTILLAS[categoria]

    if prioridad == "alta":
        respuesta = "[PRIORIDAD ALTA] " + respuesta

    return respuesta
