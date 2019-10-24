import matplotlib.pyplot
import numpy
x_list=[]
y_list=[]
for i in numpy.arange(-10,10,0.2):
	x_list.append(i)
	y_list.append(3*i**3+2*i**2+i)

matplotlib.pyplot.plot(x_list,y_list)