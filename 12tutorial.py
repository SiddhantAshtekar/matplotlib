import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.dates as mdates
import urllib as ub 

def bytesdate2num(fmt):
	strconverter=mdates.strpdate2num(fmt)
	def bytesconverter(b):
		s=b.decode()
		return strconverter(s)
	return bytesconverter
	

def graph_stocks():
	fig=plt.figure()
	ax1=plt.subplot2grid((1,1),(0,0))

	stock_url='https://pythonprogramming.net/yahoo_finance_replacement'

	source_code=ub.request.urlopen(stock_url).read().decode()

	stock_data=[]

	split_source=source_code.split('\n')

	for line in split_source[1:]:
		split_line=line.split(',')
		if len(split_line) ==7:
			if 'value' not in line and 'labels'not in line:
				stock_data.append(line)

	date,closep,highp,lowp,openp,adj_closep,volume=np.loadtxt(stock_data,delimiter=',',unpack=True,converters={0:bytesdate2num('%Y-%m-%d')})
	ax1.plot_date(date,closep,'-',label='price')
	plt.plot([],[],label='Gain',linewidth=5,color='g',alpha=0.5)
	plt.plot([],[],label='Loss',linewidth=5,color='r',alpha=0.5)
	ax1.fill_between(date,closep,closep[0],where=(closep>closep[0]),facecolor='g',alpha=0.5)
	ax1.fill_between(date,closep,closep[0],where=(closep<closep[0]),facecolor='r',alpha=0.5)
	

	for label in ax1.xaxis.get_ticklabels():
		label.set_rotation(45)

	ax1.grid(True)#,color='g',linestyle='-',linewidth=0.3)

	ax1.xaxis.label.set_color('c')

	ax1.yaxis.label.set_color('r')

	ax1.set_yticks([0,250,500,750,1000])

	plt.xlabel('date')
	plt.ylabel('price')
	plt.title('stock')
	plt.legend()
	plt.subplots_adjust(left=0.09,bottom=0.20,right=0.90,wspace=0.2,hspace=0)
	plt.show()



graph_stocks()
 			
