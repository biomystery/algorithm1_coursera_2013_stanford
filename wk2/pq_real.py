def findMiddle(array, left, right):
    '''Find a middle index from array[left] to array[right]'''
    middle = (right - left) / 2 + left
    min_value = min(array[left],array[right],array[middle])
    max_value = max(array[left],array[right],array[middle])    
    if (array[left] > min_value) & (array[left] < max_value) :
        return left
    elif (array[right] > min_value) & (array[right] < max_value) :
        return right
    else:
        return middle

def choosePivot(array,left,right,options):
    '''Choose pivot, return the pivot position'''
    if options.lower() == 'a':
        p_ind = left
    elif options.lower() == 'b':
        p_ind = right
    elif options.lower() == 'c':
        '''Median of array(left),array(right),array(middle)'''
        p_ind = findMiddle(array,left,right)
    return p_ind

def swap(array, ind_a, ind_b):
    tmp = array[ind_b]
    array[ind_b] = array[ind_a]
    array[ind_a] = tmp


def partition(array,p_ind,left,right):
    '''Partition the array around the pivot, return the loc of the pivot'''
    p_value = array[p_ind]
    swap(array,left,p_ind)
    i = left + 1
    for j in range(i,right+1):
        if array[j] < p_value:
            swap(array,i,j)
            i += 1
    swap(array,left,i-1)
    return i-1


def quickSort(array, left, right, options, cmp_count):
    '''Recursively sort'''
    if right - left <= 0:
        return cmp_count 
    else:
        p_ind = choosePivot(array,left, right, options)
        p_ind = partition(array,p_ind,left,right)
        cmp_count += right - left
        
        # recursively sort 1st part
        cmp_count = quickSort(array,left,p_ind - 1, options, cmp_count)

        # recursively sort 2st part        
        cmp_count = quickSort(array,p_ind + 1,right, options, cmp_count)
        return cmp_count


    
##########
# main code
##########

# read the data file        
array = [];

with open('QuickSort.txt') as f:
    array = [[int(x) for x in line.split()] for i, line in enumerate(f)]

array_old = array[:]
cmp_count = 0
cmp_counts = {}
result_arr = {}

for i, option in enumerate({'a','b','c'}):
    '''for different cases'''
    cmp_count = quickSort(array,0,len(array)-1,option, cmp_count)    
    result_arr.update({option: array})
    cmp_counts.update({option:cmp_count})
    cmp_count = 0
    array = array_old[:]

        




