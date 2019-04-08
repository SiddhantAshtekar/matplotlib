import matplotlib.pyplot as plt 
x=[2,4,6,8,10]
y=[6,7,8,2,4]
x1=[1,3,5,7,9]
y1=[7,4,6,7,8]
plt.bar(x,y, label='Bars1' , color='b')
plt.bar(x1,y1, label ='Bars2' , color='c')
plt.xlabel('x')
plt.ylabel('y')
plt.title('intresting graph\n check out')
plt.legend()
plt.show()
