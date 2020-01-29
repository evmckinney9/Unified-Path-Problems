def createDominatorTree(G):
    return G

def DECOMPOSE_AND_SEQUENCE(G):
    n = len(G.vertices)
    m = len(G.edges)
    T = createDominatorTree(G)
    
    #initalize
    for v in G.vertices:
        INITALIZE(v)

    sequence = ""

    #loop
    for u in range(1,n):

        #derive
        for v in children(u):
            for e in nonTree(v, T):
            pass
                



def INITALIZE(v):
    pass


def children(u):
    #return children of vertex numbered u
    pass

def nonTree(v, T):
    #edges that are not in T, tail is v, head is not idiom(u)