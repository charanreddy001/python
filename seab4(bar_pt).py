import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


file_path = r'C:/Users/Charan Reddy/Downloads/Datasett/customers.csv'
data = pd.read_csv(file_path)

plt.figure(figsize = (5,5), dpi = 120)
sns.barplot(data = data, x = 'loyalty_score',y = 'purchase_amount',errorbar = 'sd', estimator = np.mean)
plt.show()

#                                  VIOLIN PLOT
# violin plot is combination of default =  box plot and KDE (density at that point)
# search 'kde' in google and see pictures
# in graph we see that at which point we have density
# as in box plot we can see 25%, middle(50%), 75% by this marking we can see density at that point
sns.violinplot(data = data, x = 'region', y = 'purchase_amount',hue = 'region')
plt.show()
# split divides that symmetry figure into a single
sns.set(style = 'dark')
sns.violinplot(data = data, x = 'region', y = 'purchase_amount',hue = 'region',split = True)
plt.show()
# we can change inner things by:
sns.violinplot(data = data, x = 'region', y = 'purchase_amount',hue = 'region', inner = 'quartile')
plt.show()
# another type
sns.violinplot(data = data, x = 'region', y = 'purchase_amount',hue = 'region',inner = 'stick')
plt.show()