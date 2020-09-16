import sys
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """
    Loads message and category data from csv files paths and return a pandas data frame of the the two datasets joined on id

    Args:
        messages_filepath
            fil path to messages csv file
        categories_filepath
            file path to categories csv fil
    Returns:
        pandas data frame
    """
    messages   = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories, on='id')
    return df 


def clean_data(df):
    """
    cleans the data, splitting category string out into numeric column that take a value of 0 or 1

    Args:
       df:
          a data frame of message and category csvs merged together
    """
    # create a dataframe of the 36 individual category columns
    categories = df.categories.str.split(';', expand=True)

    # select the first row of the categories dataframe
    row = categories.loc[0,:].values

    # use this row to extract a list of new column names for categories.
    # using a list comprehension
    category_colnames = [x[:-2] for x in row]

    # rename the columns of `categories`
    categories.columns = category_colnames

    # iterate over columns keep only the last char (which will be 1 or 0)
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].astype(str).str[-1]

        # convert column from string to numeric
        categories[column] = categories[column].astype(int)

    # drop the original categories column from `df`
    df = df.drop('categories', axis='columns')

    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], axis='columns')

    # drop duplicates
    df = df.drop_duplicates()

    return df
def save_data(df, database_filename):

    engine = create_engine(f'sqlite:///{database_filename}')
    df.to_sql('message_category', engine, index=False)
    
def main():
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
