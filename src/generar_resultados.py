from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]

INPUT = ROOT / "data" / "processed" / "modelo_limpio.csv"
FIGURES = ROOT / "outputs" / "figures"

FIGURES.mkdir(parents=True, exist_ok=True)

if not INPUT.exists():
    raise FileNotFoundError(
        f"No se encontró {INPUT}."
    )

df = pd.read_csv(INPUT)

print("Observaciones:", len(df))
print("Variables:", list(df.columns))

# Edad
edad = df.groupby("EDAD")["trabaja"].mean()

plt.figure(figsize=(8, 5))
edad.plot()
plt.xlabel("Edad")
plt.ylabel("Proporción que trabaja")
plt.title("Probabilidad observada de trabajar según edad")
plt.tight_layout()
plt.savefig(
    FIGURES / "probabilidad_edad.png",
    dpi=300
)
plt.close()

# Sexo
sexo = df.groupby("hombre")["trabaja"].mean()

plt.figure(figsize=(7, 5))
sexo.plot(kind="bar")
plt.xlabel("Hombre (1 = sí)")
plt.ylabel("Proporción que trabaja")
plt.title("Probabilidad observada de trabajar según sexo")
plt.tight_layout()
plt.savefig(
    FIGURES / "probabilidad_sexo.png",
    dpi=300
)
plt.close()

# Área
area = df.groupby("urbano")["trabaja"].mean()

plt.figure(figsize=(7, 5))
area.plot(kind="bar")
plt.xlabel("Urbano (1 = sí)")
plt.ylabel("Proporción que trabaja")
plt.title("Probabilidad observada de trabajar según área")
plt.tight_layout()
plt.savefig(
    FIGURES / "probabilidad_area.png",
    dpi=300
)
plt.close()

print("Gráficos generados correctamente.")
