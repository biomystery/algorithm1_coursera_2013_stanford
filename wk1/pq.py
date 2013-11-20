
# read the file 
with open('integerarray.txt') as f:
    array = [[int(x) for x in line.split()] for line in f]

# two loops 
count = 0 
n = len(array)
for i in range(n-1):
    for j in range(i,n):
        if array[i] > array[j]:
            count += 1
# write the result 
with open('result1.txt','w') as f:
    f.write(str(count))
        




