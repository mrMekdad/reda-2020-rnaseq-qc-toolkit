import argparse
from rnaseq_qc_toolkit.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Command-line toolkit for read count summaries, QC rollups, and batch notes.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
