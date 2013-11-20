# subroutine: DFS
import sys,os
'''sys.settrace
sys.setrecursionlimit(20000)
os.system('sudo ulimit -s unlimited; some_executable')'''

#import resource, sys
#resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
#resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))
#sys.setrecursionlimit(10**6)

global_t = 0; 
global_s = 0;#leader

def DFSloop(hash_table,hash_table_rev):
    '''If node is only a head
    no key in the dict, key only is the tail.
    
    '''
    global global_s
    # time: for python, index start from 0
    node_no = max(max(hash_table),max(hash_table_rev))
    finish_time = [0]*(node_no+1)
    explore_flag = [False]*(node_no + 1)
    leader = [0]*(node_no+1)
    def DFS(graph_dict,node_s,explore_flag,rev_flag):
        global global_t
        global global_s # leader
        explore_flag[node_s] = True         
        if not rev_flag: #2nd round
            leader[node_s] = global_s
        if node_s in graph_dict: # only key 
            for node_head in graph_dict[node_s]:
                if not explore_flag[node_head]:
                    DFS(graph_dict,node_head,explore_flag,rev_flag)
        if rev_flag:
            global_t += 1
            finish_time[node_s] = global_t
    #1. 1st DFS on reverse to get finish_time'''
    for node in range(node_no,0,-1):
        #        if node == 874931:
        #    import pdb
        #    pdb.set_trace()
        if not explore_flag[node]:
            DFS(hash_table_rev,node,explore_flag,True)
    # release memory
    #del hash_table_rev
    print finish_time[1:10]
    # 2. 2nd DFS on new graph, whose node is finish_time(old_node)
    explore_flag = [False]*(node_no+1)
    # get new hash_table
    hash_table_new = {}
    for key,value in hash_table.items():
        hash_table_new[finish_time[key]] = [finish_time[i] for i in value]
    #del hash_table
    for node in range(node_no,0,-1):#start from new largest node
        if node%10000 ==0:
            print node
        if not explore_flag[node]:
            global_s = node
            DFS(hash_table_new,node,explore_flag,False) # not rev
    #print leader
    # return the leader array
    return leader[1:] 
                    
def listCount(lst,top_no):
    '''Count the top_no frequencies in the list'''
    count = []
    for i in range(top_no):
        member = max(set(lst),key = lst.count)
        count.append(lst.count(member))
        lst = filter(lambda a: a != member, lst)
    return count



def hashFunc(lst,hash_table,rev_flag):
    '''Push a list into hash_table, represent adjancy graph'''
    idx_first = int(rev_flag)
    idx_second = int(not rev_flag)
    
    if hash_table.has_key(lst[idx_first]):
        hash_table[lst[idx_first]].append(lst[idx_second])
    else:
        hash_table[lst[idx_first]] = [lst[idx_second]]

if __name__ == '__main__':

    #read the data
    hash_table = {}
    hash_table_rev = {}
    #test case 
    print "Now loading the data..."
    for line in open('test3.txt'):
        line_lst = [int(i) for i in line.split()]
        hashFunc(line_lst,hash_table,False)
        hashFunc(line_lst,hash_table_rev,True)
        print "Loading finished"
        leader = DFSloop(hash_table,hash_table_rev)
    print listCount(leader,3)
        
    
