
def mergeSort(arr,inv_count = 0):
    '''return the sorted array and the inversion no.'''
    if len(arr)<=1:
        return (arr,inv_count)
    mid = int(len(arr)/2)
    left, inv_count = mergeSort(arr[:mid],inv_count)
    right, inv_count = mergeSort(arr[mid:],inv_count)
    arr_output,inv_count = merge(left,right,inv_count)
    return (arr_output,inv_count)


def merge(left,right,inv_count):
    '''Merge two sortted array'''
    arr_output = []
    i,j=0,0;
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            arr_output.append(right[j])
            inv_count = inv_count + len(left) - i#expose the inversions in the left
            j = j+1
        else:
            arr_output.append(left[i])
            i = i+1
    arr_output += left[i:]
    arr_output += right[j:]
    return (arr_output,inv_count)

            
# read the file & test the file . 
array = [];
with open('integerarray.txt') as f:
    array = [[int(x) for x in line.split()] for i, line in enumerate(f)]
'''    for i, line in enumerate(f):
        tmp = [int(x) for x in line.split()]
        array.append(tmp)
        if i > 4:
            break'''

out, count = mergeSort(array)                   

# write the result 
with open('result2.txt','w') as f:
    f.write(str(count))

        




