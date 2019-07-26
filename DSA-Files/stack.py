""" Stacks is an abstract data type and follows LIFO structure i.e. Last In, First Out
As popping and pushing of last element follows linear time complexity O(n) in arrays,
we use python lists to make arrays """

class Stack:

	# constructor basically
	def __init__(self):
		self.stack = []

	# check if stack is empty
	def isEmpty(self):
		return self.stack == []

	# push new data on top
	def push(self, data):
		self.stack.append(data)
 
	# pop out last element
	def pop(self):
		data = self.stack[-1]
		del self.stack[-1]
		return data

	#peek from top
	def peek(self):
		return self.stack[-1]
		
	# return the size of stack
	def sizeOfStack(self):
		return len(self.stack)


# testing
stack = Stack()
stack.push(2)
stack.push(34)
stack.push(23)
stack.push(11)
stack.pop()
stack.push(22)
stack.push(99)
stack.pop()

print(stack.peek())

print("the size of stack is : " + str(stack.sizeOfStack()))