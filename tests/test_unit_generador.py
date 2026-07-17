import pytest
from src.generador_respuestas import generar_respuesta


def test_generar_respuesta_soporte():
    respuesta = generar_respuesta("soporte")
    assert "equipo tecnico" in respuesta


def test_generar_respuesta_prioridad_alta():
    respuesta = generar_respuesta("reclamo", prioridad="alta")
    assert respuesta.startswith("[PRIORIDAD ALTA]")


def test_generar_respuesta_categoria_invalida():
    with pytest.raises(KeyError):
        generar_respuesta("categoria_inexistente")
