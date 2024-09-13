import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


file_path = r'C:/Users/Charan Reddy/Downloads/Datasett/customers.csv'
data = pd.read_csv(file_path)


#                                  JOINT PLOT
sns.jointplot(data = data, x ='region', y = 'annual_income')
plt.show()

sns.jointplot(data = data, x ='annual_income', y = 'annual_income',kind = 'kde')
plt.show()

# this gives all type of graphs from data
sns.pairplot(data = data)
plt.show()


g = sns.PairGrid(data)
g = g.map_upper(sns.scatterplot)
g = g.map_diag(sns.boxplot)
g = g.map_lower(sns.violinplot,color = 'red')
plt.show()