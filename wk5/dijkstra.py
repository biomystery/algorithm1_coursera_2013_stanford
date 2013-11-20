def shortestDist(graph,start):
    X = set([start])
    B = {start:[]} # visiting seqs. 
    v_no = len(graph)
    V = set([graph[i][0][0] for i in range(v_no)])
    A = {i:1000000 for i in range(start,start+v_no) }#dist for each node
    A[start]=0 
    D = {} # dict for final dists
    timer = 0
    while X!=V:
        # among all edges(v,w) with v in X, w not in X
        for v in X:
            # all head not in X with dist
            all_lw = [a[v-1][i] for i in range(1,len(a[v-1])) if a[v-1][i][0] not in X]
            # find min dist add into dist_dict
            if len(all_lw)>0:
                D[v] = min([i[::-1] for i in all_lw]) # [min_dist,node w]
                D[v][0] = D[v][0] + A[v] #update distance A[v]+ Lvw
            else:
                D ={}
        # find minimal, relax 
        if len(all_lw)>0:        
            v_s = min(D,key=D.get) # key for minimal dist
            w_s = D[v_s][1]
            X.add(w_s) # add w_s to X
            A[w_s] = D[v_s][0] # update dist
            print [w_s],[v_s],B[v_s]
            B[w_s] = B[v_s]
            B[w_s].append(w_s)
    return A

# read data
a=[[[int(j) for j in i.split(',')] for i in line.split()] for line in open('test.txt')] # 3d list,dijkstraData
#a = [[[1],[2,1],[3,4]],[[2],[3,2],[4,6]],[[3],[4,3]],[[4],[4,0]]]
A = {}
A = shortestDist(a,0)
print A
