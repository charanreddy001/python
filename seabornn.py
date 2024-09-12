import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Specify the file path
file_path = r'C:\Users\Charan Reddy\Downloads\datasett\customers.csv'
# Load the dataset into a pandas DataFrame
data = pd.read_csv(file_path)

# Preview the first few rows of the dataset
print(data.head())

# Create a scatterplot using seaborn
sns.scatterplot(data=data, x='region', y='purchase_frequency')
plt.show()

# this gives the size of figure
# in this pycharm this decides the size of window
plt.figure(figsize = (10,7))
sns.scatterplot(data = data, x = 'age', y = 'annual_income', hue = 'region',size = 'region')
# you give hue to the column which you want to display in different colours
plt.show()


sns.scatterplot(data = data, x = 'age', y = 'annual_income', hue = 'region',s = 200,alpha =0.6)
plt.show()
