import subprocess


def test_app_e2e():
    resultado = subprocess.run(
        ["python", "app.py"],
        capture_output=True,
        text=True,
    )

    assert "Bienvenido al sistema de automatizacion" in resultado.stdout
    assert "Respuesta generada:" in resultado.stdout
    assert "Dato recuperado del historial:" in resultado.stdout
    assert "Final de la ejecucion del flujo" in resultado.stdout
