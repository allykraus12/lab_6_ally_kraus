from lab6problem1 import Node

class LinkedList:
	def __init__(self, head, tail):
		self.head = head 
		self.tail = tail 

	def getHead(self,head):

		self.head == head 

	def getSize(self):

		nodeCount = 0
		currentNode = head
		while True:
			if currentNode.nextPointer is None:
			    return nodeCount         
        	currentNode = currentNode.nextPointer
        	nodeCount = nodeCount + 1

        return nodeCount

	def getTail(self):
		
		self.tail = tail

 	def addNode(self,data):
 		nodeVariable = Node()
 		nodeVariable.setData(data)

 		if self.getSize()==0:
 			head = nodeVariable

def main():

	linkedList1 = LinkedList(head=None, tail=None)



	print(linkedList1.getSize())

	print(linkedList1.addNode("data1"))

	print(linkedList1.getSize())




if __name__ == '__main__':
	main()


	