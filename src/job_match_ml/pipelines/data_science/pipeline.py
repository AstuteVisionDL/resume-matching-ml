"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import extract_job_title_resumes_embeddings


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            extract_job_title_resumes_embeddings,
            inputs="processed_resumes",
            outputs="resumes_embeddings",
            name="extract_job_title_resumes_embeddings",
        )
    ])
