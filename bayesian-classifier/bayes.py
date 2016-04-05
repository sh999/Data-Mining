'''
Bayesian classifier for car data
data source:
            http://archive.ics.uci.edu/ml/datasets/Car+Evaluation
The data contain classification of cars into unacceptable to very good
Car attributes include buying price, maintenance price, # doors,
 capacity, luggage size, and safety estimate
I am using 1000 of the car entries as training set; the remaining 728
 are the training set

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

Representation as dict:
{"unacc":{count:10,buying:{vhigh:3,high:4...},maint:{vhigh...},...,"acc":{count:32,buying:{......}}}

'''

def make_table():
	'''
	Bayesian classifier table with absolute counts
	'''
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
					"buying":{"vhigh":0,"high":0,"med":0,"low":0},
					"maint":{"vhigh":0,"high":0,"med":0,"low":0},
					"doors":{"2":0,"3":0,"4":0,"5more":0},
					"persons":{"2":0,"4":0,"more":0},
					"lug_boot":{"small":0,"med":0,"big":0},
					"safety":{"low":0,"med":0,"high":0}
					}
			}
	return table

def parse_lines(input):
	'''
	Convert txt file to a list of attribute strings
	 for each data entry
	'''
	output = []					# processed input
	for i in input:
		# print "i:",i
		temp = i.split(",")
		# print "temp",temp
		output.extend([temp])
	return output

def update_table(table, input):
	'''
	For each data entry, update all table values
	'''
	classification = input[-1].rstrip()
	table[classification]['count'] += 1
	# print "classification:",classification	
	for i, j in enumerate(input):
		# print "checking: ",i,"and",j
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

def display_table(table):
	for classification in table:
		print "Class = ",classification 
		for attribute in table[classification]:
			print "\t",attribute,"=", table[classification][attribute]
def freq_table(table):
	'''
	Convert Bayesian classifier table (raw integer counts) 
	 into frequency values (value/total entries)
	'''
	total_entries = 0
	for i in table:
		total_entries += table[i]['count']
	
	for classification in table:
		for attribute in table[classification]:
			if attribute != 'count':
				for value in table[classification][attribute]:
					table[classification][attribute][value] /= float(table[classification]['count'])
	for classification in table:
		table[classification]['count'] /= float(total_entries)
	return table


def single_odds(f_table, input):
	'''
	Input: All conditions with one classification
	Returns: Odds of this condition to have this classification
	'''
	classification = input[-1]
	a = ["buying","maint","doors","persons","lug_boot","safety"]
	odds = 1
	for i in range(0,len(input)-1):
		this_condit = f_table[classification][a[i]][input[i]]
		odds = odds * this_condit
		# print input[i], this_condit, odds
	# print "this condit:", odds
	return odds

def odds(f_table, input):
	input = input[0]
	classifications = ["unacc","acc","good","vgood"]
	class_odds = {"unacc":0,"acc":0,"good":0,"vgood":0}
	for c in classifications:
		input[-1] = c
		print "input:",input
		odds = single_odds(f_table, input)
		print "class",c,"odds:",odds
		class_odds[c] = odds
	print class_odds
	# x = {1:2, 3:6, 5:4}
	print "Bayes classification:",max(class_odds, key=lambda i: class_odds[i])

def main():
	table = make_table()
	# print "init table:",table
	inputfile = open("cartrain2.data")
	inputstrings = inputfile.readlines()
	parsed_input = parse_lines(inputstrings)
	# print parsed_input
	for i in parsed_input:
		table = update_table(table, i)
	# print "updated table:",table
	# display_table(table)
	f_table = freq_table(table)
	# display_table(f_table)

	# test = ["med,vhigh,2,more,big,med,acc\n","med,med,2,4,small,low,unacc\n"]
	test = ["vhigh,med,2,4,big,med,acc","med,med,2,4,small,low,unacc\n"]
	test = parse_lines(test)
	print test
	print "=============================="
	x = odds(f_table, test)


main()