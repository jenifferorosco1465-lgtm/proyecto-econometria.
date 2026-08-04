from pathlib import Path
import pandas as pd
import statsmodels.formula.api as smf

ROOT = Path(__file__).resolve().parents[1]

INPUT = ROOT / "data" / "processed" / "modelo_limpio.csv"
TABLES = ROOT / "outputs" / "tables"

TABLES.mkdir(parents=True, exist_ok=True)

if not INPUT.exists():
    raise FileNotFoundError(
        f"No se encontró {INPUT}. "
        "Ejecute primero el proceso de limpieza."
    )

df = pd.read_csv(INPUT)

formula = "trabaja ~ hombre + EDAD + edad2 + urbano"

print("Estimando Logit...")
logit = smf.logit(formula, data=df).fit(disp=False)

print("Estimando Probit...")
probit = smf.probit(formula, data=df).fit(disp=False)

# Efectos marginales promedio
logit_marg = logit.get_margeff(at="overall").summary_frame()
probit_marg = probit.get_margeff(at="overall").summary_frame()

logit_marg.to_csv(
    TABLES / "efectos_marginales_logit.csv"
)

probit_marg.to_csv(
    TABLES / "efectos_marginales_probit.csv"
)

# Comparación
comparacion = pd.DataFrame({
    "Modelo": ["Logit", "Probit"],
    "AIC": [logit.aic, probit.aic],
    "BIC": [logit.bic, probit.bic],
    "Pseudo_R2": [
        logit.prsquared,
        probit.prsquared
    ]
})

comparacion.to_csv(
    TABLES / "comparacion_modelos.csv",
    index=False
)

# Coeficientes Logit
pd.DataFrame({
    "variable": logit.params.index,
    "coeficiente": logit.params.values,
    "p_valor": logit.pvalues.values
}).to_csv(
    TABLES / "resultados_logit.csv",
    index=False
)

# Coeficientes Probit
pd.DataFrame({
    "variable": probit.params.index,
    "coeficiente": probit.params.values,
    "p_valor": probit.pvalues.values
}).to_csv(
    TABLES / "resultados_probit.csv",
    index=False
)

print("")
print("=" * 60)
print("MODELOS ESTIMADOS")
print("=" * 60)

print(logit.summary())

print("")
print(probit.summary())

print("")
print("EFECTOS MARGINALES PROMEDIO - LOGIT")
print(logit_marg)

print("")
print("EFECTOS MARGINALES PROMEDIO - PROBIT")
print(probit_marg)

print("")
print("COMPARACIÓN")
print(comparacion)
