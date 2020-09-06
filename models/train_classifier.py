import sys
import nltk
nltk.download(['punkt', 'wordnet'])

import re
import numpy as np
import pandas as pd
import pickle
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer,TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.multioutput import MultiOutputClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV

from sqlalchemy import create_engine

def load_data(database_filepath):
    '''loads dataframe from database and splits it into X and Y
        returns X,Y, category_names'''
    
    #create sqlite engine
    engine = create_engine('sqlite:///{}'.format(database_filepath))
    
    # read in df from database
    df = pd.read_sql('SELECT* FROM messages',engine) 
    
    #split df into predictor(X) and criterion(Y) variables
    X = df.loc[:,'message'].values
    Y = df.iloc[:,4:].values
    
    # get list of categories
    category_names=df.iloc[:,4:].columns
    
    return X,Y,category_names

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    # build pipeline
    pipeline = Pipeline([
    ('tfidf',TfidfVectorizer(tokenizer=tokenize)),
    ('moc',MultiOutputClassifier(KNeighborsClassifier()))
    ])    
    return pipeline


def evaluate_model(model, X_test, Y_test, category_names):
    # predict on test data
    Y_pred=pipeline.predict(X_test)
    for i in range (Y_test.shape[1]):
    print('The classification report for {} is \n {}'.format(df.columns[(i+4)],classification_report(Y_test[:,i],Y_pred[:,i])))



def save_model(model, model_filepath):
    filename = model_filepath
    pickle.dump(model, open(filename, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()