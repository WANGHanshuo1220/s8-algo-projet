import copy

# Whether the marker has been visited，0 means not, 1 means yes.
# list book[] is initialised in main function
book = []

# indicate the len of the shortest path right now
# initialised to infinite(9999)
lenth_min = 9999

# a list contained all the shortest paths
shortest_paths = []

# the path the algo is working on
this_path = []


# being used when algo has already found a path from the starting point to the ending point
# check if this path is shorter than what have been save in list shortest_paths
def check_len(path):
    global lenth_min
    _path = copy.copy(path)
    if (len(_path) < lenth_min):
        lenth_min = len(_path)
        shortest_paths.clear()
        shortest_paths.append(_path)
    elif (len(_path) == lenth_min):
        shortest_paths.append(_path)


# just for visualization, when a path has been found
def show_path(path):
    print("path from start to end: ", end=" ")
    for i in range(len(path)):
        print(path[i], end=" ")
    print(" ")


def DFS(graph, start, end):
    for i in range(len(graph)):
        if (graph[start][i] == 1) & (book[i] == 0):
            if i == end:
                this_path.append(end)
                check_len(this_path)
                # show_path(this_path)
                this_path.pop()
                return "Done"
            else:
                book[i] = 1
                this_path.append(i)
                DFS(graph, i, end)
                this_path.pop()
                book[i] = 0


def find_shortest_path(graph, start, end):
    global lenth_min
    # reset the variable global
    lenth_min = 999
    shortest_paths.clear()
    this_path.clear()
    book.clear()

    # initialise the list book[]
    for i in range(len(graph)):
        book.append(0)

    # the starting point must mark to 1 in the first time
    book[start] = 1

    # add starting point to the path
    this_path.append(start)

    # run the algo
    DFS(graph, start, end)

    return shortest_paths
