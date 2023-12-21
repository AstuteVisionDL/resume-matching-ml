# job-match-ml

## How to install dependencies

To install them, run:

```
pip install -r src/requirements.txt
```

## How to run full pipeline

You can run all project with:

```
kedro run
```

### How to run only part of pipeline

Pipeline consist of two parts: 
1) Data processing pipeline
2) Data science pipeline

Data processing pipeline for extracting and transforming raw data from HH resume dataset and open API with vacancies 

Data science pipeline for evaluation different methods of sentence similarity finding

### Data processing pipeline
To run data processing pipeline run:

```bash
kedro run --pipeline data_engineering
```

### Data science pipeline

1) Download validation set from [google drive](https://drive.google.com/file/d/1XnRtaojtZJSzm1oJ2FobqBLgW-a6sZwd/view?usp=sharing)
2) Place it in data/03_primary directory
3) Run data science pipeline with:

```bash
kedro run --pipeline data_science
```


# Results 

Evaluation results:
e5
https://app.clear.ml/projects/8e7a87fb96ed45a3951f29c5ed13cd65/experiments/00a1ced96ca24a358534debe15c36a7f/output/execution

mp5
https://app.clear.ml/projects/8e7a87fb96ed45a3951f29c5ed13cd65/experiments/3591761e3a3e461e8370ee89588ed4eb/output/execution

navec:
https://app.clear.ml/projects/8e7a87fb96ed45a3951f29c5ed13cd65/experiments/7b8abea984984056853cb70ed4fa677a/output/execution

Main metric was Roc-AUC, so based on them best model was intfloat/multilingual-e5-large
