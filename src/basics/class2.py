import pandas as pd
import numpy as np
import matplotlib as mplt
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)

data = pd.DataFrame({
    "student": [f"Student {i}" for i in range(1, 21)],
    "study_hours": np.random.randint(1, 10, 20, int), # randint(<lowerLimit>, <higherLimit>, <outputSize>, <outputType>) => generates random int numbers
    "grade": np.random.uniform(5, 10, 20),
    "class": np.random.choice(["A", "B"], 20) # choice(<choicesVector>, <outputSize>) => random choice between the choices inside the vector specified
})

print(data.head(), "\n")

# using GUI framework for visualization
mplt.use('TkAgg') # Tkinter GUI
# mplt.use('QtAgg') # PyQt GUI

plt.style.use('default')

# -- Most Used Graphics MATPLOTLIB --

# Dados simples de exemplo
x = np.arange(1, 11)
y = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
y2 = y + np.random.randint(-3, 3, size=len(y))

# ==================================================
# 1. Gráfico de Linha
# Usado para evolução ao longo do tempo
# ==================================================
plt.figure()
plt.plot(x, y)
plt.title("Gráfico de Linha\nUsado para mostrar evolução ou tendência")
plt.xlabel("Tempo")
plt.ylabel("Valor")
plt.grid(True)
plt.show()

# ==================================================
# 2. Gráfico de Barras
# Usado para comparar categorias
# ==================================================
plt.figure()
plt.bar(x, y)
plt.title("Gráfico de Barras\nUsado para comparar valores entre categorias")
plt.xlabel("Categoria")
plt.ylabel("Valor")
plt.show()

# ==================================================
# 3. Gráfico de Dispersão (Scatter)
# Usado para analisar relação entre duas variáveis
# ==================================================
plt.figure()
plt.scatter(x, y)
plt.title("Gráfico de Dispersão\nUsado para analisar correlação")
plt.xlabel("Variável X")
plt.ylabel("Variável Y")
plt.show()

# ==================================================
# 4. Histograma
# Usado para analisar distribuição de dados
# ==================================================
plt.figure()
plt.hist(y, bins=5)
plt.title("Histograma\nUsado para visualizar distribuição de dados")
plt.xlabel("Valores")
plt.ylabel("Frequência")
plt.show()

# ==================================================
# 5. Boxplot
# Usado para identificar mediana, quartis e outliers
# ==================================================
plt.figure()
plt.boxplot(y)
plt.title("Boxplot\nUsado para analisar dispersão e outliers")
plt.ylabel("Valores")
plt.show()

# ==================================================
# 6. Gráfico de Área
# Usado para mostrar crescimento acumulado
# ==================================================
plt.figure()
plt.fill_between(x, y)
plt.title("Gráfico de Área\nUsado para mostrar valores acumulados")
plt.xlabel("Tempo")
plt.ylabel("Valor")
plt.show()

# ==================================================
# 7. Gráfico de Pizza (Pie)
# Usado para proporção/percentual
# ==================================================
plt.figure()
plt.pie(y[:5], labels=x[:5], autopct="%1.1f%%")
plt.title("Gráfico de Pizza\nUsado para proporções e percentuais")
plt.show()

# ==================================================
# 8. Gráfico com Duas Linhas
# Usado para comparação de séries
# ==================================================
plt.figure()
plt.plot(x, y, label="Série 1")
plt.plot(x, y2, label="Série 2")
plt.title("Comparação de Séries\nUsado para comparar dois comportamentos")
plt.xlabel("Tempo")
plt.ylabel("Valor")
plt.legend()
plt.grid(True)
plt.show()

# ==================================================
# 9. Gráfico de Erro
# Usado quando há incerteza nos dados
# ==================================================
erro = np.random.rand(len(y))
plt.figure()
plt.errorbar(x, y, yerr=erro, fmt='o')
plt.title("Gráfico com Erro\nUsado quando há incerteza na medição")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# -- Most Used Graphics Seaborn

# Configuração visual padrão do seaborn
sns.set(style="whitegrid")

# Dados simples
dados = pd.DataFrame({
    "Tempo": np.arange(1, 11),
    "Valor": [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
    "Grupo": ["A"]*5 + ["B"]*5
})

dados["Valor2"] = dados["Valor"] + np.random.randint(-3, 3, size=10)

# ==================================================
# 1. Gráfico de Linha
# Usado para evolução ao longo do tempo
# ==================================================
sns.lineplot(data=dados, x="Tempo", y="Valor")
plt.title("Line Plot\nUsado para mostrar evolução ou tendência")
plt.show()

# ==================================================
# 2. Gráfico de Barras
# Usado para comparar categorias
# ==================================================
sns.barplot(data=dados, x="Tempo", y="Valor")
plt.title("Bar Plot\nUsado para comparar valores entre categorias")
plt.show()

# ==================================================
# 3. Gráfico de Dispersão
# Usado para analisar relação entre variáveis
# ==================================================
sns.scatterplot(data=dados, x="Tempo", y="Valor")
plt.title("Scatter Plot\nUsado para analisar correlação")
plt.show()

# ==================================================
# 4. Histograma
# Usado para analisar distribuição dos dados
# ==================================================
sns.histplot(data=dados, x="Valor", bins=5)
plt.title("Histogram\nUsado para visualizar distribuição")
plt.show()

# ==================================================
# 5. Boxplot
# Usado para identificar mediana e outliers
# ==================================================
sns.boxplot(data=dados, y="Valor")
plt.title("Boxplot\nUsado para analisar dispersão e outliers")
plt.show()

# ==================================================
# 6. Violin Plot
# Usado para ver distribuição + densidade
# ==================================================
sns.violinplot(data=dados, y="Valor")
plt.title("Violin Plot\nDistribuição e densidade dos dados")
plt.show()

# ==================================================
# 7. Gráfico de Área
# Usado para crescimento acumulado
# ==================================================
sns.lineplot(data=dados, x="Tempo", y="Valor")
plt.fill_between(dados["Tempo"], dados["Valor"], alpha=0.3)
plt.title("Area Plot\nUsado para valores acumulados")
plt.show()

# ==================================================
# 8. Comparação de Séries
# Usado para comparar comportamentos
# ==================================================
sns.lineplot(data=dados, x="Tempo", y="Valor", label="Série 1")
sns.lineplot(data=dados, x="Tempo", y="Valor2", label="Série 2")
plt.title("Multiple Line Plot\nComparação entre séries")
plt.show()

# ==================================================
# 9. Gráfico de Correlação
# Usado para ver relação entre múltiplas variáveis
# ==================================================
sns.heatmap(dados[["Tempo", "Valor", "Valor2"]].corr(), annot=True)
plt.title("Heatmap de Correlação\nRelação entre variáveis")
plt.show()

# ==================================================
# 10. Gráfico de Contagem
# Usado para contar ocorrências por categoria
# ==================================================
sns.countplot(data=dados, x="Grupo")
plt.title("Count Plot\nUsado para contagem de categorias")
plt.show()
