global_t = 0; 
global_s = [];

# subroutine: DFS
def DFSloop(graph):
    global global_s
      
    def DFS(graph,node_s,explore_flag,reverse_flag):
        global global_t
        global global_s # leader

        explore_flag[node_s] = True 
        if reverse_flag:
            for edge in graph:
                if edge[1] == node_s:
                    if not explore_flag[edge[0]]:
                        DFS(graph,edge[0],explore_flag,reverse_flag)
            global_t += 1
            finish_time[node_s] = global_t
        else:
            leader[node_s] = global_s
            #print leader
            for edge in graph:
                if edge[0] == node_s:
                    if not explore_flag[edge[1]]:
                        DFS(graph,edge[1],explore_flag,reverse_flag)

    # time: for python, index start from 0
    node_no = max(sum(graph,[]))
    print node_no
    finish_time = [0]*(node_no+1)
    explore_flag = [False]*(node_no + 1)
    leader = [0]*(node_no+1)

    # 1. 1st DFS on reverse to get finish_time    
    for node in range(node_no,0,-1):
        print node
        if not explore_flag[node]:
            DFS(graph,node,explore_flag,True)
    print 'finished first loop'
    # 2. 2nd DFS on new graph, whose node is finish_time(old_node)
    explore_flag = [False]*(node_no+1)
    new_graph = [[finish_time[edge[0]],finish_time[edge[1]]] for edge in graph]

    for new_node in range(node_no,0,-1):
        print new_node
        if not explore_flag[new_node]:
            global_s = new_node
            DFS(new_graph,new_node,explore_flag,False) # not rev
            
    print 'finished second loop'            
    # return the leader array
    return leader[1:] 
                    


# test case 
graph=[[1,4],[2,8],[3,6],[4,7],[5,2],[6,9],[7,1],[8,5],[8,6],[9,3],[9,7]]
leader = DFSloop(graph)
print leader[1:]

def listCont(lst,top_no):
    count = []
    for i in range(top_no):
        member = max(set(lst),key = lst.count)
        count.append(lst.count(member))
        lst = filter(lambda a: a != member, lst)
    return count

# read the data
print 'loading data'
X = [[int(i) for i in line.split()] for line in open('SCC.txt')]

print 'finshed loading'
node_no = 875714
leader = DFSloop(X)

# list count 
print listCont(leader,3)
        
    
