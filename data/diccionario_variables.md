# Diccionario de variables

## Fuente

Encuesta de Condiciones de Vida (ECV6R) del Instituto Nacional de
Estadística y Censos (INEC) de Ecuador.

## Unidad de observación

Persona.

## Variable dependiente

**trabaja:** variable binaria que representa la condición laboral.
1 = trabaja; 0 = no trabaja.

## Variables explicativas

| Variable | Tipo | Descripción |
|---|---|---|
| trabaja | Binaria | Condición laboral |
| hombre | Binaria | 1 = hombre; 0 = mujer |
| EDAD | Numérica | Edad de la persona en años |
| edad2 | Numérica | Edad al cuadrado |
| urbano | Binaria | 1 = área urbana; 0 = área rural |
| FEXP | Numérica | Factor de expansión de la encuesta |

## Tratamiento de datos

Las observaciones con valores faltantes en las variables necesarias
para la estimación son excluidas.

La variable edad2 se construye como EDAD^2 para capturar una posible
relación no lineal entre edad y probabilidad de trabajar.

Las variables categóricas utilizadas en el modelo se expresan como
indicadores binarios.

## Factor de expansión y diseño muestral

La ECV6R es una encuesta y contiene factores de expansión. El análisis
debe reconocer que la utilización de FEXP no equivale necesariamente
a incorporar todos los componentes del diseño muestral complejo.

Esta consideración constituye una limitación metodológica del proyecto.

## Fuente

Instituto Nacional de Estadística y Censos (INEC), Encuesta de
Condiciones de Vida ECV6R.

Fecha de consulta: 2026.
