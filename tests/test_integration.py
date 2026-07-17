from app import procesar_correo
from src.almacenamiento import obtener_respuesta, historial


def test_procesar_correo_integracion():
    historial.clear()
    respuesta = procesar_correo(
        "correo_test", "Reclamo urgente", "estoy molesto, esto es urgente"
    )
    assert "PRIORIDAD ALTA" in respuesta

    guardado = obtener_respuesta("correo_test")
    assert guardado["categoria"] == "reclamo"
    assert guardado["respuesta"] == respuesta
