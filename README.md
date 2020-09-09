# Disaster Response Pipeline Project

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/


### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Instructions](#instructions)
5. [Results](#results)
6. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

All of the requirements to run the application are captured in the requirements.txt


## Project Motivation<a name="motivation"></a>

For this project I created a Machine Learning Pipeline to correctly classify disaster responses.



## File Descriptions <a name="files"></a>

This project consists of three parts:

1.ETL Pipeline
    - Loads the datasets
    - Merges the two datasets
    - Cleans the data
    - Stores it in a SQLite database

2. ML Pipeline
    - Loads data from the SQLite database
    - Splits the dataset into training and test sets
    - Builds a text processing and machine learning pipeline
    - Trains and tunes a model using GridSearchCV
    - Outputs results on the test set
    - Exports the final model as a pickle file
    
3. Web App
    The web app displays visualization of the dataset that was used for training and validation of the ML-Pipeline.
    The emergency worker can input a message in the web app. By hitting the 'Classify-Message'-button, you get classification results in several categories


You can find the file structure of the product below:
- app
| - template
| |- master.html  # main page of web app
| |- go.html  # classification result page of web app
|- run.py  # Flask file that runs app

- data
|- disaster_categories.csv  # data to process 
|- disaster_messages.csv  # data to process
|- process_data.py
|- InsertDatabaseName.db   # database to save clean data to

- models
|- train_classifier.py
|- classifier.pkl  # saved model 

- README.md

<a name="results"></a>/Users/anna/Desktop/Bildschirmfoto 2020-09-09 um 11.06.34.png 


## Instructions<a name="results"></a>

1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

## Results<a name="results"></a>

The main findings of the code can be found at the post available [here](https://medium.com/@annatrumm/how-tech-makes-women-close-the-gender-pay-gap-2b306de4b965?sk=61e0c51593b98564e5805ad02f2eafcc).

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to FigureEight for the data and Udacity for preparation for the flask web app.

Otherwise, feel free to use the code here as you would like! 