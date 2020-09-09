

import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from langdetect import detect


def load_data(messages_filepath, categories_filepath):
 
    """loads datasets and merges them

    Args:
    message_filepath: str, filepath to the messages data
    categories_filepath: str, filepath to the categories data
    
    Returns:
    merged dataframe
    """
    
    #load message filepath
    messages=pd.read_csv(messages_filepath)
    
    # load categories filepath
    categories=pd.read_csv(categories_filepath)
   
    #merge both datasets
    df=pd.merge(messages,categories, on='id')

    return df

def clean_data(df):
     """Reads in and cleans dataframe from NaNs in the salary column of Stackoverflow Survey data

    Args:
    df: DataFrame, dataframe which has to be cleaned
    
    Returns:
    cleaned dataframe
    """
   
    # create a dataframe of the 36 individual category columns
    categories = df.categories.str.split(';',expand=True)
    # select the first row 
    row = categories.iloc[0]
    # use this row to extract a list of new column names for categories.
    category_colnames = [x[:-2] for x in row]
    # rename the columns of `categories`
    categories.columns = category_colnames
    
    for column in categories:
    # set each value to be the last character of the string
        categories[column]= categories[column].str.strip().str[-1]   
    # convert column from string to numeric
        categories[column] = categories[column].astype(int) 
    
    # drop the original categories column from `df`
    df.drop(['categories'],axis=1, inplace=True)
    
    # concatenate the original dataframe with the new `categories` dataframe
    df =  pd.concat([df, categories], axis=1)
    
    # drop duplicates
    df.drop_duplicates(inplace=True)
    
    # drop 'child_alone' column
    df.drop(['child_alone'],axis=1,inplace=True)
    
    # drop columns that are not detected as english language
    for col in df.message:
        try:
            language=detect(col)
            index_list=[]
            if language != 'en':
                df.drop(df[df['message'] == col],inplace=True)
        except:
            pass
    
    return df

def save_data(df, database_filename):
     """saves dataframe into sqlite database

    Args:
    df: DataFrame, dataframe 
    database_filename: str., name of the database
  
    """
    
    #create engine
    engine = create_engine('sqlite:///{}'.format(database_filename))
    
    #save df to sqlite database
    df.to_sql('messages', engine, index=False,if_exists='replace')


def main():
    """executes code and prints status while executing the steps of the program
    """
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()