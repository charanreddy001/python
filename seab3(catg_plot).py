import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

file_path = r'C:/Users/Charan Reddy/Downloads/Datasett/customers.csv'
data = pd.read_csv(file_path)

data.hist(edgecolor = 'green',linewidth = 1.7, figsize = (7,6.510))#(length,width)
plt.show()

#                                 BOX PLOT
sns.boxplot(x = 'region', y = 'loyalty_score',data = data,width = 0.3)
# bro mana data ki box plot sarigga ravatle
# but if you change values of x and y you will get
# in x you need to give some fixed values which will repeat the same
plt.show()


#                                  COUNT PLOT
plt.figure(figsize = (10,4), dpi = 100) # dpi(dots per inches) will make the picture more clarity
sns.countplot(x = 'region',data = data,hue = 'purchase_amount')
plt.show()
