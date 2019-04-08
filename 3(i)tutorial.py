import matplotlib.pyplot as plt 
population_age=[22,55,45,42,74,32,54,21,41,11,20,28,73,29]
# ids=[x for x in range(len(population_age))]  

bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]

# plt.bar(ids,population_age, label='bars')
plt.hist(population_age,bins,histtype='bar' , rwidth=0.8)
plt.ylabel('population_age')
plt.xlabel('ids')
plt.title('population graph')
plt.legend()
plt.show()



