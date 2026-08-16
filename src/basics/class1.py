import numpy as np
import pandas as pd

# -- First Language Test --

print("Hello World\n")

def greetings():
    print("Hello World 2\n")

greetings()

# -- Activity 1 --

vet = np.array([21, 42, 1, 463, 234])

def results():
    print("Média Vetor: ", vet.mean())
    print("Maior Valor: ", vet.max())
    print("Menor Valor: ", vet.min())
    print("\n")

    if vet.mean() < 100 :
        print("média menor que 100\n")
    else :
        print("média maior ou igual a 100\n") 

results()

# -- Pandas Dataframe --

data = {
    "name": ["Vitor", "Vitor2", "Vitor3"],
    "age": [18, 19, 20],
    "grade": [8.2, 9.0, 8.9]
}

df = pd.DataFrame(data)

print("Raw Table:\n\n", data, "\n")
print("Dataframe:\n\n", df)
print(df.head())
print(df.info())
print(df.describe())

# df.head() => table head
# df.info() => table info
# df.describe() => statistics on this table

# -- Excel Pandas Dataframe --

# df_excel = pd.read_excel("data.xlsx")

# url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
# df_git = pd.read_csv(url)

