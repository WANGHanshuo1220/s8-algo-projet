from DFS import *
from generate_graph import *
from tools import *
import numpy as np


def geodesique(graph, tab):
    mark = set_mark(graph)
    all_gero_group_min = []
    # all lists that can generated by the graph
    for i in range(2, len(tab)+2):
        # all the subgroup in one single list
        for j in range(0, len(tab["list" + str(i)][0])):
            mark = set_mark(graph)
            # all the possible choices contained 2 points in a single subgroup
            l_of_2_point = find_two_point(tab["list" + str(i)][0][j])
            # for each possible choice contained 2 points
            for k in range(len(l_of_2_point)):
                # find the lists of all the shortest paths between these two points
                p = copy.copy(find_shortest_path(graph, l_of_2_point[k][0]-1, l_of_2_point[k][1]-1))
                # mark the list "mark" by the shortest paths found before
                for m in range(len(p)):
                    for n in p[m]:
                        mark[n] = mark[n] + 1
            if not zero_in_mark(mark):
                all_gero_group_min.append(tab["list" + str(i)][0][j])

        if all_gero_group_min:
            break
    return all_gero_group_min

if __name__=="__main__":
    
    """
    graph = [
        [0, 1, 9, 1, 9],
        [1, 0, 1, 9, 1],
        [9, 1, 0, 1, 1],
        [1, 9, 1, 0, 1],
        [9, 1, 1, 1, 0]
    ]
    """
    
    graph = creation(5)
    #graph=[[0,1,1,9],[1,0,9,1],[1,9,0,1],[9,1,1,0]]
    graph = np.asarray(graph)
    # graph = init_graphe_cercle(5)

    tab = ensemble(graph)
    
    re = geodesique(graph, tab)

    print("graph: \n", graph)
    print("geodesique ensemble: ", re)