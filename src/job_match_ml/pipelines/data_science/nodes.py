"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""
import pandas as pd
from sklearn.metrics import roc_auc_score, accuracy_score, precision_score, recall_score, f1_score
import wget
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from navec import Navec
from razdel import tokenize
import pymorphy2


def make_predictions_navec(evaluation_data: pd.DataFrame) -> pd.DataFrame:
    """
    Extracts job title from resumes and generates embeddings for them.
    """
    if not os.path.exists("navec_hudlit_v1_12B_500K_300d_100q.tar"):
        wget.download("https://storage.yandexcloud.net/natasha-navec/packs/navec_hudlit_v1_12B_500K_300d_100q.tar")
    navec = Navec.load("navec_hudlit_v1_12B_500K_300d_100q.tar")
    embedding_dim = 300
    morph = pymorphy2.MorphAnalyzer()

    def tokenizer_razdel(text):
        navec_words = []
        tokens = [_.text for _ in list(tokenize(text))]
        for word in [morph.parse(_)[0].normal_form for _ in tokens]:
            try:
                navec[word]
                navec_words.append(word)
            except:
                pass
        return navec_words

    def get_sentence_embedding(sentence):
        words = tokenizer_razdel(sentence)
        sentence_len = len(words)
        embedding = np.zeros(embedding_dim)
        for word in words:
            navec[word.lower()]
            embedding += navec[word.lower()]
        print(embedding)
        return embedding / sentence_len

    def make_prediction(row):
        resume_emb = get_sentence_embedding(row["Резюме"])
        vacancy_emb = get_sentence_embedding(row["Вакансия"])
        try:
            return cosine_similarity([resume_emb], [vacancy_emb])[0][0]
        except:
            return 0

    evaluation_data["prediction"] = evaluation_data.apply(make_prediction, axis=1)
    return evaluation_data


def evaluate_navec(predictions_navec: pd.DataFrame) -> pd.DataFrame:
    """
    Evaluates the model on the evaluation dataset.
    """
    target = predictions_navec["Совпадение"]
    predicted = predictions_navec["prediction"]
    predicted_binary = np.where(predicted > 0.5, 1, 0)
    metrics_dict = {
        "roc_auc": roc_auc_score(target, predicted),
        "accuracy": accuracy_score(target, predicted_binary),
        "precision": precision_score(target, predicted_binary),
        "recall": recall_score(target, predicted_binary),
        "f1": f1_score(target, predicted_binary),
    }
    return pd.DataFrame(metrics_dict, index=[0])
