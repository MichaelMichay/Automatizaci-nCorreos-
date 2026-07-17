import pytest
from src.clasificador import clasificar_correo, extraer_prioridad


def test_clasificar_soporte():
    assert clasificar_correo("Error en el sistema", "no funciona nada") == "soporte"


def test_clasificar_ventas():
    assert clasificar_correo("Consulta de precio", "quiero cotizacion") == "ventas"


def test_clasificar_reclamo():
    assert clasificar_correo("Queja", "estoy muy molesto con el servicio") == "reclamo"


def test_clasificar_informacion():
    assert clasificar_correo("Duda", "cual es el horario de atencion") == "informacion"


def test_clasificar_general():
    assert clasificar_correo("Saludos", "solo queria saludar") == "general"


def test_clasificar_sin_contenido_lanza_excepcion():
    with pytest.raises(ValueError):
        clasificar_correo("", "")


def test_prioridad_alta():
    assert extraer_prioridad("Esto es urgente, necesito ayuda ya mismo") == "alta"


def test_prioridad_normal():
    assert extraer_prioridad("Quisiera saber el horario") == "normal"


def test_prioridad_cuerpo_none_lanza_excepcion():
    with pytest.raises(ValueError):
        extraer_prioridad(None)
