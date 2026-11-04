try:
df = pd.read_csv("missing_file.csv")
except FileNotFoundError:
print("File does not exist.")

ry:
df = pd.read_csv("data.csv")
except Exception as e:
print("Something went wrong:", e)