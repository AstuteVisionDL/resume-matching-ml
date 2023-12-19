"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node

from .e5 import make_predictions_e5
from .navec import make_predictions_navec
from .evaluation import evaluate


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            make_predictions_navec,
            inputs="evaluation_data",
            outputs="predictions_navec",
            name="make_predictions_navec",
        ),
        node(
            evaluate,
            inputs=["predictions_navec", "params:navec_model_name"],
            outputs="evaluation_navec",
            name="evaluate_navec",
        ),
        node(
            make_predictions_e5,
            inputs="evaluation_data",
            outputs="predictions_e5",
            name="make_predictions_e5",
        ),
        node(
            evaluate,
            inputs=["predictions_e5", "params:e5_model_name"],
            outputs="evaluation_e5",
            name="evaluate_e5",
        )
    ])
