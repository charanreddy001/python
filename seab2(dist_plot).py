import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#                RUGPLOT IS MAIN FOCUS

file_path = r'C:\Users\Charan Reddy\Downloads\datasett\customers.csv'
data = pd.read_csv(file_path)
print(data.head())

sns.rugplot(data=data, x='annual_income',height = 0.6)
# here values given in y-axis is meaningless
plt.show()

sns.rugplot(data = data,x = 'annual_income', y = 'age',height = 0.4)
# here two values ae given for rugplot
# in annual income we have to consider just x-axis another axis is useless
# in age we just have to consider y-axis other axis is useless
plt.show()
#                              DISPLOT
# in displot you can use multiple plots
sns.displot(x = 'annual_income',data = data,kde = True,rug = True,rug_kws = {"height" : 0.2})
plt.show()


#                             HIST PLOT(BASICALLY HISTOGRAM)

sns.set(style = 'dark')
sns.histplot(data = data, x = 'purchase_amount',bins = 100 ) # here bins gives us more detailed graph than original
plt.show()