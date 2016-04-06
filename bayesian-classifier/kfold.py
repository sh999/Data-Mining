'''
K-fold cross validation
'''
import random
from bayes import *
import copy
def training_indices(k):
	'''
	Calculate k bins, each bin has indices for training set
	original_set[k] is tested against the training sets
	e.g. k:4
	element indices:0,1,2,3

	testing_set_index:training_set_index
	0:1,2,3
	1:0,2,3
	2:0,1,3
	3:0,1,2

	indices are used to run bayesian classification
		classify()
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

def classify_folds(input_set, indices):
	'''
	Run Bayesian classifier on input_set multiple times based on 
	 given indices. Indices format is described in training_indices()
	'''
	print "\n\ninput_set:",input_set
	'''
	for test_index, train_index in enumerate(indices):
		print "test index:", test_index
		print "train_index", train_index
		testing_set = [input_set[test_index]]
		print "testing_set:",testing_set
		# training_set = input_set[train_index]
		# print "training_set:",training_set

		# classify([test_index], train_index)
	'''
	orig = copy.deepcopy(input_set)
	print "orig:",orig
	print "indices:", indices
	testing_set = input_set[0]
	print "testing_set:",testing_set
	training_set = input_set[1]
	print "training_set:",training_set
	accuracy = classify(training_set, testing_set)
	print "accuracy:",accuracy
	
	input_set = copy.deepcopy(orig)
	print "\n\ninput_set:",input_set
	print "indices:", indices
	testing_set = input_set[0]
	print "testing_set:",testing_set
	training_set = input_set[2]
	print "training_set:",training_set
	accuracy = classify(training_set, testing_set)
	print "accuracy:",accuracy


def main():
	list_size = 100
	k = 4
	# orig_list = [i for i in range(0,list_size)]
	input_set = parse_lines("small.data")
	print input_set
	input_set = randomize_list(k, input_set)
	indices = training_indices(k)
	classify_folds(input_set, indices)

if __name__ == '__main__':
	main()