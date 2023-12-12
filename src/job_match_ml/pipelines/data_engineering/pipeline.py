"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import download_resumes, download_vacancies


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                download_resumes,
                inputs=["params:cv_dataset_path", "params:cv_dataset_url"],
                outputs="resumes",
                name="download_cv_dataset"
            ),
            node(
                download_vacancies,
                inputs=["params:vacancies_dataset_path", "params:vacancies_dataset_url", "params:vacancies_region_codes"],
                outputs="vacancies",
                name="download_vacancies_dataset",
            ),
        ]
    )
