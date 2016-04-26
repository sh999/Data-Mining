'''
K-fold cross validation
'''
import random
from bayes import *
import copy
import sys

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
	# print "indices:",indices
	return indices

def randomize_list(k, orig_list):
	list_size = len(orig_list)
	# print "orig list:",orig_list
	random_list = []
	for i in range(0,k):
		random_list.append([])	# empty partitions

	while len(orig_list) > 0:
		for i in range(0,k):
			x = random.choice(orig_list)
			orig_list.remove(x)
			random_list[i].extend([x])

	# print "randomized, partitioned:",random_list
	return random_list

def classify_folds(input_set, indices):
	'''
	Run Bayesian classifier on input_set multiple times based on 
	 given indices. Indices format is described in training_indices()
	'''
	
	# print "\n\ninput_set:",input_set
	all_accuracies = []
	average_accuracies = []
	for test_index, all_train_sets in enumerate(indices):
		# print "test index:", test_index
		test_set = input_set[test_index]
		# print "testing set:", test_set
		# print "training indices:", all_train_sets
		all_accuracies.append([])
		average_accuracies.append([])
		for train_index in all_train_sets:
			train_set = input_set[train_index]
			# print "training set:", train_set
			accuracy = classify(test_set,train_set)
			all_accuracies[test_index].extend([accuracy])
		current_average = sum(all_accuracies[test_index])/3.0
		average_accuracies[test_index].extend([current_average])


	print "Fold % Accuracy:", all_accuracies
	print "Fold average Accuracy:", average_accuracies
	
	
	flat_indices = [x for y in indices for x in y]	# flatten list of lists
	max_ave = max(average_accuracies)
	exclude_index = average_accuracies.index(max_ave)
	print "Highest Ave. Accuracy:", max_ave
	# print "flat:", flat_indices
	best_training = input_set[exclude_index]
	# print "training set best:", best_training
	return exclude_index	# index for the test set that needs to be excluded

	
def get_best_training_set(k, input_file):
	# random.seed(3)
	# list_size = 1000
	k = int(k)
	# orig_list = [i for i in range(0,list_size)]
	input_set = parse_lines(input_file)
	list_size = len(input_set)
	# input_set = parse_lines("cartrain2.data")
	# print input_set
	split_input = randomize_list(k, input_set)
	indices = training_indices(k)
	exclude = classify_folds(split_input, indices)
	print "Model will exclude fold #", exclude

	smaller_training = [split_input[c] for c in range(0,len(split_input)) if c is not exclude]
	# print "smaller training = ", smaller_training
	flat_smaller_training = [a for b in smaller_training for a in b]
	# print "flat flat_smaller_training:", flat_smaller_training
	return flat_smaller_training

def main():
	if(len(sys.argv)==4):
		print "....Running k-fold validation to find best model...."
		k = sys.argv[1]
		training_file = sys.argv[2]
		testing_file = sys.argv[3]
		best_model = get_best_training_set(k, training_file)
		accuracy = classify(best_model,testing_file)
	else:
		print "Please enter the following command:\n"
		print "~/kfold.py [k] [training file] [testing]\n"
		print "Since the above was not done, the following is Bayesian classifi-"
		print "cation on the default car data\n"
		k = 4
		training_file = "cartrain2.data"
		testing_file = "cartest2.data"
		accuracy = classify(training_file, testing_file)
	print "....Running model with test data...."
	print "Accuracy:",accuracy

if __name__ == '__main__':
	main()