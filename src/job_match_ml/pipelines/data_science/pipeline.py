"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import make_predictions_navec, evaluate_navec


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            make_predictions_navec,
            inputs="evaluation_data",
            outputs="predictions_navec",
            name="make_predictions_navec",
        ),
        node(
            evaluate_navec,
            inputs="predictions_navec",
            outputs="evaluation_navec",
            name="evaluate_navec",
        )
    ])
