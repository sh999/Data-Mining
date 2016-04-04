'''
Bayesian classifier for car data
'''
classifications = ["unacc","acc","good","vgood"]
buying = ["vghigh","high","med","low"]
maint = ["vghigh","high","med","low"]
doors = ["2","3","4","5more"]
persons = ["2","4","more"]
lug_boot = ["small","med","big"]
safety = ["low","med","high"]
inputfile = open("small.data")
attributes = [classifications, buying, maint, doors, persons, lug_boot, safety]

small = "med,low,3,more,big,low,unacc"
'''
pseudocode:
For each line in file:
	Look at the last attribute for classification; remember this
	For each attribute:

Sample data structure:
unacc = 10
	   buying = 
	   		   vhigh = 3
	   		   high  = 4
	   		   med   = 1
	   		   low   = 2
	   maint = 
	   		   vhigh ...
	   doors = 
	   .
	   .
	   .
	   safety = 
	           low = 9
	           med = 1
	           high = 0
acc = 32
		.
		.
		.
		.
good = 

'''

