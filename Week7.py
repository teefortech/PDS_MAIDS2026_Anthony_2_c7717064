import random
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

# Draw 6 plots:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 1)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 2)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 3)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 4)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 5)
plt.plot(x,y)
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 6)
plt.plot(x,y)
plt.show()

# With Pyplot, you can use the scatter() function to draw a scatter plot
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')
plt.show()

# In addition you have to create an array with values (from 0 to 100), one value for
# each point in the scatter plot:
import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar()
plt.show()

# The bar() function takes arguments that describes the layout of the bars
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, color = "red")
plt.show()

# Example: Say you ask for the height of 250 people, you might end up with a
# histogram like this:
# In Matplotlib, we use the hist() function to create histograms.
# The hist() function will use an array of numbers to create a histogram, the array is
# sent into the function as an argument.
# For simplicity we use NumPy to randomly generate an array with 250 values, where
# the values will concentrate around 170, and the standard deviation is 10

x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()
# With Pyplot, you can use the pie() function to draw pie charts. By default the
# plotting of the first wedge starts from the x-axis and moves counterclockwise:
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show()

# Normal Distribution
sns.distplot(random.normal(size=1000), hist=False)
plt.show()
# importing packages
import seaborn as sns
# loading dataset
data = sns.load_dataset("iris")
# draw lineplot
sns.lineplot(x="sepal_length", y="sepal_width", data=data)
