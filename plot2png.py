#!/usr/bin/python 
import matplotlib.pyplot as plt

data = [ 1,2,3,4,13,43,23,21,9,4,65,71,12,1,3,5,2]
plt.hist(data)

plt.show()

plt.savefig('testplot.png')
