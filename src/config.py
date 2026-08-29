"""
Rutas del proyecto y constantes compartidas.

Ningun notebook deberia escribir una ruta a mano: todas las rutas del
proyecto salen de este archivo.
"""

from pathlib import Path

# parent.parent porque este archivo vive en src/: funciona igual sin
# importar si el notebook corre desde notebooks/ o desde la raiz.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = PROJECT_ROOT / "raw_data"
RAW_DATA_CLINICAL_DIR = RAW_DATA_DIR / "ficha_clinica"
RAW_DATA_GENES_DIR = RAW_DATA_DIR / "genes"
RAW_DATA_PROTEINS_DIR = RAW_DATA_DIR / "proteins"
RAW_DATA_METADATA_DIR = RAW_DATA_DIR / "metadata"

RESULTS_DIR = PROJECT_ROOT / "results"
FIGURES_DIR = RESULTS_DIR / "figures"
TABLES_DIR = RESULTS_DIR / "tables"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

# Constantes verificadas con los archivos del proyecto.

# metadata.json la llama "col_id".
PATIENT_ID_COL = "patient_id"

# metadata.json la llama "label". 0 = sano, 1 = Alzheimer.
LABEL_COL = "alzheimer"

# Orden de los genes en los archivos FASTA.
GENES = ["APP", "PSEN1", "PSEN2", "APOE", "TREM2"]

# Colores usados para mantener consistencia entre los graficos.
PALETTE = {0: "#4C72B0", 1: "#C44E52"}


def create_project_folders() -> None:
    """Crea results/, results/figures/, results/tables/ y outputs/ si faltan (no toca raw_data/)."""
    for folder in (RESULTS_DIR, FIGURES_DIR, TABLES_DIR, OUTPUTS_DIR):
        folder.mkdir(parents=True, exist_ok=True)
