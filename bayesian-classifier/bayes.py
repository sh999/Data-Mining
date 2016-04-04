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

{unacc:{count:10,buying:{vhigh:3,high:4...},maint:{vhigh...},...,acc:{count:32,buying:{......}}}

'''
small = ["vhigh,low,3,more,big,low,unacc","low,vhigh,5more,4,big,high,acc"]
small = small.split(",")
print "small:",small
unacc = {'count':10,
	 'buying':{'vhigh':3,'high':7},
	 'maint':{'vhigh':2,'high':8}
	 }
acc = {'count':6,
	 'buying':{'vhigh':3,'high':3},
	 'maint':{'vhigh':2,'high':4}
	 }
print "before:\n", unacc
c = small[-1]
unacc['buying'][small[0]] += 1
print "after:\n", unacc



