# Data science blog post project

## Motivation

As I am looking to shift across from my current role as an ETL/Data Engineer and into a Data Science role in the near future I was curious to get an idea of what the UK Data Science job market looks like at the moment.

I wanted to answer three key questions
* What are the most requested skills/technologies for Data Scientist positions?
* Where are Data Scientist roles located across the UK?
* Do roles tend to be permanent or contract/temporary roles

There are no easily obtainable data on current roles so I decided to write a web scraper to gather this myself and analyse to answer my questions.

## Workflow

I began by writing the web scraper, initially experimenting with Selenium as Indeed.co.uk appear to be a dynamic web site that I have found in the past to be less amenable to scraping with Request and BeautifulSoup. 

After some experimentation I was not noticing the skill, location and the other key attributes split out int any way to easily extract. After monitoring the network I noticed a JSON call that returned exactly the data I wanted so I worked created a template web request to retrieve this data for any job_id. Experimented with this request, removing parameter and such I found you could use a very similar URL to return the full job description page, the job description both HTML and plain text could be simply retrieved from here using BeautifulSoup.

With a function written that could pull the specific attribute I wanted from json and also retrieve the job_description just using a job_id I wrote a function to scrape an array of job ids for a supplied search query. Putting all this together I had a solution!

I added two sections one for Pre-Processing and one for exploratory data analysis and began by doing some basic checks for duplicates and missing values plus setting the correct dtypes.

Following this I would do some EDA, note a need for further data cleansing and loop back to Pre-Processing to write the code needed to fix the data.

Finally I wrote up my finding in a blog post which can be found at 

## Requirements

The notebook makes use of several libraries which can be found in Requirements.txt in this repo. This file can be used with pip to install this requirements e.g. pip install -r requirements.txt

## Files

requirements.txt:
    pip requirements file listing packages needed by the jupyter notebook

uk-data-science-job-analysis.ipynb:
    jupyter notebook containing the code for the web scraper, data pre-processing/cleaning and data analysis/visualisations



