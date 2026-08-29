"""
Funciones para cargar los datos del proyecto y guardar resultados.

Cada funcion de carga sabe su propia ruta (usa config.py); nadie necesita
escribir una ruta a mano en un notebook.
"""

import json
from pathlib import Path

import pandas as pd

from src import config


def load_metadata() -> dict:
    """Carga metadata.json (columnas y nombre del label del proyecto)."""
    path = config.RAW_DATA_METADATA_DIR / "metadata.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_clinical_data() -> pd.DataFrame:
    """Carga la ficha clinica de los 1000 pacientes."""
    path = config.RAW_DATA_CLINICAL_DIR / "synthetic_alzheimer_patients_1000.csv"
    return pd.read_csv(path)


def load_gene_sequences() -> pd.DataFrame:
    """Carga las 5000 secuencias de DNA de los pacientes (1 fila = 1 gen de 1 paciente)."""
    path = config.RAW_DATA_GENES_DIR / "alzheimer_synthetic_1000_patients_5genes.fasta"
    rows = fasta_to_rows(path)
    df = pd.DataFrame(rows)
    df = df.rename(columns={"id": "patient_id"})
    return df[["patient_id", "gene", "chromosome", "sequence"]]


def load_gene_reference() -> pd.DataFrame:
    """Carga la secuencia de referencia de cada uno de los 5 genes."""
    path = config.RAW_DATA_GENES_DIR / "alzheimer_synthetic_reference_5genes.fasta"
    rows = fasta_to_rows(path)
    df = pd.DataFrame(rows)
    return df[["gene", "chromosome", "sequence"]]


def load_protein_sequences() -> pd.DataFrame:
    """Carga las 5000 secuencias de proteinas de los pacientes (version clean)."""
    path = config.RAW_DATA_PROTEINS_DIR / "alzheimer_synthetic_protein_sequences_5000.csv"
    return pd.read_csv(path)


def load_protein_reference() -> pd.DataFrame:
    """Carga la secuencia de referencia de cada una de las 5 proteinas (version clean)."""
    path = config.RAW_DATA_PROTEINS_DIR / "alzheimer_synthetic_reference_5proteins_clean.fasta"
    rows = fasta_to_rows(path)
    df = pd.DataFrame(rows)
    return df[["gene", "chromosome", "sequence"]]


def save_table(df: pd.DataFrame, filename: str) -> None:
    """Guarda df como CSV en results/tables/."""
    df.to_csv(config.TABLES_DIR / filename, index=False)


def save_figure(fig, filename: str) -> None:
    """Guarda fig en results/figures/."""
    fig.savefig(config.FIGURES_DIR / filename)


# --- Lectura de FASTA (uso interno de este archivo) ---
# Los headers del proyecto siguen el formato ">id|gene=X|chr=N|...",
# por ejemplo ">P0001|gene=APP|chr=21|source=synthetic".

def fasta_to_rows(path: Path) -> list:
    rows = []
    header = None
    sequence = ""

    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if header is not None:
                    rows.append(header_to_row(header, sequence))
                header = line[1:]
                sequence = ""
            else:
                sequence += line
        if header is not None:
            rows.append(header_to_row(header, sequence))

    return rows


def header_to_row(header: str, sequence: str) -> dict:
    parts = header.split("|")
    record_id = parts[0]
    tags = parts[1:]

    tag_values = {}
    for tag in tags:
        key, value = tag.split("=", 1)
        tag_values[key] = value

    return {
        "id": record_id,
        "gene": tag_values["gene"],
        "chromosome": tag_values["chr"],
        "sequence": sequence,
    }
