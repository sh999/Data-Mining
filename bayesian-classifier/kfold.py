'''
K-fold cross validation
'''
import random
from bayes import *
def training_indices(k):
	'''
	Calculate k bins, each bin has indices for training set
	original_set[k] is tested against the training sets
	k:4
	elements:0,1,2,3

	testing_set_index:training_set_index
	0:1,2,3
	1:0,2,3
	2:0,1,3
	3:0,1,2

	indices are used to run bayesian classification
	'''
	x = [i for i in range(0,k)]
	indices = []
	for i in range(0,k):
		indices.append([])	# empty partitions
	for i in range(0,len(x)):
		to_insert = [b for b in x if b != x[i]]
		indices[i].extend(to_insert)
	print "indices:",indices
	return indices

def randomize_list(k, orig_list):
	list_size = len(orig_list)
	print "orig list:",orig_list
	random_list = []
	for i in range(0,k):
		random_list.append([])	# empty partitions

	while len(orig_list) > 0:
		for i in range(0,k):
			x = random.choice(orig_list)
			orig_list.remove(x)
			random_list[i].extend([x])

	print "randomized, partitioned:",random_list
	return random_list

def run_classifier():
	pass

list_size = 12
k = 4
# orig_list = [i for i in range(0,list_size)]
input_lines = parse_lines("small.data")
print input_lines
# randomize_list(k, orig_list)
# training_indices(k)