import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score

# HOW TO USE:
    # 1. Create an object of the class
    #       m1 = ML_RandomForest()
    # 2. Use either predict() function OR predict_verbose() function as required
    #       prediction = m1.predict(33,1,9,4,29,13.8,1.348674,2.653326)
    #       m1.predict_verbose(33,1,9,4,29,13.8,1.348674,2.653326)

class ML_RandomForest:
    df=0
    x=0
    y=0
    train_x=0
    test_x=0
    train_y=0
    test_y=0
    number_of_trees=100
    classifier=0
    
    test_obj =np.array([0,0])
    user_df=0
    
    def __init__(self):        
        df = pd.read_csv('../input/credit-risk-analysis-for-extending-bank-loans/bankloans.csv')
        df = df.dropna()
        x = df.drop(['default'],axis=1)
        y = df['default']
        train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=42)
        number_of_trees = 200
        classifier = RandomForestClassifier(n_estimators=number_of_trees)
        classifier.fit(train_x, train_y)
        classifier.score(test_x,test_y)
        test_obj =np.array([0,0])
    
    def __str__(self):
        return f"Credit card prediction model by Smit Chawda"

    def score_mean(self):
        val_score = cross_val_score(estimator=classifier,X=train_x, y=train_y,cv=10)
        return val_score.mean()

    def predict_test(self):
        return classifier.predict(test_x)
    
    def print_test_x_data(self):
        print(test_x)
    
    def predict(self, age, ed, employ, address, income, debtinc, creddebt, othdebt):
        test_obj = np.array([[age,ed,employ,address,income,debtinc,creddebt,othdebt]])
        return classifier.predict(test_obj)
    
    def predict_verbose(self, age, ed, employ, address, income, debtinc, creddebt, othdebt):
        pred = self.predict(age, ed, employ, address, income, debtinc, creddebt, othdebt)
        if pred==0:
            print('The user is NOT expected to default on the payments')
        else:
            print('The user is expected to default on the payments')
        