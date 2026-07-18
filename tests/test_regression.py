from src.clasificador import clasificar_correo

# Casos historicos que deben mantener su clasificacion esperada
# a pesar de futuros cambios en el modulo clasificador.
CASOS_REGRESION = [
    ("Error en el sistema", "no funciona el login", "soporte"),
    ("Cotizacion", "quiero saber el precio del producto", "ventas"),
    ("Queja formal", "estoy insatisfecho con el servicio", "reclamo"),
    ("Consulta general", "cual es el horario de atencion", "informacion"),
]


def test_regression_clasificacion():
    for asunto, cuerpo, esperado in CASOS_REGRESION:
        resultado = clasificar_correo(asunto, cuerpo)
        assert resultado == esperado, (
            f"Regresion detectada: '{asunto}' se clasifico como "
            f"'{resultado}' en vez de '{esperado}'"
        )
