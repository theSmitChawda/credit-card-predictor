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
# Check the first 5 values of the dataset to ensure proper loading
df.head()

# Check for nulls in each column
df.isnull().sum()

# Dataset Description
df.value_counts()

# We dont want any null values in our project hence we drop them
df = df.dropna()

# Check again for nulls in each column
df.isnull().sum()

# Finally check for the number of defaults in the datasets
df['default'].value_counts()