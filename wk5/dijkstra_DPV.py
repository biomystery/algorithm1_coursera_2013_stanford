# note: The node in the graph should start as 1
def shortestDist(graph,start):
    X = set() # known region 
    B = {start:[]} # visiting seqs. 
    v_no = len(graph)
    V = set([graph[i][0][0] for i in range(v_no)])
    A = {i:1000000 for i in range(v_no+1) }#dist for each node
    A[start]=0 
    D = {} # dict for final dists, l(v,z)

    while X!=V:
        
        #pp.124 book DPV,find min A[v] for all v not in X as v
        tmpdict = dict([(key,value) for key,value in A.items() if key not in X])
        v = min(tmpdict,key = tmpdict.get)

        # add v to X
        X.add(v)
 
        # all edges (v,w) update A[w]
        for w,l in a[v-1][1:]:
            if A[w]>A[v]+l:
                A[w] = A[v]+l 
        
    return A

# read data
a=[[[int(j) for j in i.split(',')] for i in line.split()] for line in open('dijkstraData.txt')] # 3d list,dijkstraData
#a = [[[1],[2,1],[3,4]],[[2],[3,2],[4,6]],[[3],[4,3]],[[4],[4,0]]]
A = {}
A = shortestDist(a,1)
print A[7],A[37],A[59],A[82],A[99],A[115],A[133],A[165],A[188],A[197]
