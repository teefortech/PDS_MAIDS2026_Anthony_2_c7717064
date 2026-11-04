a = 1
b = 3
print(a + b)



x = 7

if x > 5:
    print("Valid")

# Task 1: Environment Setup
print('Week 1 – Code Quality Lab')

# Task 2: Understanding Poor Code
def calc(a,b,c=[]):
 x=0
 for i in a:
  if(i>10):
   x=x+i
  else:
   x=x-1
 if b==True:print("Result is:",x)
 return x

data=[1,5,12,20,3]
result=calc(data,True)
print(result)
# Question 1: Can you easily identify logic blocks?
# Answer: Not easily. The indentation is inconsistent, and the
# single-line if statement makes the logic harder to follow.

# Question 2: Are variable names meaningful?
# Answer: Mostly no. Names such as a, b, c, x and i do not clearly
# describe their purposes. However, data and result are clearer.

# Question 3: Would this code be easy to debug?
# Answer: No. Unclear variable names, poor formatting and the unused
# parameter c make the code harder to understand and debug.

# Reformating the above code using ctrl + Alt + L
def calc(a, b, c=[]):
    x = 0
    for i in a:
        if (i > 10):
            x = x + i
        else:
            x = x - 1
    if b == True: print("Result is:", x)
    return x


data = [1, 5, 12, 20, 3]
result = calc(data, True)
print(result)

# 3.Add comments, rename variables and adjust formatting to improves readability.
def calculate_result(numbers, show_result=False):
    total = 0

    # Add numbers greater than 10; subtract 1 for each other number.
    for number in numbers:
        if number > 10:
            total += number
        else:
            total -= 1

    # Display the total when requested.
    if show_result:
        print("Result is:", total)

    return total


# Calculate and display the result for the sample data.
sample_numbers = [1, 5, 12, 20, 3]
result = calculate_result(sample_numbers, show_result=True)
print(result)

# Task 4: Comments & Docstrings
def calculate_result(numbers, show_result=False):
    """Return the sum of values above 10, minus 1 for each remaining value.

    Print the total as well if show_result is True.
    """
    total = 0

    for number in numbers:
        if number > 10:
            total += number
        else:
            total -= 1  # Each value at or below 10 carries a fixed penalty.

    if show_result:
        print("Result is:", total)

    return total


sample_numbers = [1, 5, 12, 20, 3]
result = calculate_result(sample_numbers, show_result=True)
print(result)


# Reflection: What is one thing you learned about code quality today?
# Meaningful names and clear formatting make code easier to understand,
# while useful comments explain decisions that may not be obvious.

# Reflection: Why might poor code affect data analysis results?
# Unclear code can hide errors in calculations or data processing,
# producing inaccurate results and misleading conclusions.


# Tutorial : 1.2
import pandas as pd
import seaborn as sns
iris = sns.load_dataset('iris')

print(iris.shape)
print(iris.columns)
print(iris.dtypes)
print(iris.info)

# Task 4: Data Selection and Indexing
# Select the first row
print(iris.iloc[0])

# Select rows 10 to 20
print(iris.iloc[10:20])

# Select two specific columns
print(iris[['sepal_length', 'petal_length']])