# Data science blog post project

## Summary

Repository containing a jupyter notebook which scrapes data from Indeed.co.uk (a popular UK job posting site) and performs analyis on the data extracted.

The analysis follows the CRISP-DM process and seeks to answer the following 3 questions: 

* What are the most requested skills/technologies for Data Scientist positions?
* Where are Data Scientist roles located across the UK?
* Do roles tend to be permanent or contract/temporary roles

The full process and findings are documented in the jupyter notebook uk-data-science-job-analysis.ipynb. A blog post which explains the result can be read at https://medium.com/@neilmayhew/uk-data-science-roles-aug-2020-44f3123eb640. 

In short the analysis found that a large proportion of data science jobs are found in London and that they are very often permanent positions. The key skill request is Python appearing in 84% of jobs. R and SQL feature highly also.

## Acknowledgements

Help with coding a Donut chart - https://medium.com/@krishnakummar/donut-chart-with-python-matplotlib-d411033c960b

Data scraped from - http://Indeed.co.uk

## Requirements

The notebook makes use of several libraries which can be found in Requirements.txt in this repo. This file can be used with pip to install this requirements e.g. pip install -r requirements.txt

## Files

requirements.txt:
    pip requirements file listing packages needed by the jupyter notebook

uk-data-science-job-analysis.ipynb:
    jupyter notebook containing the code for the web scraper, data pre-processing/cleaning and data analysis/visualisations



