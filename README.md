# Proyecto Econométrico: Factores asociados a la probabilidad de trabajar

## 1. Descripción del proyecto

Este proyecto econométrico analiza los factores asociados a la probabilidad de que una persona se encuentre trabajando, utilizando información de la Encuesta de Condiciones de Vida (ECV6R) del Ecuador.

Se estiman modelos de elección binaria **Logit y Probit**, utilizando como variable dependiente el indicador de participación laboral (`trabaja`) y como variables explicativas el sexo, la edad, la edad al cuadrado y el área de residencia.

El objetivo es identificar la relación entre estas características sociodemográficas y la probabilidad estimada de trabajar, además de comparar el desempeño de los modelos Logit y Probit.

---

## 2. Objetivo general

Analizar mediante modelos econométricos de elección binaria los factores asociados a la probabilidad de que una persona trabaje en Ecuador.

### Objetivos específicos

* Preparar y depurar la base de datos de la ECV6R.
* Construir la variable dependiente `trabaja`.
* Estimar un modelo Logit.
* Estimar un modelo Probit.
* Calcular efectos marginales promedio.
* Generar predicciones de probabilidad.
* Comparar los modelos mediante AIC, BIC y Pseudo R².
* Evaluar la capacidad predictiva mediante matriz de confusión y curva ROC.
* Interpretar económicamente los principales resultados.

---

## 3. Base de datos

La información utilizada corresponde a la base de personas de la **Encuesta de Condiciones de Vida (ECV6R)**.

La base original contiene **109.694 observaciones y 684 variables**.

Después del proceso de preparación y selección de las variables necesarias para la estimación, se obtuvo una muestra final de:

**85.919 observaciones.**

---

## 4. Variables utilizadas

### Variable dependiente

**trabaja**

* `1` = trabajó al menos una hora.
* `0` = no trabajó.

### Variables independientes

**hombre**

* `1` = hombre.
* `0` = mujer.

**EDAD**

Edad de la persona en años.

**edad2**

Edad al cuadrado, incorporada para capturar una posible relación no lineal entre edad y la probabilidad de trabajar.

**urbano**

* `1` = área urbana.
* `0` = área rural.

---

## 5. Modelos econométricos

Se estimaron dos modelos de elección binaria:

### Modelo Logit

El modelo Logit estima la probabilidad de que una persona trabaje en función del sexo, edad, edad al cuadrado y área de residencia.

### Modelo Probit

El modelo Probit utiliza las mismas variables explicativas y permite comprobar la estabilidad de los resultados obtenidos mediante Logit.

---

## 6. Resultados principales

### Comparación de modelos

| Modelo |       AIC |       BIC | Pseudo R² |
| ------ | --------: | --------: | --------: |
| Logit  | 83298.284 | 83345.090 |    0.2748 |
| Probit | 83326.118 | 83372.924 |    0.2745 |

El modelo Logit presenta valores ligeramente inferiores de AIC y BIC, por lo que se selecciona como modelo principal. Ambos modelos presentan un nivel de ajuste muy similar.

### Efectos marginales promedio del Logit

| Variable | Efecto marginal |
| -------- | --------------: |
| Hombre   |          0.2018 |
| Edad     |          0.0461 |
| Edad²    |         -0.0005 |
| Urbano   |         -0.1443 |

Todos los efectos marginales presentan significancia estadística con valores de p inferiores a 0.001.

El efecto marginal de `hombre` es positivo, indicando una diferencia promedio de aproximadamente 20,18 puntos porcentuales en la probabilidad estimada de trabajar entre hombres y mujeres, manteniendo constantes las demás variables.

El efecto marginal de `urbano` es negativo, indicando una diferencia promedio de aproximadamente 14,43 puntos porcentuales en la probabilidad estimada de trabajar para las personas del área urbana respecto al área rural, manteniendo constantes las demás variables.

La edad presenta un efecto positivo mientras que la edad al cuadrado presenta un efecto negativo. En conjunto, estos resultados sugieren una relación no lineal entre edad y probabilidad de trabajar: la probabilidad aumenta con la edad hasta cierto punto y posteriormente tiende a disminuir.

---

## 7. Capacidad predictiva

El modelo Logit obtuvo:

**AUC = 0.8341**

Este resultado indica una buena capacidad de discriminación del modelo entre las personas que trabajan y aquellas que no trabajan.

La matriz de confusión obtenida fue:

```text
[[21519 11912]
 [ 7746 44742]]
```

El modelo clasificó correctamente 66.261 de las 85.919 observaciones, equivalente aproximadamente al **77,1 %** de las observaciones.

---

## 8. Gráficos generados

El proyecto genera los siguientes gráficos:

* Curva ROC del modelo Logit.
* Probabilidad estimada de trabajar según edad.
* Probabilidad estimada de trabajar según sexo.
* Probabilidad estimada de trabajar según área de residencia.

Los gráficos se encuentran en:

```text
outputs/figures/
```

---

## 9. Archivos de resultados

Los principales resultados generados son:

```text
outputs/
├── figures/
│   ├── roc_logit.png
│   ├── probabilidad_edad.png
│   ├── probabilidad_sexo.png
│   └── probabilidad_area.png
│
├── tables/
│   ├── comparacion_modelos.csv
│   └── coeficientes_logit_probit.csv
│
└── results/
    └── predicciones.csv
```

---

## 10. Estructura del proyecto

```text
Proyecto de econometria/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_exploracion.ipynb
│   ├── 02_limpieza.ipynb
│   └── 02_modelo.ipynb
│
├── outputs/
│   ├── figures/
│   ├── tables/
│   └── results/
│
├── README.md
└── .venv/
```

---

## 11. Tecnologías utilizadas

* Python
* Pandas
* NumPy
* Statsmodels
* Scikit-learn
* Matplotlib
* Jupyter Notebook
* VS Code

---

## 12. Conclusión

Los resultados muestran que las características sociodemográficas incluidas en el modelo presentan una asociación estadísticamente significativa con la probabilidad de trabajar.

El modelo Logit fue seleccionado como modelo principal debido a sus menores valores de AIC y BIC frente al modelo Probit. Además, el AUC de 0.8341 evidencia una buena capacidad de discriminación.

Los resultados de Logit y Probit son consistentes entre sí, lo que proporciona mayor estabilidad a las conclusiones obtenidas.

En términos generales, el análisis permite identificar diferencias importantes asociadas al sexo, edad y área de residencia en la probabilidad estimada de trabajar.

