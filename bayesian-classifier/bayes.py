'''
Bayesian classifier for car data
'''
'''
classifications = ["unacc","acc","good","vgood"]
buying = ["vghigh","high","med","low"]
maint = ["vghigh","high","med","low"]
doors = ["2","3","4","5more"]
persons = ["2","4","more"]
lug_boot = ["small","med","big"]
safety = ["low","med","high"]
'''


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
classifications = {"unacc","acc","good","vgood"}
buying = {"vghigh":0,"high":0,"med":0,"low":0}
maint = {"vghigh":0,"high":0,"med":0,"low":0}
doors = {"2":0,"3":0,"4":0,"5more":0}
persons = {"2":0,"4":0,"more":0}
lug_boot = {"small":0,"med":0,"big":0}
safety = {"low":0,"med":0,"high":0}
attributes = [classifications, buying, maint, doors, persons, lug_boot, safety]

table = {x:{'count':0} for x in classifications} 
for car_class, v in table.iteritems():
	for attr, val in buying.iteritems():
		table[car_class][attr] = 0

print "table:\n",table

# inputfile = open("small.data")
input = ["vhigh,low,3,more,big,low,unacc","low,vhigh,5more,4,big,high,acc"]
input_lines = []					# processed input
# print input[0].split(",")
for i in input:
	t = i.split(",")
	input_lines.extend([t])
print "input_lines:",input_lines
for i in input_lines:
	print i

'''
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
'''

