# Apuntes — Integración de datos (notebook 04)

Notas en lenguaje simple para entender y explicar todo el trabajo, desde el alineamiento hasta la
integración final. Sirve como guion de estudio y como base para la defensa.

---

## La idea en una frase

Cada paciente tiene tres tipos de datos generados por separado: su **ficha clínica**, sus
**secuencias de genes** (DNA) y sus **secuencias de proteínas**. El notebook 04 los junta en una
sola tabla, uno por paciente, y busca qué relaciones son significativas dentro del universo
completo de muestras.

---

## 1. De qué trata el trabajo: contexto y alineamiento

**Objetivo.** Detectar cambios en los genes, respecto a una secuencia de **referencia**, que estén
asociados al Alzheimer en los casos diagnosticados.

**Método.** Alinear la secuencia candidata (la del paciente) contra la de referencia. El
alineamiento es lo que permite ver, posición por posición, dónde el paciente difiere del patrón.

**Por qué importa a nivel biológico.** El gen codifica un producto: la **proteína**. Las proteínas
tienen **regiones conservadas**, tramos críticos para su función. Una mutación en esas zonas suele
ser la más determinante en el desarrollo de la enfermedad. Por eso no basta con contar cambios:
importa **dónde** caen y si alteran la proteína (de ahí la conexión DNA → proteína de los nb 02 y 03).

---

## 2. Pregunta vs. hipótesis

Son dos cosas distintas y conviene tenerlas claras:

- **La pregunta** suele ser **binaria**: ¿existen diferencias en las secuencias de personas con
  diagnóstico de Alzheimer? (sí / no).
- **La hipótesis** pide una respuesta **no binaria**: se cuantifica, da un número.

**Enfoque del trabajo.** ¿Existe un **incremento porcentual** en las variantes mutacionales entre
pacientes con diagnóstico y sin diagnóstico? Con una pregunta central sólida y bien respondida
alcanza; lo importante es responderla con rigor, no acumular preguntas.

---

## 3. Cómo se cuenta: tipo de variante y carga mutacional

**Primero el tipo, después la posición.** En una primera etapa interesa **identificar el tipo de
variante** y ver su comportamiento, más que fijar la posición exacta. Los tres tipos:

- *SNP* (*Single Nucleotide Polymorphism*): cambia un nucleótido por otro.
- **Deleción**: se pierden nucleótidos.
- **Inserción**: se agregan nucleótidos.

**El conteo como descriptor.** Se caracteriza el genoma de forma cuantitativa: cuántos *SNPs*,
deleciones e inserciones tiene cada muestra. Ese conteo es el descriptor más simple para comparar
pacientes.

**Estratificar Alzheimer vs. control.** Las preguntas concretas:

- ¿Qué **porcentaje** de genes con deleción/inserción hay cuando el Alzheimer está presente y
  cuando no?
- ¿Qué proporción de pacientes positivos y negativos presenta 1 o 2 mutaciones centrales?

Eso es la **carga mutacional**: cuántos cambios acumula cada paciente. En los datos, la carga es
mayor en casos, pero el exceso está concentrado en pocas variantes (sobre todo APOE), no repartido
por todo el genoma.

**Análisis avanzado (opcional): zonas calientes.** Hacer el conteo **por posiciones específicas**.
Es más complejo, pero permite ver si hay *hotspots* (zonas del gen con mayor tendencia a asociarse
a un diagnóstico positivo). Responde a: ¿hay tramos del gen que concentran las mutaciones ligadas
a la enfermedad?

---

## 4. Cómo se integra: el notebook 04

**Por qué unir por `patient_id`.** Es lo único que comparten las tres capas. La ficha no sabe de
secuencias y el FASTA no sabe de presión arterial; el identificador del paciente es el hilo que
los conecta. Unir tablas por una columna común se llama *merge*.

**El control de calidad va primero.** Antes de unir, dos chequeos que, si fallan, dejan el dataset
mal sin avisar:

1. ¿Están los mismos 1.000 `patient_id` en las tres capas, sin duplicados? Sí.
2. ¿La etiqueta `alzheimer` coincide paciente a paciente en las tres? Tiene que ser idéntica.

Recién ahí se hace el *merge* (*inner*, porque no falta nadie).

**Qué aporta cada capa.**

- **Clínica.** La señal más fuerte del trabajo es la *edad* (casos ~9 años mayores).
- **DNA.** El *haplotipo* APOE: dos variantes ligadas presentes en ~60% de casos vs. ~19% de
  controles.
- **Proteína.** Traduce los cambios de DNA. Aparecen los *frameshift*: un indel de pocos
  nucleótidos corre el marco de lectura y altera toda la proteína desde ese punto.

**Coherencia entre capas** (integrar no es solo apilar columnas):

- Carga de DNA y de proteína suben juntas, pero no perfecto: el desajuste lo causan los
  *frameshift* (un nucleótido cambia cientos de aminoácidos).
- La variante APOE aparece en los mismos pacientes en DNA y en proteína. Es la mejor prueba de que
  las capas están bien conectadas.
- Entre capas la correlación es **baja**: cada una aporta algo que las otras no tienen. Eso es lo
  que justifica integrar.

**Meta final.** Integrar todos los datos, identificar las relaciones significativas e interpretar
los hallazgos dentro del universo completo de las muestras.

---

## 5. Estadística y modelos

**Desbalance de datos.** Las dos distribuciones (sanos vs. Alzheimer) están desbalanceadas (~2
controles por caso). Eso obliga a comparar con **porcentajes**, no con conteos absolutos, y a
evaluar el efecto real de un grupo sobre el otro.

**D de Cohen — tamaño de efecto.** No dice solo *si* hay diferencia, sino **qué tan grande** es,
normalizada por la variabilidad de los datos. Es lo que permite decir si una diferencia es
biológicamente relevante o solo ruido. Regla: |d| ≈ 0.2 chico, 0.5 mediano, 0.8 grande. Es la
herramienta correcta justo porque los grupos están desbalanceados.

**Teorema de Bayes.** Sirve para actualizar probabilidades. Ejemplo directo: calcular la
probabilidad de tener Alzheimer **dado que** se encontró una mutación específica —
P(Alzheimer | mutación)— a partir de las frecuencias observadas en cada grupo.

**CatBoost.** Algoritmo de *machine learning* basado en árboles de decisión, eficiente con
variables **categóricas** (como el tipo de mutación) sin preprocesamiento complejo. Es el modelo
sugerido para el análisis integrado. (En el notebook 04 se dejó una regresión logística simple
como línea base accesible; *CatBoost* es la extensión natural si se quiere un modelo más potente.)

**Visualización.** Para lo comparativo, los **gráficos de barras combinadas** son la mejor opción:
muestran de un vistazo la diferencia entre casos y controles por variable, gen o tipo de cambio.

---

## 6. Qué NO se puede concluir

- Nada causal. Todo es asociación descriptiva sobre datos **sintéticos** de uso docente; las
  relaciones fueron sembradas por el generador.
- Que el genotipo determina el diagnóstico. Hay controles con el haplotipo APOE y casos sin él.
- Que un modelo entrenado acá sirva para clasificar pacientes reales.

---

## Diálogo de defensa (posibles preguntas)

**P: ¿Cuál es la pregunta y cuál la hipótesis?**
R: La pregunta es binaria: ¿hay diferencias en las secuencias de los casos? La hipótesis la
cuantifica: ¿hay un incremento porcentual de variantes mutacionales en los casos frente a los
controles? Esa versión numérica es la que respondemos.

**P: ¿Por qué alinear contra una referencia?**
R: Porque el alineamiento es lo que deja ver, posición por posición, dónde el paciente difiere del
patrón. Sin referencia no hay contra qué comparar.

**P: ¿Por qué importa dónde cae la mutación y no solo cuántas hay?**
R: Porque el gen codifica una proteína con regiones conservadas críticas para su función. Una
mutación en esas zonas pesa mucho más que la misma cantidad de cambios en zonas neutras.

**P: ¿Qué es la carga mutacional?**
R: Cuántos cambios acumula cada paciente. La usamos como descriptor cuantitativo y la comparamos
entre grupos. Es mayor en casos, pero concentrada en pocas variantes, sobre todo APOE.

**P: ¿Cómo unieron tres tipos de datos distintos?**
R: Por `patient_id`, con un *merge*. Es la única columna común. Antes verificamos que los 1.000
IDs estén en las tres capas y que la etiqueta coincida paciente a paciente.

**P: ¿Por qué usaron *inner join*?**
R: Porque el control de calidad confirmó que no falta ningún paciente. Con datos incompletos habría
que decidir entre descartar (inner) o rellenar con huecos (outer).

**P: Los grupos están desbalanceados, ¿eso no sesga la comparación?**
R: Por eso comparamos en porcentajes y usamos el *d de Cohen*, que mide el tamaño del efecto
normalizado por la variabilidad, no el conteo bruto.

**P: ¿Para qué serviría el teorema de Bayes acá?**
R: Para pasar de "esta variante es más frecuente en casos" a "cuál es la probabilidad de Alzheimer
dado que un paciente porta esta variante": P(Alzheimer | mutación).

**P: ¿Por qué *CatBoost* y no otro modelo?**
R: Porque maneja bien variables categóricas como el tipo de mutación sin preprocesamiento complejo.
En el notebook dejamos una regresión logística simple como base; *CatBoost* es el paso siguiente.

**P: ¿Encontraron zonas calientes en los genes?**
R: Ese es el análisis por posiciones, más avanzado: buscar tramos del gen que concentren las
mutaciones asociadas al diagnóstico. Es opcional respecto de la pregunta central.

**P: ¿Las capas se contradicen?**
R: No. Carga de DNA y de proteína suben juntas, y la variante APOE aparece en los mismos pacientes
en ambas capas. El único desajuste lo explican los *frameshift*.

**P: ¿Qué límite tiene todo esto?**
R: Son datos sintéticos y asociaciones sembradas. Es un ejercicio de método, no un resultado
clínico.
