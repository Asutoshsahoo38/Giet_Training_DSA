## Double Linked List 
class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
class DoubleLinkedlist:
    def __init__(self):
        self.head =  None
    def is_empty(self):
        if self.head == None:
            return True 
        return False    
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node    
    def insert_at_beginning(self,data):
        new_node = Node(data)
        if (self.is_empty()):
            self.head = new_node
        else:
            next_node = self.head
            new_node.next = self.head
            self.head = new_node
            new_node.next.prev = next_node
            
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end = ' ')
            temp = temp.next
llist = DoubleLinkedlist()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
print('Given Linked List ')
llist.printList()
llist.insert_at_beginning(21)
print('\nafter insert_at_beginning')
llist.printList()


