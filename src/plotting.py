"""
Estilo visual compartido por los graficos del proyecto.
"""

import seaborn as sns


def apply_plot_style() -> None:
    """Aplica un tema y un tamano de figura consistentes para todo el proyecto."""
    sns.set_theme(style="whitegrid", rc={"figure.figsize": (8, 5)})
