# creating a node class
class Node:
    def __init__(self,data):
        self.data = data 
        self.leftChild = None
        self.rightChild = None

# creating the BST class
class BinarySearchTree:

    def __init__(self):
        self.root = None

    # insert function
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    # insert sub function
    def insertNode(self, data, node):
        # if the new data is less than root
        if data < node.data:
            # if there is a left child
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            # if there is not left child
            else:
                node.leftChild = Node(data)
        # if the new data is bigger than root
        else:
            # if there is a right child
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            # if there is not a right child
            else:
                node.rightChild = Node(data)


    # function for getting minimum value
    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    # sub function of getMinValue()
    def getMin(self, node):
        # we know left child are always less than right child, so we'll find 
        # minimum value in left side, thereby we check if there is a left child
        if node.leftChild:
            return self.getMin(node.leftChild)

        # when recursively we reach a point when there is no left child, it
        # means we have reached the minimum number, and we return it
        return node.data


    # function for getting maximum value
    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)

    # sub function of getMaxValue()
    def getMax(self, node):
        # we know right child are always bigger than left child, so we'll find 
        # maximum value in right side, thereby we check if there is a right child
        if node.rightChild:
            return self.getMax(node.rightChild)

        # when recursively we reach a point when there is no right child, it
        # means we have reached the maximum number, and we return it
        return node.data


    # function to traverse the bst
    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    # sub function of traverse() which is called recursively
    def traverseInOrder(self, node):
        # if there is a left child
        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        # prints the current node data
        print("{}".format(node.data))

        # if there is a right child
        if node.rightChild:
            self.traverseInOrder(node.rightChild)


    # function to remove a node
    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    # sub function of remove() called recursively
    def removeNode(self, data, node):

        # if the input is None, return None
        if not node:
            return node

        # if the data to remove is less than the current node data
        if data < node.data:
            # we update the left child
            node.leftChild = self.removeNode(data, node.leftChild)
        # if the data to remove is more than the current node data
        elif data > node.data:
            # we update the right child
            node.rightChild = self.removeNode(data, node.rightChild)
        # else when we reach the node we have to remove
        else:

            # we encounter 3 cases
            # CASE 1 - the node to remove is a leaf node
            if not node.leftChild and not node.rightChild:
                print("Removing a leaf node...")
                del node
                return None

            # CASE 2 - the node to remove has a right child or left child
            if not node.leftChild:
                print("Removing a node with single right child...")
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print("Removing a node with single left child...")
                tempNode = node.leftChild
                del node
                return tempNode

            # CASE 3 - the node to remove has 2 children
            print("Removing a node with two children...")
            # we call getPredecessor() to get the predecessor to replace the node
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data 
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        return node

    # the method to get predecessor when removing a node with 2 children
    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)

        return node            

# TESTING -----

bst = BinarySearchTree()

# Number test
# bst.insert(10)
# bst.insert(5)
# bst.insert(15)
# bst.insert(6)

bst.insert(10)
bst.insert(13)
bst.insert(5)
bst.insert(14)

bst.remove(10)

# Character test
# bst.insert("C")
# bst.insert("A")
# bst.insert("Z")
# bst.insert("G")

# print(bst.getMinValue())
# print(bst.getMaxValue())
bst.traverse()