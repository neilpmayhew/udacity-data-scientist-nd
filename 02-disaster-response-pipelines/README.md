# Disaster Response Pipeline Project

## Project Summary
This project takes a data set of messages sent during a disaster provided by the company Figure Eight and aims to build a machine learning model to categorise these messages so that they can be responded to promptly to supply the help needed.

The raw csv files were loaded, cleansed and joined together to produce a data set ready to build the machine learning model.

A multi-label classifier was built, tuned using grid search and save to a pickle file.

A flask based web app allows ad-hoc classification of message text and provides visualisations of the data using the plotly library.

## Project Files

- data/
  - etl-pipelines-preparation.ipynb - notebook exploring the data, cleaning/de-duplicating and  writing to database. Working to build function neede in process_data.py
  - process_data.py - script given csv data and database path that will clean and de-duplicate data and write a SQL Lite db to the path supplied
- models/
  - ml-pipeline-preparation.ipynb - notebook used to iteratively build the machine learning model, experimenting with different feature, algorithm and grid search to tune parameters
  - train_classifier.py - script to load dataset from supplied SQL lite db path and build a machine learning pipeline which is tuned using grid search and saved as a pickle file to that file path supplied
- app/
  - run.py - main script for a flask web app allow users to classify a message entered and showing visualisations of the data using the Plotly library
  - /templates/
    - go.html - flask template to format the results from categorising a message 
    - master.html - master flask template providing a textbox to enter a message and button to categorise the message using the saved machine learning model. Visualisations of the data are provided created using the Plotly library

## Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/disaster_messages.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/disaster_response_classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/
