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