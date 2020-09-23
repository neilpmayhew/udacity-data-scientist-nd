import sys
sys.path.append("..")


import nltk
nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger'])

import re
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import classification_report,f1_score
from sklearn.multioutput import MultiOutputClassifier
import pickle
from xgboost import XGBClassifier
from disaster_message_components.disaster_message_tokenize import tokenize
from disaster_message_components.starting_verb_extractor import StartingVerbExtractor

def load_data(database_filepath):
    engine = create_engine(f'sqlite:///{database_filepath}')

    df = pd.read_sql('SELECT * FROM message_category',engine)
    X = df.message
    y = df.iloc[:,4:]

    return X,y,y.columns 

def build_model():
    """
    Build an ML pipeline with tfidf and starting verb features.

    An XGBoost classifier is used wrapped in MultiOutputClassier to enable multiple outputs

    A grid search is constructed to


    """
    xgboost_with_starting_verb = Pipeline([
            ('features', FeatureUnion([

                ('text_pipeline', Pipeline([
                    ('vect', CountVectorizer(tokenizer=tokenize)),
                    ('tfidf', TfidfTransformer())
                ])),

                ('starting_verb', StartingVerbExtractor())
            ])),

            ('clf', MultiOutputClassifier(XGBClassifier(objective='binary:logistic')))
        ])

    param_grid = param_test1 = {'clf__estimator__max_depth':range(3,10,2)
                                , 'clf__estimator__min_child_weight':range(1,6,2)}


    gsearch_xgboost_with_starting_verb = GridSearchCV(estimator = xgboost_with_starting_verb,
                            param_grid = param_grid,
                            n_jobs=3, iid=False, 
                            cv=3)

    return gsearch_xgboost_with_starting_verb

def evaluate_model(model, X_test, y_test, category_names):
    """
    Calculate and print overall accuracy and f1 scores followed by a classification report showing metric for each category
    """
    y_pred = model.predict(X_test)
    
    accuracy = (y_test == y_pred).mean().mean()
    f1_samples = f1_score(y_test, y_pred, average='samples')
    f1_weighted = f1_score(y_test, y_pred, average='weighted')
    
    print(f'''
    Overall accuracy      : {accuracy}
    Overall f1 [samples]  : {f1_samples}
    Overall f1 [weighted] : {f1_weighted}
    ''')
        
    labels = [1,0]
    n=0

    for category_name in category_names:

        print(classification_report(y_test.iloc[:,n],y_pred[:,n],labels=labels,target_names=[category_name + '-' + str(v) for v in labels]))

        n+=1

def save_model(model, model_filepath):
    """
    Save the model to a pickle file

    args:

    model:
    the model to save

    model_filepath:
    filepath to write the pickle file to

    """
    pickle.dump(model, open(model_filepath, 'wb'))

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
