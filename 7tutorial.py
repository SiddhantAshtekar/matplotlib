import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('example.txt','r') as csv_file:
	plots=csv.reader(csv_file,delimiter=',')
	for row in plots:
		x.append(int(row[0]))
		y.append(int(row[1]))
plt.plot(x,y,label='loded file!')
plt.xlabel=('x')
plt.ylabel=('y')
plt.title('x vs y')
plt.legend()
plt.show()