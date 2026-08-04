FACTORES ASOCIADOS A LA PROBABILIDAD DE TRABAJAR EN ECUADOR: UNA APLICACIÓN DE MODELOS LOGIT Y PROBIT

Autora: Jeniffer Orosco
Universidad Técnica de Cotopaxi
Carrera: Economía
Asignatura: Econometría

Repositorio GitHub: [PEGAR AQUÍ EL ENLACE REAL DE GITHUB]
Dashboard en Vercel: [PEGAR AQUÍ EL ENLACE REAL DE VERCEL]

Resumen

El presente estudio analiza los factores asociados con la probabilidad de que una persona se encuentre trabajando en Ecuador mediante modelos econométricos de respuesta binaria Logit y Probit. Para ello, se utiliza información de la Encuesta de Condiciones de Vida, Sexta Ronda (ECV6R), elaborada por el Instituto Nacional de Estadística y Censos (INEC). La variable dependiente es trabaja, mientras que las variables explicativas consideradas son sexo, edad, edad al cuadrado y área de residencia.

Después del proceso de depuración se utilizaron 85.950 observaciones. Los resultados muestran que el modelo Logit presenta un Pseudo R² de 0,2748, mientras que el Probit alcanza 0,2745. Los efectos marginales promedio del modelo Logit indican una asociación positiva entre ser hombre y la probabilidad de trabajar de aproximadamente 20,17 puntos porcentuales. La edad presenta un efecto positivo, aunque su término cuadrático negativo indica una relación no lineal. Por otra parte, residir en el área urbana presenta una asociación negativa de aproximadamente 14,43 puntos porcentuales.

En términos predictivos, el modelo Logit alcanza un AUC de 0,8341 y una exactitud de clasificación de 0,7713. Los resultados deben interpretarse como asociaciones estadísticas y no como efectos causales, debido principalmente a las características observacionales de los datos y a las limitaciones relacionadas con el diseño muestral.

Palabras clave: empleo, mercado laboral, Logit, Probit, efectos marginales, Ecuador.

1. Introducción

El mercado laboral constituye un componente fundamental para comprender las condiciones económicas y sociales de una población. La posibilidad de encontrarse trabajando puede estar relacionada con características individuales y territoriales, entre ellas el sexo, la edad y el área de residencia.

En Ecuador, la Encuesta de Condiciones de Vida (ECV) constituye una fuente importante de información para estudiar diferentes dimensiones del bienestar de los hogares y de las personas. La Sexta Ronda de la ECV fue diseñada para analizar las condiciones de vida y las relaciones entre distintos aspectos económicos y sociales de la población ecuatoriana (INEC, 2014).

La literatura económica ha utilizado modelos de respuesta binaria para estudiar decisiones y resultados laborales cuando la variable dependiente solamente puede tomar dos valores. En estos casos, los modelos Logit y Probit permiten estimar probabilidades condicionadas a un conjunto de características observables.

En este contexto, el presente trabajo estudia los factores asociados con la probabilidad de trabajar en Ecuador mediante modelos Logit y Probit, utilizando información de la ECV6R.

2. Pregunta de investigación

¿Qué factores se encuentran asociados con la probabilidad de que una persona se encuentre trabajando en Ecuador?

3. Objetivos
3.1 Objetivo general

Analizar los factores asociados con la probabilidad de trabajar en Ecuador mediante modelos econométricos de respuesta binaria Logit y Probit.

3.2 Objetivos específicos
Identificar la relación estadística entre sexo, edad y área de residencia y la condición laboral.
Estimar un modelo Logit y un modelo Probit para la variable dependiente trabaja.
Calcular e interpretar los efectos marginales promedio.
Comparar el desempeño de los modelos Logit y Probit.
Evaluar la capacidad predictiva del modelo Logit mediante AUC, accuracy y matriz de confusión.
Analizar posibles problemas de multicolinealidad mediante el Factor de Inflación de la Varianza (VIF).
4. Marco teórico

Cuando la variable dependiente es binaria, los modelos tradicionales de regresión lineal no siempre son apropiados para representar una probabilidad. Los modelos Logit y Probit permiten modelar la probabilidad de ocurrencia de un determinado resultado utilizando funciones de distribución no lineales.

En el modelo Logit, la probabilidad condicionada se representa mediante una función logística. En el modelo Probit se utiliza la función de distribución acumulada normal estándar. Ambos modelos permiten obtener probabilidades estimadas entre cero y uno.

Una característica importante de estos modelos es que los coeficientes estimados no representan directamente cambios en la probabilidad. Por esta razón, para facilitar la interpretación económica se calculan efectos marginales. Los efectos marginales promedio permiten resumir el cambio promedio en la probabilidad asociada con una variación en cada variable explicativa.

La utilización conjunta de Logit y Probit permite comprobar si las conclusiones generales se mantienen bajo dos especificaciones ampliamente utilizadas para variables dependientes binarias.

5. Datos y variables
5.1 Fuente de información

La fuente utilizada es la Encuesta de Condiciones de Vida, Sexta Ronda (ECV6R) del Instituto Nacional de Estadística y Censos (INEC).

La ECV es una encuesta multipropósito que recoge información relacionada con diferentes dimensiones del bienestar y las condiciones de vida de la población. La documentación oficial de la Sexta Ronda señala que la encuesta permite analizar factores económicos y sociales relacionados con las condiciones de vida de los hogares y las personas.

5.2 Variable dependiente

La variable dependiente es:

trabaja: variable binaria que toma el valor:

1 = la persona trabaja.
0 = la persona no trabaja.
5.3 Variables independientes

Las variables utilizadas son:

Variable	Descripción
hombre	1 = hombre; 0 = mujer
EDAD	Edad de la persona en años
edad2	Edad al cuadrado
urbano	1 = área urbana; 0 = área rural
FEXP	Factor de expansión de la encuesta

La variable edad2 se incorpora para representar una posible relación no lineal entre edad y probabilidad de trabajar.

6. Metodología

Se estimaron dos modelos de respuesta binaria:

Modelo Logit:

P(trabajaᵢ = 1 | Xᵢ) = Λ(β₀ + β₁hombreᵢ + β₂EDADᵢ + β₃edad2ᵢ + β₄urbanoᵢ)

donde Λ representa la función logística.

Modelo Probit:

P(trabajaᵢ = 1 | Xᵢ) = Φ(β₀ + β₁hombreᵢ + β₂EDADᵢ + β₃edad2ᵢ + β₄urbanoᵢ)

donde Φ representa la función de distribución acumulada normal estándar.

Los modelos fueron estimados mediante máxima verosimilitud utilizando Python y la biblioteca Statsmodels.

Después de la depuración de la información, se utilizaron 85.950 observaciones.

Para evaluar los modelos se consideraron:

Pseudo R².
Criterio de Información de Akaike (AIC).
Log-verosimilitud.
Efectos marginales promedio.
AUC.
Accuracy.
Matriz de confusión.
Factor de Inflación de la Varianza (VIF).
7. Resultados
7.1 Modelo Logit

El modelo Logit presentó un Pseudo R² de 0,2748 y una log-verosimilitud de -41.661,01.

Variable	Coeficiente	Significancia
Constante	-4,8288	p < 0,001
hombre	1,2719	p < 0,001
EDAD	0,2906	p < 0,001
edad2	-0,0031	p < 0,001
urbano	-0,9100	p < 0,001

Todos los coeficientes incluidos en el modelo resultaron estadísticamente significativos al nivel convencional del 1 %.

El coeficiente positivo de hombre indica una asociación positiva entre esta característica y la probabilidad de trabajar. La variable EDAD presenta un coeficiente positivo, mientras que edad2 presenta un coeficiente negativo, lo que sugiere una relación no lineal entre edad y probabilidad de trabajar.

El coeficiente negativo de urbano indica una asociación negativa entre residir en el área urbana y la probabilidad estimada de trabajar, manteniendo constantes las demás variables incluidas.

7.2 Modelo Probit

El modelo Probit presentó un Pseudo R² de 0,2745 y una log-verosimilitud de -41.680,55.

Variable	Coeficiente	Significancia
Constante	-2,8353	p < 0,001
hombre	0,7455	p < 0,001
EDAD	0,1701	p < 0,001
edad2	-0,0018	p < 0,001
urbano	-0,5255	p < 0,001

Los signos de los coeficientes coinciden con los obtenidos mediante el modelo Logit. Esto proporciona consistencia en la dirección de las asociaciones encontradas.

8. Efectos marginales promedio

Los efectos marginales promedio permiten interpretar los resultados en términos de cambios en la probabilidad estimada.

Variable	Logit	Probit
hombre	0,2017	0,2035
EDAD	0,0461	0,0464
edad2	-0,0005	-0,0005
urbano	-0,1443	-0,1435

En el modelo Logit, el efecto marginal promedio de hombre es 0,2017. Esto indica que, manteniendo constantes las demás variables del modelo, la condición de ser hombre se encuentra asociada con una probabilidad promedio de trabajar aproximadamente 20,17 puntos porcentuales mayor respecto de la categoría de referencia.

El efecto marginal promedio de EDAD es 0,0461. Sin embargo, debido a que el modelo incorpora simultáneamente EDAD y edad2, este valor debe interpretarse con cautela y no como un incremento constante de la probabilidad por cada año de edad.

El efecto marginal negativo de edad2 (-0,0005) respalda la existencia de una relación no lineal entre edad y probabilidad de trabajar.

Para urbano, el efecto marginal promedio es -0,1443, lo que significa que residir en el área urbana se encuentra asociado con una probabilidad promedio de trabajar aproximadamente 14,43 puntos porcentuales menor respecto del área rural, manteniendo constantes las demás variables.

Los resultados del Probit son muy similares: 0,2035 para hombre, 0,0464 para EDAD, -0,0005 para edad2 y -0,1435 para urbano.

9. Capacidad predictiva

El modelo Logit obtuvo un AUC de 0,8341, lo que evidencia una capacidad de discriminación adecuada entre las observaciones clasificadas en las dos categorías de la variable dependiente.

La exactitud global de clasificación fue de 0,7713, equivalente al 77,13 %.

La matriz de confusión fue:


	Predicción 0	Predicción 1
Real 0	21.547	11.912
Real 1	7.749	44.742

El modelo presenta un recall de 0,6440 para la categoría 0 y de 0,8524 para la categoría 1. La precisión fue de 0,7355 para la categoría 0 y de 0,7897 para la categoría 1.

En conjunto, estos indicadores muestran que el modelo presenta una capacidad predictiva considerable, aunque no clasifica perfectamente todas las observaciones.

10. Diagnóstico y robustez
10.1 Factor de Inflación de la Varianza

Los resultados del VIF fueron:

Variable	VIF
Constante	16,6099
hombre	1,0006
EDAD	16,8969
edad2	16,9013
urbano	1,0052

Los valores de EDAD y edad2 son elevados debido a que la edad al cuadrado se construye directamente a partir de la edad. Por tanto, la elevada relación entre ambas variables es esperable y debe considerarse al interpretar el diagnóstico de multicolinealidad.

No se observa un problema relevante de colinealidad entre hombre y urbano.

10.2 Comparación Logit-Probit
Modelo	Pseudo R²	AIC	Log-verosimilitud
Logit	0,2748	83.332,02	-41.661,01
Probit	0,2745	83.371,11	-41.680,55

Ambos modelos presentan resultados muy similares. El modelo Logit registra un Pseudo R² ligeramente superior y un AIC menor que el Probit. Por estos criterios, el Logit presenta un ajuste ligeramente mejor dentro de las especificaciones estimadas.

Además, los efectos marginales de ambos modelos son prácticamente iguales, lo que evidencia robustez en la dirección y magnitud aproximada de las asociaciones estimadas.

11. Discusión

Los resultados muestran una asociación estadísticamente significativa entre las características analizadas y la probabilidad de trabajar. La diferencia asociada al sexo es particularmente importante: el efecto marginal positivo de hombre es cercano a 20 puntos porcentuales en ambos modelos.

Este resultado es consistente con evidencia reciente sobre Ecuador que identifica diferencias importantes en la participación laboral entre hombres y mujeres. Estudios recientes señalan que factores socioeconómicos y normas sociales pueden contribuir a explicar las diferencias de participación laboral por género.

La edad presenta una relación no lineal con la probabilidad de trabajar. El coeficiente positivo de EDAD y el coeficiente negativo de edad2 sugieren que el efecto de la edad no es constante a lo largo del ciclo de vida. Esta especificación resulta apropiada para evitar imponer una relación estrictamente lineal.

El efecto negativo asociado con urbano debe interpretarse con cautela. El resultado no significa que vivir en una zona urbana cause una menor probabilidad de trabajar. Puede reflejar diferencias en la estructura productiva, composición demográfica, actividades económicas, escolarización u otras características no incluidas en el modelo.

La similitud entre los resultados Logit y Probit fortalece la estabilidad de las conclusiones principales. Asimismo, el AUC de 0,8341 indica que el modelo Logit posee una capacidad adecuada para distinguir entre las dos categorías de la variable dependiente.

12. Conclusiones y limitaciones

Los resultados obtenidos permiten concluir que existen asociaciones estadísticamente significativas entre sexo, edad y área de residencia y la probabilidad de encontrarse trabajando en la muestra analizada.

El modelo Logit presenta un Pseudo R² de 0,2748 y un AIC de 83.332,02, mientras que el Probit obtiene un Pseudo R² de 0,2745 y un AIC de 83.371,11. Por estos criterios, el modelo Logit presenta un desempeño ligeramente superior.

Los efectos marginales promedio son consistentes entre ambos modelos. Ser hombre presenta una asociación positiva con la probabilidad de trabajar, mientras que la residencia urbana presenta una asociación negativa. La inclusión de la edad al cuadrado evidencia una relación no lineal entre edad y probabilidad de trabajar.

El modelo Logit también muestra un desempeño predictivo adecuado, con un AUC de 0,8341 y una exactitud de clasificación del 77,13 %.

Sin embargo, los resultados no deben interpretarse como relaciones causales. El análisis utiliza información observacional y un conjunto limitado de variables explicativas, por lo que pueden existir factores omitidos relacionados tanto con las características individuales como con la condición laboral.

Otra limitación corresponde al tratamiento del diseño muestral de la encuesta. Aunque se dispone del factor de expansión FEXP, su utilización no implica necesariamente que se hayan incorporado todos los componentes del diseño complejo de la ECV. Esta consideración debe tenerse presente al generalizar los resultados.

Finalmente, la relación entre EDAD y edad2 genera valores elevados de VIF, debido a la construcción matemática de la segunda variable. Esto no invalida automáticamente el modelo, pero sí debe ser considerado en el diagnóstico econométrico.

13. Referencias

Bazen, S. (2011). Dummy and ordinal dependent variables. En Econometric methods for labour economics (pp. 53–75). Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199576791.003.0004

Biørn, E. (2016). Analysis of discrete response. En Econometrics of panel data: Methods and applications (pp. 261–286). Oxford University Press. https://doi.org/10.1093/acprof:oso/9780198753445.003.0009

Evdokimov, K. S., Kalnina, I., & Zeleneev, A. (2026). Marginal effects for probit and tobit with endogeneity. The Econometrics Journal, 29(1), 106–124. https://doi.org/10.1093/ectj/utaf010

Fernández-Val, I. (2009). Fixed effects estimation of structural parameters and marginal effects in panel probit models. Journal of Econometrics, 150(1), 71–85. https://doi.org/10.1016/j.jeconom.2009.02.007

Yepez, J., & Caria, S. (2026). Social norms vs socioeconomic vulnerability: Gender identity and female labor force participation in Ecuador. PLOS ONE, 21(5), e0339503. https://doi.org/10.1371/journal.pone.0339503

Instituto Nacional de Estadística y Censos [INEC]. (2014). Encuesta de Condiciones de Vida: Sexta Ronda (ECV6R). INEC.

14. Declaración de uso de inteligencia artificial

Durante el desarrollo de este proyecto se utilizaron herramientas de inteligencia artificial como apoyo para la revisión de código, organización del repositorio, documentación del proyecto y mejora de la redacción. La autora verificó los procedimientos, estimaciones, referencias e interpretaciones y asume la responsabilidad sobre el contenido presentado.