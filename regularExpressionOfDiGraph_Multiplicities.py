#this algorithm assumes that the DiGraph passed is an Acylic Directed Graph

def computeRegularExpression(dag):
    #the total expression
    regularExpression = ""

    #the roots and leaves of the DAG
    #TODO DAG class needs these
    dagLeaves = dag.getLeafNodes()
    dagRoot = dag.getRootNode()

    #implementation of a O(n) solution to count paths
    stack = []
    multiplicties = {}
    triggers = {}

    #handle some trivial edge cases
    if (dagRoot == null):
        #function is empty, there are no paths
        return regularExpression
    elif (dagRoot in dagLeaves):
        #function contains a single node
        regularExpression += dagRoot.toString()
        return regularExpression

    multiplicties[dagRoot] = dagRoot.toString()
    stack.append(dagRoot)

    #L: stop if stack is empty
    while (len(stack) > 0):

        #pop a node
        v = stack.pop()

        #for each successor s of v
        for (outgoingEdge in dag.forwardStep(v.edges())): #TODO implement in inner class

            s = outgoingEdge.tail() #dag has edges head -> tail in Tarjan notation

            if (not s in multiplicties.keys()):
                multiplicties[s] = s.toString())
            if (not s in triggers.keys()):
                triggers[s] = len(dag.reverseStep(s)) #TODO implement in inner class

            between = len(dag.betweenStep(v,s))

            #M(s) = M(s) + need some way to calculate regular expression operator
            value = multiplicities[s] + "~some operator~" + multiplicties[v]
            multiplicties[s] = value

            #T(s) = T(s) = (#edges from v to s)
            value = triggers[s] - between
            triggers[s] = value

            #if T(s) == 0
            if (triggers[s] == 0):
                #if (s is leaf) np = np + M(s)
                if (s in dagLeaves):
                    regularExpression += multiplicties[s]
                    #TODO, fix

                #else Push s
                else:
                    stack.append(s)
