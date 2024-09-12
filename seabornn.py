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

# Show the plot
plt.show()
