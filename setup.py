from setuptools import setup

setup(
    name="reda-2020-rnaseq-qc-toolkit",
    version="0.1.0",
    description="Command-line toolkit for read count summaries, QC rollups, and batch notes.",
    author="Red@",
    packages=["rnaseq_qc_toolkit"],
    package_dir={"": "src"},
)
