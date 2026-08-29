# Integrative Analysis of a Synthetic Alzheimer's Cohort

Proyecto final del curso de Introducción a la Bioinformática.

## Descripción

Este proyecto realiza un análisis exploratorio e integrador de una cohorte sintética de **1.000 pacientes**, combinando información clínica, genómica y proteica para identificar diferencias entre pacientes sanos y con enfermedad de Alzheimer.

El análisis sigue la estrategia propuesta en el proyecto:

**Clínica → DNA → Proteína → Integración → Candidatos diferenciales**

---

## Objetivos

- Realizar un análisis exploratorio (EDA) de la ficha clínica.
- Identificar mutaciones en secuencias de DNA mediante comparación con secuencias de referencia.
- Caracterizar cambios en proteínas derivados de las variantes genéticas.
- Integrar información clínica, genómica y proteica utilizando `patient_id`.
- Proponer candidatos diferenciales asociados al diagnóstico de Alzheimer.

---

## Dataset

La cohorte contiene:

- 1.000 pacientes
- 657 controles
- 343 pacientes con Alzheimer

Información disponible:

- Ficha clínica
- Secuencias de DNA (APP, PSEN1, PSEN2, APOE y TREM2)
- Secuencias de proteínas
- Archivos de referencia para genes y proteínas
- Metadata

---

## Estructura del proyecto

```text
.
├── src/                      # config, data_io, validation, plotting
├── raw_data/                 # datos crudos (no versionados, ver raw_data/README.md)
│   ├── ficha_clinica/
│   ├── genes/
│   ├── proteins/
│   └── metadata/
├── notebooks/                # 00_setup ... 05_candidates_summary
├── outputs/                  # datos intermedios entre etapas
├── results/
│   ├── figures/
│   └── tables/
└── README.md
```
---

## Flujo de trabajo

### 1. Exploración clínica

- Dimensiones del dataset
- Tipos de variables
- Valores faltantes
- Registros duplicados
- Estadística descriptiva
- Histogramas
- Boxplots
- Violinplots
- Variables categóricas
- Matriz de correlación
- PCA

### 2. Análisis genómico

- Separación de secuencias por gen
- Comparación con secuencias de referencia
- Identificación de SNPs
- Inserciones
- Deleciones
- Frecuencia de variantes
- Carga mutacional

### 3. Análisis proteico

- Comparación con proteínas de referencia
- Cambios de aminoácidos
- Longitud de proteínas
- Composición de aminoácidos
- Fracción hidrofóbica
- Fracción aromática
- Fracción cargada
- Peso molecular

### 4. Integración

- Relación DNA → proteína
- Relación proteína → clínica
- Comparación entre controles y pacientes
- Selección de candidatos diferenciales

---

## Herramientas utilizadas

- Python 3.11
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Biopython

---

## Resultados

Las figuras y tablas que produzca cada notebook se guardan en `results/`
(`figures/` y `tables/`), usando las funciones de `src/data_io.py`.

---

## Reproducibilidad

Clonar el repositorio:

```bash
git clone https://github.com/HisokaMorow1/intr_2026_trabajo_final.git
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar los notebooks siguiendo el orden de las etapas.

---

## Consideraciones

- El dataset es completamente **sintético**.
- Los resultados corresponden a un **análisis exploratorio**.
- No deben interpretarse como evidencia clínica real.

---

## Autores

- Matías Cárcamo 
- Rafael Sánchez
- Catalina Viñas
- Karina Díaz
- Cristina Hernández
- Duvan Figueroa 
---

## Uso de inteligencia artificial

Se utilizó inteligencia artificial como apoyo en la organización del código, resolución de dudas, depuración de errores y documentación.