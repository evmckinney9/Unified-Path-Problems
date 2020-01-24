class DirectedGraph():
    def __init__(self):
        self.edges = []
        self.vertexes = []

    #regard edge as leading from head to tail
    def addEdge(self, edge):
        self.edges.append(edge)

    def addVertex(self, vertex):
        self.vertexes.append(vertex)

    def getVertex(self, label):
        for v in self.vertexes:
            if (v.label == label):
                return v
        return None
    
    def calcVertexValue(self, label):
        value = 0
        for e in self.edges:
            if (e.tail.label == label):
                head = e.head.value
                if head == None:
                    print("missing vertex value!")
                    return None
                value += e.weight * e.head.value
        self.getVertex(label).value = value
        return value

class Vertex():
    def __init__(self, label, value):
        self.label = label
        self.value = value

class Edge():
    def __init__(self, weight, head, tail):
        self.weight = weight
        self.head = head
        self.tail = tail

def matrixInputScan():
    print("Convert system Ax=b into direct graph.")
    n = int(input ("n:="))
    raw_A = input("Enter matrix A row-wise:\n")
    raw_B = input("Enter matrix B row-wise:\n")

    A = []
    raw_A = [x for x in raw_A if x.isdigit()]
    if len(raw_A) != n**2:
        print("A not size(n x n)!")
        exit()
    for i in range(n):
        a = []
        for j in range(n):
            a.append(raw_A[n*i + j])
        A.append(a)
    
    B = []
    raw_B = [x for x in raw_B if x.isdigit()]
    if len(raw_B) != n:
        print("B not size(n)!")
        exit()
    B = raw_B

    return [A,B,n]

def calcAprime(A,B,n):
    #size is (n+1 x n+1)
    IsubA = []
    for i in range(n):
        IsubA_temp = []
        for j in range(n):
            if i==j:
                IsubA_temp.append(1-int(A[i][j]))
            else:
                IsubA_temp.append(0-int(A[i][j]))
        IsubA.append(IsubA_temp)

    #print(IsubA)
    Ap = []
    Ap.append([0 for i in range(n+1)])
    for i in range(0, n):
        Ap_temp = []
        Ap_temp.append(B[i])
        for x in IsubA[i]:
            Ap_temp.append(x)
        Ap.append(Ap_temp)

    #print(Ap)
    return Ap

def constructGraph(A_prime, n):
    diG = DirectedGraph()

    #create vertexes 
    for i in range(n+1):
        value = 1 if i==0 else None 
        v = Vertex(f"x_{i}", value)
        diG.addVertex(v)

    #create edges
    for i in range(n+1):
        for j in range(n+1):
            if (A_prime[i][j] != 0):
                e = Edge(int(A_prime[i][j]), diG.getVertex(f"x_{j}"), diG.getVertex(f"x_{i}"))
                diG.addEdge(e)\
    
    return diG




def main():
    #only n variables, not sure yet how alg does a (nxl) matrix of variables
    A,B,n = matrixInputScan()
    A_prime = calcAprime(A,B,n)
    diG = constructGraph(A_prime, n)

    #need a clever way to iterate through the nodes, but doesn't solve problem if has edge to itself!
    v1= diG.calcVertexValue("x_1")
    print(v1)
    v2= diG.calcVertexValue("x_2")
    print(v2)

if __name__ == "__main__":
    main()