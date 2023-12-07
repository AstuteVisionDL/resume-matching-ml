from pathlib import Path

from opendatasets import download

from job_match.consts import RAW_DATA_DIR
from job_match.data.consts import RESUMES_URL
import gdown


def download_resumes(output_dir: Path, output_filename: str = "resumes.csv"):
    output_filepath = output_dir / "resumes" / output_filename
    output_filepath.parent.mkdir(parents=True, exist_ok=True)
    gdown.download(url=RESUMES_URL, output=str(output_filepath))


def download_vacancies(output_dir: Path):
    output_dir = output_dir / "vacancies"
    region_codes = [
        "5000000000000",  # Moscow
        "7800000000000",  # Saint Petersburg
        "6300000000000",  # Samara
        "5900000000000",  # Perm
    ]
    for region_code in region_codes:
        download(
            f"http://opendata.trudvsem.ru/api/v1/vacancies/region/{region_code}",
            data_dir=output_dir,
        )


def download_all(output_filepath: Path = RAW_DATA_DIR):
    download_resumes(output_filepath)
    download_vacancies(output_filepath)


if __name__ == "__main__":
    download_all()
