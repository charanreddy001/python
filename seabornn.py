import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Specify the file path
file_path = r'C:\Users\Charan Reddy\Downloads\datasett\customers.csv'
# Load the dataset into a pandas DataFrame
data = pd.read_csv(file_path)

# Preview the first few rows of the dataset
print(data.head())


#                                        SCATTER PLOT MAIN FOCUS
# Create a scatterplot using seaborn
sns.scatterplot(data=data, x='region', y='purchase_frequency')
plt.show()

# this gives the size of figure
# in this pycharm this decides the size of window
plt.figure(figsize = (10,7))
sns.scatterplot(data = data, x = 'age', y = 'annual_income', hue = 'region',size = 'region')
# you give hue to the column which you want to display in different colours
# and also size option to region gives different size to it
plt.show()


sns.scatterplot(data = data, x = 'age', y = 'annual_income', hue = 'region',s = 200,alpha =0.6,style = 'region')
# alpha refers to the transparency with the dots
# style refers to different shapes of region
plt.show()
plt.savefig('seaborne_graph.jpg')

