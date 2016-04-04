'''
Bayesian classifier for car data
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

{"unacc":{count:10,buying:{vhigh:3,high:4...},maint:{vhigh...},...,"acc":{count:32,buying:{......}}}

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
buying = ["vghigh","high","med","low"]
maint = ["vghigh","high","med","low"]
doors = ["2","3","4","5more"]
persons = ["2","4","more"]
lug_boot = ["small","med","big"]
safety = ["low","med","high"]
'''
classifications = {"unacc","acc","good","vgood"}

'''
buying = {"label":"buying","vghigh":0,"high":0,"med":0,"low":0}
maint = {"label":"maint","vghigh":0,"high":0,"med":0,"low":0}
doors = {"label":"doors","2":0,"3":0,"4":0,"5more":0}
persons = {"label":"persons","2":0,"4":0,"more":0}
lug_boot = {"label":"lug_boot","small":0,"med":0,"big":0}
safety = {"label":"safety","low":0,"med":0,"high":0}
'''

table = {"unacc":{
				"count":0,
				"buying":{"vghigh":0,"high":0,"med":0,"low":0},
				"maint":{"vghigh":0,"high":0,"med":0,"low":0},
				"doors":{"2":0,"3":0,"4":0,"5more":0},
				"persons":{"2":0,"4":0,"more":0},
				"lug_boot":{"small":0,"med":0,"big":0},
				"safety":{"low":0,"med":0,"high":0}
				}
		,
		"acc":{
				"count":0,
				"buying":{"vghigh":0,"high":0,"med":0,"low":0},
				"maint":{"vghigh":0,"high":0,"med":0,"low":0},
				"doors":{"2":0,"3":0,"4":0,"5more":0},
				"persons":{"2":0,"4":0,"more":0},
				"lug_boot":{"small":0,"med":0,"big":0},
				"safety":{"low":0,"med":0,"high":0}
				}
		,
		"good":{
				"count":0,
				"buying":{"vghigh":0,"high":0,"med":0,"low":0},
				"maint":{"vghigh":0,"high":0,"med":0,"low":0},
				"doors":{"2":0,"3":0,"4":0,"5more":0},
				"persons":{"2":0,"4":0,"more":0},
				"lug_boot":{"small":0,"med":0,"big":0},
				"safety":{"low":0,"med":0,"high":0}
				}
		,
		"vgood":{
				"count":0,
				"buying":{"vghigh":0,"high":0,"med":0,"low":0},
				"maint":{"vghigh":0,"high":0,"med":0,"low":0},
				"doors":{"2":0,"3":0,"4":0,"5more":0},
				"persons":{"2":0,"4":0,"more":0},
				"lug_boot":{"small":0,"med":0,"big":0},
				"safety":{"low":0,"med":0,"high":0}
				}
		}
print table
'''
buying_vals = {"vghigh":0,"high":0,"med":0,"low":0}
maint_vals = {"vghigh":0,"high":0,"med":0,"low":0}
doors_vals = {"2":0,"3":0,"4":0,"5more":0}
persons_vals = {"2":0,"4":0,"more":0}
lug_boot_vals = {"small":0,"med":0,"big":0}
safety_vals = {"low":0,"med":0,"high":0}

# attributes = {"buying":0, "maint":0,"doors":0,"persons":0,"lug_boot":0,"safety":0}
attributes = ["buying", "maint", "doors", "persons", "lug_boot", "safety"]
# a = {i:0 for i in attributes}
# print "a:",a
buying = {"buying":{k:v for k, v in buying_vals.iteritems()}} 
maint = {"maint":{k:v for k, v in maint_vals.iteritems()}} 
doors = {"doors":{k:v for k, v in doors_vals.iteritems()}} 
persons = {"persons":{k:v for k, v in persons_vals.iteritems()}} 
lug_boot = {"lug_boot":{k:v for k, v in lug_boot_vals.iteritems()}} 
safety = {"safety":{k:v for k, v in safety_vals.iteritems()}} 

print "buying:",buying
# table = {x:{'count':0} for x in classifications} 
# for car_class, v in table.iteritems():
	# print car_class
table = {"count":0, {""}}
'''
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

