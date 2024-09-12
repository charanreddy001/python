import matplotlib.pyplot as plt
from unicodedata import category

plt.plot([1,2,3,4],[10,20,30,40],color = 'red',label = 'x plot',linewidth = 2,linestyle ='-',marker = 'd')
plt.plot([1,2,3,4],[40,30,20,10],label = 'y_plot',color = "purple",linewidth = 4,linestyle = '--')
plt.legend()
plt.show()
plt.plot([4,5,6,7,8],[20,40,50,60,70],marker = 'o',markersize = 10, markerfacecolor = 'yellow')
plt.show()

#  BAR GRAPHS

categories = ['cat A','cat B', 'cat C']
values = [10,20,60]

plt.bar(categories,values,color = 'green',width = 0.4)
plt.title('time pass yevvaralu')
plt.xlabel('categories')
plt.ylabel('values')
plt.grid(True,color = 'black',linestyle = '--')

plt.show()


categories = ['cat A','cat B', 'cat C']
values = [10,20,60]

plt.barh(categories,values,color = 'green') # if we place barh graph will be horizontal
plt.title('time pass yevvaralu')
plt.xlabel('categories')
plt.ylabel('values')
plt.grid(True,color = 'black',linestyle = '--')

plt.show()
categ = ['Category A', 'Category B', 'Category C']
values1 = [10, 15, 7]
values2 = [5, 3, 2]

# Creating stacked bar graph
plt.bar(categ, values1, label='Part 1')
plt.bar(categ, values2, bottom=values1, label='Part 2')

# Adding title, labels, and legend
plt.title('Stacked Bar Graph')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.legend()

# Show plot
plt.show()