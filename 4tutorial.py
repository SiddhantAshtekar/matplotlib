import matplotlib.pyplot as plt 
x=[1,3,6,7,8,4,3,2]
y=[1,2,3,4,5,6,7,8]
plt.scatter(x,y,label='skitscat',color='r',s=1000,marker='x')
plt.ylabel('population_age')
plt.xlabel('ids')
plt.title('population graph')
plt.legend()
plt.show()


