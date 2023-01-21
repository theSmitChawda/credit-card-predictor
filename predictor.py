import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score

df = pd.read_csv('../input/credit-risk-analysis-for-extending-bank-loans/bankloans.csv')

# We dont want any null values in our project hence we drop them
df = df.dropna()

# Finally check for the number of defaults in the datasets
df['default'].value_counts()

x = df.drop(['default'],axis=1)
y = df['default']

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=42)

classifier = RandomForestClassifier(n_estimators=number_of_trees)
classifier.fit(train_x, train_y)
classifier.score(test_x,test_y)

print("Prediction: ")
print(classifier.predict(test_x))

val_score = cross_val_score(estimator=classifier,X=train_x, y=train_y,cv=10)
val_score.mean()