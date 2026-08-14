from sklearn.datasets import load_wine # base de dados de vinhos com 13 caracteristicas
from sklearn.linear_model import Perceptron # algoritmo perceptron
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix # matriz confusao
from sklearn.tree import DecisionTreeClassifier
from sklearn.

X, y = load_wine(return_X_y=True)

# print(x[0], y[0])
# for i in wine.feature_names:
  # print(i)

perc = Perceptron(random_state=64)
score = cross_val_score(perc, X, y, cv=5)
predict = cross_val_predict(perc, X, y, cv=5)
cm = confusion_matrix(y, predict)

tree = DecisionTreeClassifier(random_state=64)
score2 = cross_val_score(tree, X, y, cv=5)
predict2 = cross_val_predict(tree, X, y, cv=5)
cm2 = confusion_matrix(y, predict2)

knn =  KNeighborsClassifer(n_neighbors=5)
score3 = cross_val_score(knn, X, y, cv=5)
predict3 = cross_val_predict(knn, X, y, cv=5)
cm3 = confusion_matrix(y, predict3)

print(score3.mean())
print(cm2)

# escolher o algoritmo ideal e dificil

# o maior problema hoje não e o aperfeicoamento de classificacao de dados, mas
# sim a qualidade de um banco de dados