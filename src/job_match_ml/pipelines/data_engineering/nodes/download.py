"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.14
"""
from pathlib import Path

import gdown
from opendatasets import download
import pandas as pd
import json


def download_resumes(output_dir: str, url, output_filename: str = "resumes.csv"):
    output_filepath = Path(output_dir) / "resumes" / output_filename
    output_filepath.parent.mkdir(parents=True, exist_ok=True)
    if not output_filepath.exists():
        gdown.download(url=url, output=str(output_filepath))
    df = pd.read_csv(output_filepath, on_bad_lines='skip', delimiter=";")
    return df


def download_vacancies(output_dir: str, url: str, region_codes: list[str] = None):
    output_dir = Path(output_dir) / "vacancies"
    if region_codes is None:
        region_codes = [
            "5000000000000",  # Moscow
            "7800000000000",  # Saint Petersburg
            "6300000000000",  # Samara
            "5900000000000",  # Perm
        ]
    full_data = []
    for region_code in region_codes:
        if not (output_dir / f"{region_code}").exists():
            download(
                f"{url}/{region_code}",
                data_dir=output_dir,
            )
        with open(output_dir / f"{region_code}") as f:
            data = json.load(f)["results"]["vacancies"]
            for vacancy in data:
                full_data.append(vacancy["vacancy"])
    df = pd.DataFrame(full_data)
    return df


if __name__ == '__main__':
    download_vacancies(output_dir="../data/01_raw", url="http://opendata.trudvsem.ru/api/v1/vacancies/region")