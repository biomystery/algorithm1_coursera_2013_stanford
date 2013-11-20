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


def quickSort(array, left, right, options):
    '''Recursively sort'''
    if right - left <= 0:
        #lenth  = 1
        return 
    else:
        p_ind = choosePivot(array,left, right, options)
        p_ind = partition(array,p_ind,left,right)
        #print str(p_ind)
        
        # recursively sort 1st part
        quickSort(array,left,p_ind - 1, options)

        # recursively sort 2st part        
        quickSort(array,p_ind + 1,right, options)
        #        return array


    
##########
# main code
##########

# read the data file        
array = [];

with open('QuickSort.txt') as f:
    array = [[int(x) for x in line.split()] for i, line in enumerate(f)]
    #array = array[:20]
array_old = array[:]

# for different cases
result = {};
for i, option in enumerate({'a','b','c'}):
    #    print array[:10]
    quickSort(array,0,len(array)-1,option)    
    result.update({option: array})
    #    print array[:10]
    array = array_old[:]

    

# output the result 
#with open('result.txt','w') as f:
#    f.write(str(count))

        




