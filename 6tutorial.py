import matplotlib.pyplot as plt 

days=[1,2,3,4,5]

sleeping= [7,8,6,11,7]
eating=	  [2,3,4,3,2]
working=  [7,8,7,2,2]
playing=  [8,5,7,8,13]

slices=[7,2,2,13]
activities=[sleeping,eating,working,playing]
color=['b','c','r','g']
plt.pie(slices,
	labels=activities,
	colors=color,
	startangle= 90,
	shadow=True,
	explode=(0,0,0,0.05),
	autopct='%1.1f%%')
# plt.ylabel('x')
# plt.xlabel('y')
plt.title('stack graph')
# plt.legend()
plt.show()
