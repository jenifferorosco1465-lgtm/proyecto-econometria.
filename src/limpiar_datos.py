from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

INPUT = ROOT / "data" / "processed" / "modelo_laboral.csv"
OUTPUT = ROOT / "data" / "processed" / "modelo_limpio.csv"

if not INPUT.exists():
    raise FileNotFoundError(
        f"No se encontró {INPUT}. "
        "Primero debe existir la base procesada modelo_laboral.csv."
    )

df = pd.read_csv(INPUT)

required = [
    "trabaja",
    "hombre",
    "EDAD",
    "edad2",
    "urbano"
]

missing = [v for v in required if v not in df.columns]

if missing:
    raise ValueError(f"Faltan variables requeridas: {missing}")

antes = len(df)

df = df.dropna(subset=required).copy()

# Eliminar edades imposibles
df = df[(df["EDAD"] >= 0) & (df["EDAD"] <= 100)].copy()

df.to_csv(OUTPUT, index=False)

print("Limpieza completada.")
print("Observaciones antes:", antes)
print("Observaciones después:", len(df))
print("Archivo generado:", OUTPUT)
