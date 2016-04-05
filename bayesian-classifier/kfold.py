'''
K-fold cross validation
'''
import random

list_size = 21
k = 3
orig_list = [i for i in range(0,list_size)]
print "orig list:",orig_list

# make empty list with k partitions
partition_size = list_size/4	# num of elements per sublist
random_list = []
for i in range(0,k):
	random_list.append([])	# empty partitions

while len(orig_list) > 0:
	for i in range(0,k):
		x = random.choice(orig_list)
		orig_list.remove(x)
		random_list[i].extend([x])

print "randomized, partitioned:",random_list
