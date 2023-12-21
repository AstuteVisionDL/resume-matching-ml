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
https://app.clear.ml/projects/8e7a87fb96ed45a3951f29c5ed13cd65/experiments/0d9b2962a4ac48d7a01ed5abe0e1eb01/output/execution
https://app.clear.ml/projects/8e7a87fb96ed45a3951f29c5ed13cd65/experiments/bcd63ee8d9914663ad6ccd0f3a3d52de/output/execution