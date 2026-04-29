from pathlib import Path

import pandas as pd
import typer
from tqdm import tqdm


def main(data_root: Path, outfile: Path, pattern: str = "digitization_metadata.csv"):
    dfs = []
    for path in tqdm(data_root.rglob(pattern)):
        relpath = path.relative_to(data_root).parent
        df = pd.read_csv(path)
        df["file_path"] = df["file_path"].apply(lambda p, r=relpath: str(r / p))
        dfs.append(df)
    combined = pd.concat(dfs)
    combined.to_csv(outfile)
    print(combined.shape, "written to", outfile)


if __name__ == "__main__":
    typer.run(main)
