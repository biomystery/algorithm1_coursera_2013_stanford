'''
Random Contraction Program: for the homework 
Author: Frank Cheng 
Date: Tue Aug  6 17:01:10 PDT 2013
Use an object in python. 
'''

#------------------------------------------------------------
# Sub-routines. 
#------------------------------------------------------------

# import the library 
import random 
from copy import deepcopy

# subroutine - edge merge
def contractEdge(graph,selected_edge):
    '''Given a graph and a selected edge
    return: the merged graph (a new graph)
    '''
    s_edges.append(selected_edge)
    index_one = [];
    index_two = [];
    # find nodes of the selected edge
    for index, each_node_edge in enumerate(graph):
        # find the first node of the selected edge
        if each_node_edge[0] == selected_edge[0]:
            index_one = [index, each_node_edge.index(selected_edge[1])]
        elif each_node_edge[0] == selected_edge[1]:
            index_two = [index, each_node_edge.index(selected_edge[0])]

    # delete the edge (due to symmetry of the graph matrix and need to combine the two nodes, we need delete both)
    try:
        del graph[index_one[0]][index_one[1]] # edge one
        del graph[index_two[0]][index_two[1]] # edge two
    except IndexError:
        print selected_edge,index_two

    # combine the selected edge
    graph[index_one[0]] += graph[index_two[0]][1:]

    # mutant the second node of the selected edge: should be after 
    for index, each_node_edge in enumerate(graph):            
        for i,x in enumerate(each_node_edge):
            if x == selected_edge[1]:
                graph[index][i]=selected_edge[0]

    # remove the self loop: should be after mutant before del
    counter = 1
    for index, node in enumerate(graph[index_one[0]][1:]):
        if node == selected_edge[0]:
            # print node,graph[index_one[0]][index+counter]
            del graph[index_one[0]][index+counter]
            counter -= 1

    # remove the second node of the selected edge
    s_remain.append(graph[index_one[0]][0])
    s_del.append(graph[index_two[0]][0])
    graph.pop(index_two[0])  


    # return
    return graph    

# rand select 
def randSelect(graph):
    '''Given a graph, random select a edge'''

    # random select nodes
    node1 = random.randint(0,len(graph)-1)
    node2 = random.randint(0,len(graph[node1])-2) + 1
    s_nodes.append([node1,node2])
    
    # return the selected edge, the actual value of the edges 
    #    print [graph[node1][0],graph[node1][node2]] 
    return [graph[node1][0],graph[node1][node2]] 


# subroutine - random contractoin
def randContraction(graph):
    '''
    Input: graph( matrix, row: the edges) and a random seed. 
    Output: the cut dictionary (including the vertices, and number of cut
    '''
    # contract this edge and gen
    while len(graph)>2:
        selected_edge = randSelect(graph)
        contractEdge(graph,selected_edge)

    return len(graph[0][1:])

#------------------------------------------------------------
# Main code
#------------------------------------------------------------
from math import log

# read the file 
graph = [];

with open('kargerMinCut.txt') as f:
    graph = [[int(x) for x in line.split()] for i, line in enumerate(f)]

graph_old = deepcopy(graph)

#print graph_old[0]

n = len(graph)     
all_cut_no =[]#200# range(int(n**2*log(n)))
#for i in range(int(n**2*log(n))):
for i in range(400*2):               
    print i
    s_remain = []
    s_del = []
    s_edges =[]
    s_nodes =[]

    all_cut_no.append(randContraction(graph))
    graph = deepcopy(graph_old)
    
#------------------------------------------------------------
# test module
#------------------------------------------------------------
#test_graph = [[1,2,4],[2,1,3,4],[3,2,4],[4,1,2,3]]
#test_graph_back = test_graph[:]
#randContraction(test_graph)

#print test_graph


print min(all_cut_no)
