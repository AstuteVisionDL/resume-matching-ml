from sklearn.metrics import roc_auc_score, accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
import numpy as np
import clearml


def evaluate(predictions: pd.DataFrame, model_name: str) -> pd.DataFrame:
    """
    Evaluates the model on the evaluation dataset.
    """
    # create clearml task
    task = clearml.Task.init(project_name="job_match_ml", task_name=f"evaluate_{model_name}")
    target = predictions["Совпадение"]
    predicted = predictions["prediction"]
    predicted_binary_0_5 = np.where(predicted > 0.5, 1, 0)
    predicted_binary_0_25 = np.where(predicted > 0.25, 1, 0)
    metrics_dict = {
        "roc_auc": roc_auc_score(target, predicted),
        "accuracy_at_0.5": accuracy_score(target, predicted_binary_0_5),
        "precision_at_0.5": precision_score(target, predicted_binary_0_5),
        "recall_at_0.5": recall_score(target, predicted_binary_0_5),
        "f1_at_0.5": f1_score(target, predicted_binary_0_5),
        "accuracy_at_0.25": accuracy_score(target, predicted_binary_0_25),
        "precision_at_0.25": precision_score(target, predicted_binary_0_25),
        "recall_at_0.25": recall_score(target, predicted_binary_0_25),
        "f1_at_0.25": f1_score(target, predicted_binary_0_25),
    }
    df = pd.DataFrame(metrics_dict, index=[0])
    task.get_logger().report_table("Metrics",
                                   f"Metrics for {model_name}",
                                   iteration=0,
                                   table_plot=df)
    task.close()
    return df
