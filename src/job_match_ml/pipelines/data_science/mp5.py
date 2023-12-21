import torch
from transformers import AutoTokenizer, AutoModel
import torch.nn.functional as F
import numpy as np


def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


def get_model():
    tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/paraphrase-multilingual-mpnet-base-v2')
    model = AutoModel.from_pretrained('sentence-transformers/paraphrase-multilingual-mpnet-base-v2')
    return tokenizer, model


def mpnet_sts(sent1: str, sent2: str) -> float:
    tokenizer_mpnet, model_mpnet = get_model()
    sentences = [sent1, sent2]
    # Tokenize sentences
    encoded_input = tokenizer_mpnet(sentences, padding=True, truncation=True, return_tensors='pt')
    # Compute token embeddings
    with torch.no_grad():
        model_output = model_mpnet(**encoded_input)

    # Perform pooling. In this case, max pooling.
    sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])
    # Косинусное сходство
    sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)
    scores = (sentence_embeddings @ sentence_embeddings.T) * 100
    scores = scores.tolist()
    scores = np.divide(scores, 100)
    return scores[0][1]


def make_predictions_mp5(evaluation_data):
    evaluation_data["prediction"] = evaluation_data.apply(lambda x: mpnet_sts(x["Резюме"], x["Вакансия"]), axis=1)
    return evaluation_data
