# subroutine: DFS

def DFSloop(hash_table,hash_table_rev):
    def DFSFirst(graph_dict,node_s,explored,mapping):#set explored, mapping the orders
        ''' First round DFS: get the mapping list (orders)
        https://class.coursera.org/algo-004/forum/thread?thread_id=1159
        Thanks to Alexander Butrym'''        
        stack = [node_s]
        while len(stack)>0: #not empty, tha
            node_tail = stack[-1]
            if node_tail not in explored:
                explored.add(node_tail)
                for node_head in graph_dict.get(node_tail,[]):
                    if node_head not in explored:
                        stack.append(node_head)
            else:
                mapping.append(stack.pop()) # the running time order. 

    def DFSSecond(graph_dict,node_s,explored,leaders):#set explored, leaders:leader-> [members with same leader]
        ''' Second round DFS: get the leaders list (sccs)'''
        stack = [node_s]
        leaders[node_s]= set([])
        while len(stack)>0: #not empty, tha
            node_tail = stack[-1]
            if node_tail not in explored:
                explored.add(node_tail)
                for node_head in graph_dict.get(node_tail,[]):
                    if node_head not in explored:
                        stack.append(node_head)
            else:
                leaders[node_s].add(stack.pop()) # the running time order. 

    # Driver function: 
    explored = set([]) # empty set
    mapping = []# empty list 
    leaders = {} # empty dictionary
    print "Start the first DFS loop"
    for key in sorted(hash_table_rev.keys(),reverse=True):
        if key%1000 ==0:
            print key
        if key not in explored:
            DFSFirst(hash_table_rev,key,explored,mapping)
            #print mapping
    print "Start the second DFS loop"
    explored = set([]) # empty set
    for key in reversed(mapping):1
        if key%1000 ==0:
            print key
        if key not in explored:
            DFSSecond(hash_table,key,explored,leaders)
    return leaders    


def hashFunc(lst,hash_table,rev_flag):
    '''Push a list into hash_table, represent adjancy graph'''
    idx_first = int(rev_flag)#if reverse, = 1
    idx_second = int(not rev_flag) # if not reverse = 0 
    
    if hash_table.has_key(lst[idx_first]):
        hash_table[lst[idx_first]].append(lst[idx_second])
        #print lst[idx_second]
    else:
        hash_table[lst[idx_first]] = [lst[idx_second]]

#read the data   
hash_table = {}
hash_table_rev = {}

# real case
import sys

print "Now loading the data..."
#for line in open(sys.argv[1]):
for line in open(sys.argv[1]):    
    line_lst = [int(i) for i in line.split()]
    hashFunc(line_lst,hash_table,False)
    hashFunc(line_lst,hash_table_rev,True)

print "Loading finished"
    
leaders = DFSloop(hash_table,hash_table_rev)    

print "DFSloop finished"

leaders_sorted_counts = sorted([len(values) for key,values in leaders.items()],reverse =True)
print "Top 5 SCC counts:"
print leaders_sorted_counts[:5]
#print leaders
# 
#leader = DFSloop(hash_table,hash_table_rev)

# list count 
#print listCount(leader,3)
        
'''    
30 seconds for loading 
5 seconds for DFS
Answer: 
Top 5 SCC counts:
[434821, 968, 459, 313, 211]
[1126218, 1669, 991, 750, 654]'''
