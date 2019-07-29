# making the node class
class Node:
    def __init__(self, name):
        self.name = name
        # list containing adjacent nodes
        self.adjacencyList = []
        # whether a node is visited or not
        self.visited = False
        # not useful in current case
        self.predecessors = None


class BreadthFirstSearch:
    def bfs(self, startNode):

        # we use queue as the abstract data type in BFS
        # for proper queue usage with best Big-O, i prefer using the queue module or
        # making a queue data type, but here for example purposes, this will do
        queue = []
        # add the startNode to queue
        queue.append(startNode)
        # set startNode to be visited
        startNode.visited = True

        # while there is a queue
        while queue:
            # pops the first item from the queue and set it's value as the value of actualNode
            actualNode = queue.pop(0)
            # prints the name of popped item
            print("{}".format(actualNode.name))

            # for each element/node 'n' in adjacency list
            for n in actualNode.adjacencyList:
                # if a node is not visited 
                if not n.visited:
                    # set it to visited and add it to the queue
                    n.visited = True
                    queue.append(n)



# TESTING ---
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")


node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node4.adjacencyList.append(node5)
node4.adjacencyList.append(node6)
node4.adjacencyList.append(node7)


bfs = BreadthFirstSearch()
bfs.bfs(node1)

