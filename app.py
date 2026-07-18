from src.clasificador import clasificar_correo, extraer_prioridad
from src.generador_respuestas import generar_respuesta
from src.almacenamiento import guardar_respuesta, obtener_respuesta


def procesar_correo(id_correo: str, asunto: str, cuerpo: str) -> str:
    """Procesa un correo: clasifica, genera respuesta y la almacena."""
    categoria = clasificar_correo(asunto, cuerpo)
    prioridad = extraer_prioridad(cuerpo)
    respuesta = generar_respuesta(categoria, prioridad)
    guardar_respuesta(id_correo, categoria, respuesta)
    return respuesta


def ejecutar_flujo():
    print("Bienvenido al sistema de automatizacion de respuestas de correo")

    correo_id = "correo_001"
    asunto = "Problema urgente con mi pedido"
    cuerpo = "Tengo un error urgente, el producto no funciona."

    respuesta = procesar_correo(correo_id, asunto, cuerpo)
    print(f"Respuesta generada: {respuesta}")

    guardado = obtener_respuesta(correo_id)
    print(f"Dato recuperado del historial: {guardado}")
    print("Final de la ejecucion del flujo")


if __name__ == "__main__":
    ejecutar_flujo()
