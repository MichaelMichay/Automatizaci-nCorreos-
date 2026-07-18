from src.almacenamiento import guardar_respuesta, obtener_respuesta, historial


def test_guardar_respuesta():
    historial.clear()
    guardar_respuesta("correo_1", "soporte", "respuesta de prueba")
    assert "correo_1" in historial
    assert historial["correo_1"]["categoria"] == "soporte"


def test_obtener_respuesta_existente():
    historial.clear()
    guardar_respuesta("correo_1", "ventas", "respuesta de venta")
    dato = obtener_respuesta("correo_1")
    assert dato["categoria"] == "ventas"


def test_obtener_respuesta_inexistente():
    historial.clear()
    dato = obtener_respuesta("correo_inexistente")
    assert dato == "No se encontraron datos para el correo especificado."
