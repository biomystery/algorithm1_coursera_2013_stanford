'''Ref: http://stackoverflow.com/questions/10657503/find-running-median-from-a-stream-of-integers'''
# libraries. 
import math

# maxHeap class
# ref: http://www.shaunlippy.org/blog/?p=105
class maxHeap:
    def __init__(self, items=None):
        if items == None:
            self.__items = deque() # init is an empty deque (double ended queue)
        else:
            self.__items = self.__build_heap(items)
            
    def __build_heap(self, items):
        count = len(items)
        for i in range(int(math.floor(count/2)) - 1, -1, -1): # start from the last parent
            self.__heapify(items, i, count)
        return items
    def __heapify(self, items, idx, max_element):
        left, right = 2*idx + 1, 2*idx + 2 
        
        if left < max_element and items[left] > items[idx]:
            largest = left
        else:
            largest = idx
        if right < max_element and items[right] > items[largest]:
            largest = right
        if not largest == idx: # swap and terminate when largest == idx
            items[idx], items[largest] = items[largest], items[idx]
            self.__heapify(items, largest, max_element)
    def add(self, item):
        self.__items.append(item) # need to know here.
        self.__build_heap(self.__items)
    def remove(self):
        item = self.__items.popleft()
        self.__build_heap(self.__items)
        return item
    def root(self):
        return self.__items[0]
    def size(self):
        return len(self.__items)
    def is_empty(self):
        return len(self.__items) == 0

# minHeap class
class minHeap:
    def __init__(self, items=None):
        if items == None:
            self.__items = deque() # init is an empty deque (double ended queue)
        else:
            self.__items = self.__build_heap(items)
            
    def __build_heap(self, items):
        count = len(items)
        for i in range(int(math.floor(count/2)) - 1, -1, -1): # start from the last parent
            self.__heapify(items, i, count)
        return items
    def __heapify(self, items, idx, max_element):
        left, right = 2*idx + 1, 2*idx + 2 
        
        if left < max_element and items[left] < items[idx]:
            smallest = left
        else:
            smallest = idx
        if right < max_element and items[right] < items[smallest]:
            smallest = right
        if not smallest == idx: # swap and terminate when smallest == idx
            items[idx], items[smallest] = items[smallest], items[idx]
            self.__heapify(items, smallest, max_element)
    def add(self, item):
        self.__items.append(item) # need to know here.
        self.__build_heap(self.__items)
    def remove(self):
        item = self.__items.popleft()
        self.__build_heap(self.__items)
        return item
    def root(self):
        return self.__items[0]
    def size(self):
        return len(self.__items)
    def is_empty(self):
        return len(self.__items) == 0

#    
def medianSteam(array,currentInd):
    '''Input: array and current index, output current median'''

    # remove root and rebuild the heap
    def removeRoot(heap,maxFlag):
        if maxFlag == 1:
            pass
        elif maxFlag == 0:
            pass

    # add a value into a heap
    def addHeap(heap,value,maxFlag):
        pass
    
    # 1. maintain maxHeap: Root is min
    # 2. maintain minHeap: Root is max
    # 3. maintain equal length
    def maintainLen(minHeap,maxHeap):
        if len(minHeap) - len(maxHeap) < -2: #or while????
            # minHeap less than maxheap
            a = removeRoot(maxHeap,1) #remove root from maxHeap
            addHeap(minHeap,a,0) # add it to minHeap
        elif len(minHeap) - len(maxHeap) > 2:
            a = removeRoot(minHeap,0) #remove root from maxHeap
            addHeap(maxHeap,a,1) # add it to minHeap

    # 4. calMedian(minHeap,maxHeap)
    def calMedian(minHeap,maxHeap):
        if len(minHeap) == len(maxHeap):
            return (minHeap[0] + maxHeap[0])/2.0
        elif len(minHeap) > len(maxHeap):
            return minHeap[0]
        else:
            return maxHeap[0]


#if __name__== '__main__':
from collections import deque
# read the data 
array = [];
with open('Median.txt') as f:
    array = [int(line) for i, line in enumerate(f)]
        
# initial, first two
sum_median = 0    
min_heap = minHeap()
max_heap = maxHeap()
max_heap.add(min(array[0:2]))
min_heap.add(max(array[0:2]))            
sum_median += array[0] + min(array[0:2])

# continue
for i in range(2,len(array)):
    if i%500 ==0:
        print i
    # add item
    if array[i] < max_heap.root():
        max_heap.add(array[i])
    else:
        min_heap.add(array[i])
    # balance heaps
    if max_heap.size() - min_heap.size() >1:
        min_heap.add(max_heap.remove())
    elif max_heap.size() - min_heap.size() <-1:
        max_heap.add(min_heap.remove())
    # update median
    if max_heap.size() >= min_heap.size():
        sum_median += max_heap.root()
    else:
        sum_median += min_heap.root()

# return the sum mod 10000
print sum_median%10000
    

