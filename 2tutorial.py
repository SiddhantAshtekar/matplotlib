import matplotlib.pyplot as plt 
x=[1,2,3]
y=[5,7,4]
x1=[1,2,3]
y1=[10,14,12]
plt.plot(x,y,label='first line')
plt.plot(x1,y1,label='second line')
plt.xlabel('plot number')
plt.ylabel('important var')
plt.title('intresting graph')
plt.legend()
plt.show()