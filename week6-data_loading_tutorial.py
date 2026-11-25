import pandas as pd

try:
    df = pd.read_csv("missing_file.csv")
except FileNotFoundError:
    print("File does not exist.")

try:
    df = pd.read_csv("data.csv")
except Exception as e:
    print("Something went wrong:", e)

    # C:\Users\c7717064\Downloads

   # C:\Users\c7717064\Downloads

File_object = open(r"data.csv")
print(File_object.read())

# Change directory: you can create a new folder inside your project directory.
import os
print(os.getcwd(),)
os.chdir("new_folder")

# Use pathlib (modern approach):
# Create a folder name it to “data” and then put “data.csv” inside it.
from pathlib import Path
file_path = Path("data") / "data.csv"
# df = pd.read_csv(file_path)
# print(df)

df = pd.read_csv("data.csv")
3# For data validation, you can use these helper functions to get more information about your
# dataset. Make sure you use print() statement for each method.
df.shape
df.info()
df.isna().sum()
df.dtypes

# Task 4: JSON Normalization
# Instead of basic .to_json(), show nested JSON:
import json
data = {
"user": {
"name": "Alice",
"scores": [80, 90, 85]
}
}
# Then flatten it:
print(pd.json_normalize(data))

# Task 5: Automating File Processing
sample_data_path = "C:/Users/USER/PycharmProjects/PDS_MAIDS2026_Anthony_2_c7717064/data"
files = [os.path.join(sample_data_path, f) for f in os.listdir(sample_data_path) if
f.endswith(".csv")]
dfs = [pd.read_csv(file) for file in files]
# Check if the dfs list is not empty before attempting to concatenate
if dfs:
    combined = pd.concat(dfs)
    print(combined)
else:
    print("No CSV files found in the directory to concatenate.")
