'''Test the edgeMerge'''
test_graph = [[1,2,4],[2,1,3,4],[3,2,4],[4,1,2,3]]

# contract 1: [1,4]
selected_edge_one = [1,4]
edgeMerge(test_graph,selected_edge_one)
print test_graph
selected_edge_one = [2,1]
edgeMerge(test_graph,selected_edge_one)
print test_graph
'''Test the random selection'''
