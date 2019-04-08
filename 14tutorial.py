import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc

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
	
	x=0
	y=len(date)
	ohlc=[]
	while x<y:
		append_me=date[x],closep[x],highp[x],lowp[x],openp[x],adj_closep[x],volume[x]
		ohlc.append(append_me)
		x+=1

	candlestick_ohlc(ax1,ohlc)

	ax1.tick_params(axis='x',colors='#f06215')
	plt.xlabel('date')
	plt.ylabel('price')
	plt.title('stock')
	plt.legend()
	plt.subplots_adjust(left=0.09,bottom=0.20,right=0.90,wspace=0.2,hspace=0)
	plt.show()



graph_stocks()
 			
