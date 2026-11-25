#Importing libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

#Read the datasets
dataset=pd.read_csv("weight-height.csv")
#Check the dataset
dataset.head()

#check if null values is present in dataset or not.....
dataset.isnull().sum()
#Checking the dimensions of the dataset

#Plot Gender vs Weight............
x1 = dataset.iloc[:, 0].values
y1 = dataset.iloc[:, 2].values
plt.scatter(x1,y1,label='Gender',color='Green',s=50)
plt.xlabel('Gender')
plt.ylabel('Weight')
plt.title('Gender vs Weight')
plt.legend()
plt.show()

#Plot Height vs Weight............
x2 = dataset.iloc[:, 1].values
y2 = dataset.iloc[:, 2].values
plt.scatter(x2,y2,label='Height',color='Orange',s=50)
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Height vs Weight')
plt.legend(loc="lower right")
plt.show()

#separating the dependent and independent values....
#X-Independent variable
X = dataset.iloc[:, 1:2].values
print(X)

#y-dependent or target variable
y = dataset.iloc[:, 2].values
print(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
random_state=123)

#Creating linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
#predicting the test set
y_pred = regressor.predict(X_test)

#Step 4-Checking the accuracy

# Predicting the Test set results
y_pred = regressor.predict(X_test)
print('Coefficients: ', regressor.coef_)
# The mean squared error
print("Mean squared error: %.2f" % np.mean((regressor.predict(X_test) -
y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regressor.score(X_test, y_test))

# Part 2
import pandas as pd

data = {
    "Hours_Studied": [1,2,3,4,5,6,7,8,9,10],
    "Exam_Score": [40,42,50,55,60,65,70,75,85,90]
}

df = pd.DataFrame(data)

print(df)

import matplotlib.pyplot as plt

plt.scatter(df["Hours_Studied"], df["Exam_Score"])
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Study Hours vs Exam Score")
plt.show()

X = df[["Hours_Studied"]]
y = df["Exam_Score"]

# Task 4 – Split the Dataset
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Task 5 – Train the Model
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

# Task 6 – Make Predictions
predictions = model.predict(X_test)

print(predictions)

# Task 7 – Evaluate the Model
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Mean Squared Error:", mse)

print("R² Score:", r2)

# Task 8 – Visualise the Regression Line
plt.scatter(X, y)

plt.plot(X, model.predict(X), color="red")

plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")

plt.show()

# Task 9 – Make a Prediction
# Predict the exam score for a student who studies 7.5 hours.
model.predict([[7.5]])





