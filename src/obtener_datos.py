"""
Obtención y documentación de los datos.

Fuente:
Instituto Nacional de Estadística y Censos (INEC).

Base:
Encuesta de Condiciones de Vida ECV6R.

La base original no se incorpora al repositorio cuando existen
restricciones de tamaño o distribución. El usuario debe obtenerla
desde la fuente oficial y colocar los archivos originales en:

data/raw/

Posteriormente se genera la base procesada utilizada por el modelo.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"

print("Fuente: INEC - Encuesta de Condiciones de Vida ECV6R")
print("Directorio esperado:", RAW)

if RAW.exists():
    print("Directorio data/raw encontrado.")
else:
    print("Crear data/raw y colocar allí los archivos originales.")
