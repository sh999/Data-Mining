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

def make_table():

	table = {"unacc":{
					"count":0,
					"buying":{"vhigh":0,"high":0,"med":0,"low":0},
					"maint":{"vhigh":0,"high":0,"med":0,"low":0},
					"doors":{"2":0,"3":0,"4":0,"5more":0},
					"persons":{"2":0,"4":0,"more":0},
					"lug_boot":{"small":0,"med":0,"big":0},
					"safety":{"low":0,"med":0,"high":0}
					},
			"acc":{
					"count":0,
					"buying":{"vhigh":0,"high":0,"med":0,"low":0},
					"maint":{"vhigh":0,"high":0,"med":0,"low":0},
					"doors":{"2":0,"3":0,"4":0,"5more":0},
					"persons":{"2":0,"4":0,"more":0},
					"lug_boot":{"small":0,"med":0,"big":0},
					"safety":{"low":0,"med":0,"high":0}
					},
			"good":{
					"count":0,
					"buying":{"vhigh":0,"high":0,"med":0,"low":0},
					"maint":{"vhigh":0,"high":0,"med":0,"low":0},
					"doors":{"2":0,"3":0,"4":0,"5more":0},
					"persons":{"2":0,"4":0,"more":0},
					"lug_boot":{"small":0,"med":0,"big":0},
					"safety":{"low":0,"med":0,"high":0}
					},
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
	return table


def parse_line(input):
	# inputfile = open("small.data")
	# input = ["vhigh,low,3,more,big,low,unacc","low,vhigh,5more,4,big,high,acc"]
	input_lines = []					# processed input
	# print input[0].split(",")
	for i in input:
		t = i.split(",")
		input_lines.extend([t])
	print "input_lines:",input_lines
	for i in input_lines:
		print i

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

	return input_lines

def update_table(table, input):
	classification = input[-1]
	print "classification:",classification
	print table[classification]["buying"]["vhigh"]
	
	for i, j in enumerate(input):
		print "checking: ",i,"and",j
		if i == 0:
			table[classification]["buying"][j] += 1
		elif i == 1:
			table[classification]["maint"][j] += 1
		elif i == 2:
			table[classification]["doors"][j] += 1
		elif i == 3:
			table[classification]["persons"][j] += 1
		elif i == 4:
			table[classification]["lug_boot"][j] += 1
		elif i == 5:
			table[classification]["safety"][j] += 1
	return table

def main():
	table = make_table()
	print "init table:",table
	# input = ["vhigh,low,3,more,big,low,unacc","low,vhigh,5more,4,big,high,acc"]
	# parsed = parse_line(input)
	input2 = ["vhigh","low","3","more","big","low","unacc"]
	table = update_table(table, input2)
	print "updated table:",table
main()
