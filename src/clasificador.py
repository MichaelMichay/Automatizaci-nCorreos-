"""
Modulo de clasificacion de correos electronicos.
Analiza el asunto/cuerpo de un correo y determina su categoria
para poder asignarle una respuesta automatica adecuada.
"""

CATEGORIAS = {
    "soporte": ["error", "falla", "problema", "no funciona", "ayuda"],
    "ventas": ["precio", "cotizacion", "comprar", "producto", "oferta"],
    "reclamo": ["queja", "reclamo", "insatisfecho", "molesto", "devolucion"],
    "informacion": ["informacion", "consulta", "duda", "horario", "contacto"],
}


def clasificar_correo(asunto: str, cuerpo: str) -> str:
    """
    Clasifica un correo en una de las categorias definidas.

    Args:
        asunto: asunto del correo.
        cuerpo: cuerpo/mensaje del correo.

    Returns:
        Nombre de la categoria detectada, o "general" si no coincide
        con ninguna palabra clave.

    Raises:
        ValueError: si asunto y cuerpo estan vacios.
    """
    if not asunto and not cuerpo:
        raise ValueError("El correo no contiene asunto ni cuerpo para analizar")

    texto = f"{asunto} {cuerpo}".lower()

    for categoria, palabras_clave in CATEGORIAS.items():
        if any(palabra in texto for palabra in palabras_clave):
            return categoria

    return "general"


def extraer_prioridad(cuerpo: str) -> str:
    """
    Determina la prioridad del correo segun palabras de urgencia.

    Returns:
        "alta" si detecta urgencia, "normal" en caso contrario.
    """
    if cuerpo is None:
        raise ValueError("El cuerpo del correo no puede ser None")

    urgentes = ["urgente", "inmediato", "ya mismo", "emergencia"]
    texto = cuerpo.lower()
    return "alta" if any(palabra in texto for palabra in urgentes) else "normal"
