import numpy as np
import random as rd
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

# Chaîne qui sert à déterminer si le graphe generé est connexe, les indices correspondent au sommet du graphe, si on viste un sommet : 1 sinon : 0
# Ainsi, si un graphe n'est pas connexe alors la liste connectivity contiendra au moins un 0, si il est connexe il y aura que des 1
connectivity=[]


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
    a=1
    for i in range(len(graph)):
        if (graph[start][i] == 1) & (book[i] == 0):
            if i == end:
                this_path.append(end)
                check_len(this_path)
                #show_path(this_path)
                this_path.pop()
                connectivity[i]=1
                #print(book)
                return "Done"
            else:
                book[i] = 1
                connectivity[i]=1
                #print(book)
                this_path.append(i)
                DFS(graph, i, end)
                this_path.pop()
                book[i] = 0
    if 0 in connectivity:
        a=0
    return a


#Fonction aléatoire servant à créer le graphe quelconque

def rand():
    return rd.choice([1,9])


#Création d'un graphe connexe quelconque en utilisant la fonction DFS

def creation(x):

    graph = np.eye(x,x) # On crée une matrice identité de taille x*x, des 1 sur la diagonale et de 0 sur le reste
    ok = 0 # booléen qui sert à verifier si la premiere ligne de la matrice contient au moins un 1
    
    ## Upgrade
    if(len(graph)==2):
    	graph=[[0,1],[1,0]]
    	return graph
    
    # Initialisation des différents tableaux

    lenth_min = 999
    shortest_paths.clear()
    this_path.clear()
    book.clear()
    connectivity.clear()

    for i in range(len(graph)):
        book.append(0)

    for j in range(len(graph)):
        connectivity.append(0)

    # the starting point must mark to 1 in the first time
    book[0] = 0
    connectivity[0]=0

    # add starting point to the path
    this_path.append(0)

    # On remplace els 1 de la matrice identité par des 0 et les 0 par des 3 (valeur intermeiaire qui sera remplacé soit par un 1 (connexion) ou un 9(non connecté))
    for i in range(x):
        for j in range(x):
            if graph[i][j]==0:
                graph[i][j]=3
            else:
                graph[i][j]=0
    
    # Tant que la premiere ligne n'a pas au moins une connexion
    while ok !=1:
        for init in range(x):
            if (graph[0][init]==3) | (graph[0][init]==9):
                graph[0][init]=rand() # On y assigne soit un 1 ou un 9

        for verif in range(x): # On vérifie que le sommet 1 soit connecté au minimum par un sommet
            if graph[0][verif]==1:
                ok=1
   
    # Pour generer le reste de la matrice, on prend en compte les lignes precedentes
    for i in range(1,x):
        for j in range(x):
            if graph[i][j]==3:
                if graph[j][i]==1:
                    graph[i][j]=1

                elif graph[j][i]==9:
                    graph[i][j]=9

                else:
                    graph[i][j]=rand()
    
    
    # On vérifie la connexité du graphe généré, si elle n'est pas respecté, on recommence l'opération
    DFS(graph,0,1)
    if 0 in connectivity:
        return creation(x)

    return graph


# Création d'un graphe en cercle :

def init_graphe_cercle(x):
    graphe = np.zeros((x, x))
    for i in range(x):
        for j in range(x):

            if i == j:
                graphe[i][j] = 0

            elif i == j + 1:
                graphe[i][j] = 1

            elif j == i + 1:
                graphe[i][j] = 1

            elif j == x - 1 and i == 0:
                graphe[i][j] = 1

            elif j == 0 and i == x - 1:
                graphe[i][j] = 1

            else:
                graphe[i][j] = 9
    return graphe


# Permet de créer plusieurs listes égale au nombre de demandes

def createListe(nom, x):
    result = {}
    if(x==2):
    	result[nom+str(2)]=[]
    	return result 
    for i in range(2, x):
        name = nom + str(i)
        result[name] = []
    return result


# Permet de déterminer tous les ensembles d'une liste

def ensemble(x):
    taille = x.shape
    res = createListe("list", taille[0])
    if taille[0]==2:
    	res["list" + str(2)].append(globals()['ensemble' + str(2)](x))
    	return res
    	
    for i in range(2, taille[0]):
        res["list" + str(i)].append(globals()['ensemble' + str(i)](x))
    return res


def ensemble2(x):
    taille = x.shape
    tab = []
    for i in range(taille[0]):
        for j in range(taille[0]):
            if i != j:
                a = [i + 1, j + 1]
                a.sort()
                if a not in tab:
                    tab.append(a)
    return tab


def ensemble3(x):
    taille = x.shape
    tab = []
    for i in range(taille[0]):
        for j in range(taille[0]):
            for k in range(taille[0]):
                if i != j and i != k and j != k:
                    a = [i + 1, j + 1, k + 1]
                    a.sort()
                    if a not in tab:
                        tab.append(a)
    return tab


def ensemble4(x):
    taille = x.shape
    tab = []
    for i in range(taille[0]):
        for j in range(taille[0]):
            for k in range(taille[0]):
                for l in range(taille[0]):
                    if i != j and i != k and j != k and l != k and l != j and l != i:
                        a = [i + 1, j + 1, k + 1, l + 1]
                        a.sort()
                        if a not in tab:
                            tab.append(a)
    return tab


