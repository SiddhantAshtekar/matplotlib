import matplotlib.pyplot as plt 

days=[1,2,3,4,5]

sleeping= [7,8,6,11,7]
eating=	  [2,3,4,3,2]
working=  [7,8,7,2,2]
playing=  [8,5,7,8,13]

plt.plot([],[],color='m',label='sleeping')
plt.plot([],[],color='c',label='eating')
plt.plot([],[],color='b',label='working')
plt.plot([],[],color='k',label='playing')
plt.stackplot(days, sleeping, eating, working,playing, colors=['m','c','b','k'])
plt.ylabel('x')
plt.xlabel('y')
plt.title('stack graph')
plt.legend()
plt.show()
