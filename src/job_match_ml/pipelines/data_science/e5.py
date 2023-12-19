from transformers import AutoTokenizer, AutoModel
import torch.nn.functional as F
from torch import Tensor
import numpy as np


def average_pool(last_hidden_states: Tensor,
                 attention_mask: Tensor) -> Tensor:
    last_hidden = last_hidden_states.masked_fill(~attention_mask[..., None].bool(), 0.0)
    return last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]


def get_model():
    tokenizer = AutoTokenizer.from_pretrained('intfloat/multilingual-e5-large')
    model = AutoModel.from_pretrained('intfloat/multilingual-e5-large')
    return tokenizer, model


def e5_sts(sent1: str, sent2: str) -> float:
    tokenizer, model = get_model()
    # Tokenize the input texts
    batch_dict = tokenizer([sent1, sent2], max_length=512, padding=True, truncation=True, return_tensors='pt')
    outputs = model(**batch_dict)
    embeddings = average_pool(outputs.last_hidden_state, batch_dict['attention_mask'])
    # normalize embeddings
    embeddings = F.normalize(embeddings, p=2, dim=1)
    scores = (embeddings @ embeddings.T) * 100
    scores = scores.tolist()
    scores = np.divide(scores, 20)
    print(scores)
    return scores[0][1]


def make_predictions_e5(evaluation_data):
    evaluation_data["prediction"] = evaluation_data.apply(lambda x: e5_sts(x["Резюме"], x["Вакансия"]), axis=1)
    return evaluation_data
