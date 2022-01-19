
def find_two_point(list_of_point):
    taille = len(list_of_point)
    tab = []
    for i in range(taille):
        for j in range(taille):
            if i != j:
                a = [list_of_point[i], list_of_point[j]]
                a.sort()
                if a not in tab:
                    tab.append(a)
    return tab

def set_mark(graph):
    mark = [0 for i in range(graph.shape[0])]
    return mark

def zero_in_mark(mark):
    return (0 in mark)