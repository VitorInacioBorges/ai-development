from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import pandas as pd

# Columns = PassengerId	/ Survived / Pclass /	Name / Sex / Age / SibSp / Parch / Ticket / Fare / Cabin / Embarked
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"

df = pd.read_csv(url)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1}) 

X = df.drop(columns=["PassengerId", "Pclass", "Name", "Ticket", "Cabin", "Fare", "SibSp", "Parch", "Embarked"])
Y = df['Survived']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.45, random_state=42, stratify=Y
)

algoritmo = GaussianNB()
algoritmo.fit(X_train, Y_train)

Y_pred = algoritmo.predict(X_test)

accuracy = accuracy_score(Y_test, Y_pred)
print("Acurácia:", accuracy)