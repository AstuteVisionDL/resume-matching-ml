"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""
import pandas as pd
import wget
from navec import Navec
import os
import numpy as np


def extract_job_title_resumes_embeddings(processed_resumes: pd.DataFrame) -> pd.DataFrame:
    """
    Extracts job title from resumes and generates embeddings for them.
    """
    if not os.path.exists("navec_hudlit_v1_12B_500K_300d_100q.tar"):
        wget.download("https://storage.yandexcloud.net/natasha-navec/packs/navec_hudlit_v1_12B_500K_300d_100q.tar")
    model = Navec.load("navec_hudlit_v1_12B_500K_300d_100q.tar")

    def extract_job_title_embeddings(row):
        job_title = row["job"].split(" ")
        job_title = [word for word in job_title if word in model]
        if len(job_title) == 0:
            return np.zeros(300)
        job_embeddings = np.array([model[word] for word in job_title])
        return np.mean(job_embeddings, axis=0)

    processed_resumes["job_embeddings"] = processed_resumes.apply(extract_job_title_embeddings, axis=1)
    return processed_resumes
