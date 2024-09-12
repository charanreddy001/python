import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(start = -10,stop = 10,num = 400)
m = 2
c = 3
y = m*x + c

# plotting
plt.plot(x,y,label = 'y = 2*x + 3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('2x + 3')
plt.grid()
plt.legend()
plt.show()

a = 1
b = -4
c = 4
x = np.linspace(start = -10,stop = 10,num = 400)
y = a * x **2 + b * x + c
plt.plot(x,y,label = 'y = 2*x + 3')
plt.xlim(0,5)
plt.ylim(-10,10)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('2x + 3')
plt.grid(False) # if nothing was passed into it default value will be taken as True and grid will be drawn
plt.show()