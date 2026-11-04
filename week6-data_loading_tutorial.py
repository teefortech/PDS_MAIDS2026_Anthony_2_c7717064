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

File_object = open(r"data(2).csv")
print(File_object.read())