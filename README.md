# Automatización de Respuestas a Correos Electrónicos

Trabajo Práctico Experimental — Módulo Automatización de Software (UNEMI Posgrados).

## Problemática seleccionada
Automatizar la clasificación y respuesta inicial de correos electrónicos
(soporte, ventas, reclamos, información general), evitando demoras
manuales en la primera respuesta al cliente.

## Estructura del proyecto
```
email_auto/
├── .github/workflows/python-ci.yml   # Pipeline CI (lint + pruebas + cobertura)
├── src/
│   ├── clasificador.py               # Clasifica el correo por categoría y prioridad
│   ├── generador_respuestas.py       # Genera la respuesta automática según categoría
│   └── almacenamiento.py             # Guarda historial de correos procesados
├── tests/
│   ├── test_unit_*.py                # Pruebas unitarias
│   ├── test_integration.py           # Prueba de integración
│   ├── test_e2e.py                   # Prueba end-to-end (ejecuta app.py)
│   └── test_regression.py            # Prueba de regresión (casos históricos)
├── app.py                            # Punto de entrada del flujo
└── requirements.txt
```

## Flujo de ramas (Git)
- **main**: versión estable, protegida.
- **developer**: rama de trabajo diario del equipo.
- **staging**: rama de integración final, lista para despliegue.

Flujo obligatorio: trabajar en `developer` → push → pipeline se ejecuta
automáticamente (lint, pruebas, cobertura) → si todo pasa y el líder aprueba
→ merge a `staging`.

## Pipeline CI (GitHub Actions)
Etapas: instalación de dependencias → estilo (`flake8`) → pruebas (`pytest`)
→ cobertura (`coverage`, reporte HTML publicado como artefacto).

## Resultados obtenidos
- 18 pruebas ejecutadas, 18 exitosas.
- 0 errores de estilo (flake8).
- 91% de cobertura de código.

## Beneficios de la automatización
- Reduce el tiempo de primera respuesta al cliente.
- Estandariza el tono y contenido de las respuestas.
- Prioriza automáticamente los correos urgentes.

## Mejoras futuras
- Integrar con una API real de correo (IMAP/Gmail API).
- Usar un modelo de lenguaje para generar respuestas más personalizadas.
- Añadir panel de métricas (correos por categoría, tiempos de respuesta).
