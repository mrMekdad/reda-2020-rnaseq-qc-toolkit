"""Core workflow for RNAseq QC Toolkit by Red@."""

PROJECT_NAME = "RNAseq QC Toolkit"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": "bioinformatics"}
