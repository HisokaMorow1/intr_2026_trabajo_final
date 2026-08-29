"""
Revisiones simples sobre los datos ya cargados.

Cada funcion imprime lo que encontro y devuelve True si esta todo bien,
False si hay algo que revisar.
"""

import pandas as pd

from src import config


def check_raw_data_present() -> bool:
    """Revisa que existan los 6 archivos crudos esperados en raw_data/."""
    expected_files = [
        config.RAW_DATA_CLINICAL_DIR / "synthetic_alzheimer_patients_1000.csv",
        config.RAW_DATA_GENES_DIR / "alzheimer_synthetic_1000_patients_5genes.fasta",
        config.RAW_DATA_GENES_DIR / "alzheimer_synthetic_reference_5genes.fasta",
        config.RAW_DATA_PROTEINS_DIR / "alzheimer_synthetic_protein_sequences_5000.csv",
        config.RAW_DATA_PROTEINS_DIR / "alzheimer_synthetic_reference_5proteins_clean.fasta",
        config.RAW_DATA_METADATA_DIR / "metadata.json",
    ]

    missing = [path for path in expected_files if not path.exists()]

    if missing:
        print("Faltan archivos en raw_data/:")
        for path in missing:
            print(f"  - {path}")
        return False

    print("Todos los archivos de raw_data/ estan presentes.")
    return True


def check_columns(df: pd.DataFrame, expected_columns: list) -> bool:
    """Revisa que df tenga todas las columnas de expected_columns."""
    missing = [col for col in expected_columns if col not in df.columns]

    if missing:
        print("Faltan columnas:", missing)
        return False

    print("Todas las columnas esperadas estan presentes.")
    return True


def check_missing_values(df: pd.DataFrame) -> bool:
    """Revisa valores faltantes por columna."""
    counts = df.isna().sum()
    columns_with_missing = counts[counts > 0]

    if len(columns_with_missing) > 0:
        print("Columnas con valores faltantes:")
        print(columns_with_missing.to_string())
        return False

    print("No hay valores faltantes.")
    return True


def check_duplicate_ids(df: pd.DataFrame, id_column: str) -> bool:
    """
    Revisa valores repetidos en id_column.

    Pensado para columnas que deberian ser unicas por fila (ej. patient_id
    en la ficha clinica). No usar en tablas donde el id se repite a
    proposito, como genes o proteinas (varias filas por paciente).
    """
    n_duplicates = df[id_column].duplicated().sum()

    if n_duplicates > 0:
        print(f"{n_duplicates} valores repetidos en '{id_column}'.")
        return False

    print(f"No hay valores repetidos en '{id_column}'.")
    return True
