# src/

Módulos compartidos por todos los notebooks. Ver `ARQUITECTURA.md` (raíz del
proyecto) para el detalle completo — acá va solo un resumen rápido.

| Módulo | Qué hace |
|---|---|
| `config.py` | Rutas del proyecto y constantes compartidas (genes, colores, nombres de columna). |
| `data_io.py` | Carga cada dataset del proyecto y guarda tablas/figuras en `results/`. |
| `validation.py` | Comprobaciones básicas de los datos ya cargados (columnas, duplicados, valores faltantes). |
| `plotting.py` | Estilo visual común para los gráficos del proyecto. |

## Ejemplo de uso desde un notebook

```python
from src import config, data_io, validation, plotting

plotting.apply_plot_style()

df_clinico = data_io.load_clinical_data()
validation.check_missing_values(df_clinico)

data_io.save_table(df_clinico.describe(), "resumen_clinico.csv")
```

No hace falta escribir ninguna ruta a mano: cada función ya sabe dónde están
los datos y dónde guardar los resultados.
