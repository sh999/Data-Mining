'''
4
0,1,2,3

0:1,2,3
1:0,2,3
2:0,1,3
3:0,1,2
'''
k = 4

x = [i for i in range(0,k)]
y = []
for i in range(0,k):
	y.append([])	# empty partitions
for i in range(0,len(x)):
	to_insert = [b for b in x if b != x[i]]
	y[i].extend(to_insert)
print y
