# test2Sum: check whether a target(t) in a hashTable.
    
def test2Sum(t,hashTable):
    for key in hashTable:
        if hashTable.has_key(t-key):
            return True # as global
    return False
    
# read the file 
array = [];

with open('algo1-programming_prob-2sum.txt') as f:
    array = [int(line) for i, line in enumerate(f)]

    #no_buckets = # number of buckets.


'''
construct the hash table
'''
# 1. Hash function: quick and dirty hash func.
#    Turn the array into a hash table, with key = number. ind = value?
    
hashTable = {}

j = 0
for i in array: # value as key 
    hashTable[i] = j
    j =  j+ 1

count = 0;
for t in xrange(-10000,10001):
    if t%100 == 0:
        print t
    if test2Sum(t,hashTable):
        count = count + 1

print count 



    

    
