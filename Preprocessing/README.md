# Description

This folder contains python scripts for data cleaning and processing.

## Explore.ipynb

*Requires input_results.csv to be present in ./data*

This jupyter notebook was used for exploratory data analysis.
It also was were data cleaning was performed, *clean_dental_data.py* is based on this file.

## clean_dental_data.py

This python file cleans the data retrieved from dentists.
It exists so the research can be reproduced.

## extract_text_sts.ipynb

*Requires the following to be present in ./data/input/*
sts-train.csv
sts-test.csv

Will tokenize and filter the data for the later stages and export those to .txt and .csv files at *./data/output/*

