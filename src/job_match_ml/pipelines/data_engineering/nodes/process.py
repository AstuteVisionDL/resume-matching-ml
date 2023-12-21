import pandas as pd


def extract_job_title_from_vacancies(vacancies: pd.DataFrame) -> pd.DataFrame:
    """Extract job title from vacancies dataset"""
    vacancies["job"] = vacancies["job-name"].str.lower()
    return vacancies[["id", "job"]]


def extract_job_title_from_resumes(resumes: pd.DataFrame) -> pd.DataFrame:
    """Extract job title from resumes dataset"""
    resumes["job"] = resumes["Ищет работу на должность:"].str.lower()
    resumes.reset_index(inplace=True)
    return resumes[["index", "job"]]
