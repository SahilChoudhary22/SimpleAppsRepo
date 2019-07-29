""" In BFS, we use queue because it's based on FIFO structure, on the other hand
in DFS, we use stacks because it's based on LIFO structure. In python, when we use
recursion, it automatically uses stacks in the background. """


# making a node class
class Node:
	def __init__(self, name):
		# the name of node
		self.name = name
		# boolean whether the node is visited or not
		self.visited = False
		# will store the children nodes
		self.adjacencyList = []
		self.predecessor = None

# creating a class DepthFirstSearch
class DepthFirstSearch:

	def dfs(self, startNode):

		## stack = [] or we just use recursion and in the background
		## it'll be automatically using stacks for storage
		startNode.visited = True
		# print each visited node name
		print("{}".format(startNode.name))

		# for each node n in adjacencyList
		for n in startNode.adjacencyList:
			# if the node is not visited
			if not n.visited:
				# call the function recursively
				self.dfs(n)


# TESTING, same nodes as in BFS.py
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

dfs = DepthFirstSearch()
dfs.dfs(node1)


# output should be
# A
# B
# D
# E
# F
# G
# C