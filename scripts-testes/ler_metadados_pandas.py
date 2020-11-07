import pandas as pd

# open file
filename = "./fotos-teste/grade_fotos.csv"
df = pd.read_csv(filename, sep=";")
print(df.head(3), "\n")

for i in range(len(df.arquivo)):
    print(df.arquivo[i])