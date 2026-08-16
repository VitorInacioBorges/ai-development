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

# print(data.head(), "\n")

# using GUI framework for visualization
mplt.use('TkAgg') # Tkinter GUI
# mplt.use('QtAgg') # PyQt GUI

plt.style.use('default')

# -- Histogram / Distribution --

sns.histplot(data["grade"])
plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Frequency")
plt.show()

# -- Boxplot --

sns.boxplot(x="class", y="grade", data=data)
plt.title("Grade Comparison by Class")
plt.xlabel("Class")
plt.ylabel("Grade")
plt.show()