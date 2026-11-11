import warnings

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
warnings.filterwarnings('ignore')
product_data=[['e-book', 2000], ['plants', 6000], ['Pencil', 3000]]
#2d list, similar to 2d array

indexes=[1,2,3]

columns_name=['product', 'unit_sold']
product_df = pd.DataFrame(data=product_data, index=indexes,
columns=columns_name)

# print(product_df)

# using dictionaries
product_data={'product': ['e-book', 'plants', 'Pencil'], 'unit_sold':
[2000, 5000, 3000]}
product_df = pd.DataFrame(data=product_data)
print(product_df)

# using numpy array
products = np.array([['','product','unit_sold'], [1, 'E-book',2000],
[2, 'Plants', 6000], [3, 'Pencil', 3000]])
product_pf = pd.DataFrame(data=products[1:,1:],index=products[1:,0 ],
columns=products[0,1:])
print(product_pf) # output is same as of first case

df = pd.read_csv('data/dirtydata.csv')
print(df.head(10))

#Print information about the data:
print(df.info())
print(df.isna().sum())
print(df.duplicated())

df = pd.read_csv('data/dirtydata.csv')
new_df = df.dropna()
print(new_df.to_string())


df = pd.read_csv('data/dirtydata.csv')
df.fillna(130)
print(new_df.to_string())

df = pd.read_csv('data/dirtydata.csv')
df["Calories"].fillna(130)

# Calculate the MEAN, and replace any empty values with it:
df = pd.read_csv('data/dirtydata.csv')
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)

# Calculate the MEDIAN, and replace any empty values with it:
df = pd.read_csv('data/dirtydata.csv')
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)

# Calculate the MODE, and replace any empty values with it:
df = pd.read_csv('data/dirtydata.csv')
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)

# Pandas has a to_datetime() method for this:
df = pd.read_csv('data/dirtydata.csv')
df['Date'] = pd.to_datetime(df['Date'], format="mixed")
print(df.to_string())

# Remove rows with a NULL value in the "Date" column:
df.dropna(subset=['Date'], inplace = True)

# Set "Duration" = 45 in row 7:
df.loc[7, 'Duration'] = 45

# If the value is higher than 120, set it to 120:
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

# Delete rows where "Duration" is higher than 120:
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace = True)

# Returns True for every row that is a duplicate, othwerwise False:
print(df.duplicated())

# Remove all duplicates:
df.drop_duplicates(inplace = True)

# Draw a line in a diagram from position (0,0) to position (6,250):
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
plt.plot(xpoints, ypoints)
plt.show()

# Default X-Points
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.show()

# You can use the keyword argument marker to emphasize each point with a
# specified marker:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o')
plt.show()

# Add a plot title and labels for the x- and y-axis:
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()

# The third argument represents the index of the current plot.
plt.subplot(1, 2, 1)
#the figure has 1 row, 2 columns, and this plot is the first plot.
plt.subplot(1, 2, 2)
#the figure has 1 row, 2 columns, and this plot is the second plot.

#Draw 2 plots on top of each other:
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 1, 1)
plt.plot(x,y)
