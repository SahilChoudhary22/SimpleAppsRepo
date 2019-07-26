class Node:
    def __init__(self, data):
        # data container
        self.data = data
        # initially we set the nextNode to none because the list is empty
        self.nextNode = None


class LinkedList:
    def __init__(self):
        # this is the root of the list
        self.head = None
        # this will count the size of the list and increment with each insertion
        self.size = 0
    
    # O(1) time complexity, this is the primary reason for using LinkedLists
    def insertAtStart(self, data):
        
        self.size = self.size + 1
        newNode = Node(data)
        
        # if there is no root, the inserted element becomes root
        if not self.head:
          self.head = newNode
        # else, it sets the next node to current root node i.e. head and the new node becomes new head
        else:
          newNode.nextNode = self.head
          self.head = newNode

    # O(1) time complexity
    def size_1(self):
      return self.size

    # size function with O(n) time complexity
    def size_by_iteration(self):

      size = 0
      actualNode = self.head

      while actualNode is not None:
        size += 1
        actualNode = actualNode.nextNode

      return size
     
    # this has O(n) time complexity
    def insertAtEnd(self, data):

      self.size = self.size + 1
      newNode = Node(data)
      actualNode = self.head

      while actualNode.nextNode is not None:
        actualNode = actualNode.nextNode

      actualNode.nextNode = newNode

    
    # this also has O(n) time complexity
    def traverse_the_list(self):

      actualNode = self.head
      while actualNode is not None:
        print("{}".format(actualNode.data))
        actualNode = actualNode.nextNode

    # O(n) time complexity
    def remove_an_element(self,data):
      # if the list is empty, just return
      if self.head is None:
        return

      # decrement the size
      self.size = self.size - 1
      previousNode = None
      currentNode = self.head

      # while the current node data is not equal to the data we want to delete
      while currentNode.data != data:
        previousNode = currentNode
        currentNode = currentNode.nextNode

      # if the data to remove is the root
      if previousNode is None:
        self.head = currentNode.nextNode
      # if the data to remove is not the root, we just point the previous node to the next node of current node
      else:
        previousNode.nextNode = currentNode.nextNode


# testing
LinkedListtt = LinkedList()
LinkedListtt.insertAtStart(2)
LinkedListtt.insertAtStart(4)
LinkedListtt.insertAtStart(7)
LinkedListtt.insertAtStart(12)
LinkedListtt.insertAtStart(10)
LinkedListtt.insertAtEnd(1111)
LinkedListtt.insertAtEnd(1122)
LinkedListtt.insertAtEnd(1133)
LinkedListtt.remove_an_element(1111)

LinkedListtt.traverse_the_list()
print("this is the size of LinkedList: " + str(LinkedListtt.size_1()))







