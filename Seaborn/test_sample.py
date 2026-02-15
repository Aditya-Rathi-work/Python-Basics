import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0, 10, 100)
y = np.sin(x)

df = pd.DataFrame({"x": x, "y": y})

sns.lineplot(data=df, x="x", y="y")

plt.show()