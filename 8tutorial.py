import matplotlib.pyplot as plt
import numpy as np
import urllib 
import matplotlib.dates as mdates

def bytespdate2num(fmt):
	strconverter=mdates.strpdate2num(fmt)
	def bytesconverter(b):
		s= b.decode()
		return strconverter(s)
	return bytesconverter

def graf_data():
	stock_price_url='https://pythonprogramming.net/yahoo_finance_replacement'

	source_code=urllib.request.urlopen(stock_price_url).read().decode()

	stock_data=[]

	split_source=source_code.split('\n')

	for line in split_source[1:]:
		split_line=line.split(',')
		if len(split_line) == 7:
			if 'value' not in line:
				stock_data.append(line)

	date,closep,highp,lowp,openp,adj_closep,volume=np.loadtxt(stock_data,delimiter=',',unpack=True,converters={0:bytespdate2num('%Y-%m-%d')})

	plt.plot_date(date,closep,'-',label='price')
	plt.xlabel('date')
	plt.ylabel('price')
	plt.title('stock')
	plt.legend()
	plt.show()






graf_data()