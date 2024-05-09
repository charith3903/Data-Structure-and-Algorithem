#singly linkedlist
class Node :
    def __init__(self,value=None):
        self.value = value
        self.next = None



class sll:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            
    def print(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            node = self.head
            while node is not None:
                print(node.value,end=" ")
                node = node.next
            print()
            
    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode    
        
        
linkedList = sll()
node1= Node(4)
node2= Node(8)
node3= Node(5)
node4= Node(5)
node5= Node(8)


linkedList.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
linkedList.tail = node5

for node in linkedList:
    print(node.value)
    
    
## traverse the singly linked list
linkedList.print()

## Insert the node at the end of the singly linked list
linkedList.insert(10,0)
linkedList.print()
linkedList.insert(101,-1)
linkedList.print()
linkedList.insert(101,4)
linkedList.print()