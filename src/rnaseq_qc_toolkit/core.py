"""Core workflow for RNAseq QC Toolkit by Red@."""

PROJECT_NAME = "RNAseq QC Toolkit"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
