# -*- coding: utf-8 -*-
"""Welcome To Colab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

import numpy as np

df=pd.read_excel('/content/drive/MyDrive/employee_burnout_.xlsx')

df.head()#print first five columns

df.info()#to view thr information like number of null values in a column

import matplotlib.pyplot as plt

import seaborn as sns

df.describe()

# @title Default title text
# Handle missing values for numeric columns only
numeric_columns = df.select_dtypes(include=np.number).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Encode categorical variables, handling unknown values
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1}).fillna(-1) # Fill unmapped values with -1
df['WFH Setup Available'] = df['WFH Setup Available'].map({'No': 0, 'Yes': 1}).fillna(-1) # Fill unmapped values with -1

# Select features and target variable
X = df[['Designation', 'Resource Allocation', 'Mental Fatigue Score', 'Gender', 'WFH Setup Available']]
y = df['Burn Rate']

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

sns.pairplot(df)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the results
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
results = {
    "Mean Squared Error": mse,
    "R-squared": r2,
    "Coefficients": coefficients
}

results



