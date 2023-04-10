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
    def insert_at_position(self,data,position):
        temp = self.head
        count = 1
        while temp is not None:
            if count == position - 1:
                break
            else:
                count += 1
                temp = temp.next
            if position == 1:
                self.insert_at_beginning(data)
            elif temp.next == None:
                self.insert_at_end(data)
            else:
                new_node = Node(data)
                new_node.next = temp.next
                new_node.previous = new_node
                temp.next = new_node
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.insert_at_beginning(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
    def delete_from_beginning(self):
        if self.is_empty():
            print("Linked List is empty")
        elif self.head.next == None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.previous = None
    def delete_at_position(self,position):
        if self.is_empty():
            print('Empty')
        elif(position == 1):
            self.delete_from_beginning()
        else:
            
            count = 1
            temp = self.head
            while temp is not None:
                if count == position:
                    break
                temp = temp.next
                count = count+1
            if temp is None:
                print("There are less than {} elements in LL".format(position))
                return
            elif temp.next is None:
                self.delete_from_end()
                return
            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp.next = None
                temp.prev = None
                
                
    def delete_from_end(self):
        if self.is_empty():
            print("The list has no element to delete")
            
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end = ' ')
            temp = temp.next
llist = DoubleLinkedlist()
llist.push(20)
llist.insert_at_end(4)
llist.insert_at_end(5)
llist.insert_at_end(6)
llist.insert_at_end(7)



print('Given Linked List ')
llist.printList()
llist.insert_at_beginning(21)
print('\nafter insert_at_beginning')
llist.printList()
llist.insert_at_position(90,2)
print('\nafter insert at position')
llist.printList()
print('\nDelete from the beginning')
llist.delete_from_beginning()
llist.printList()
print('\nAfter deleting the element from the end')
llist.delete_from_end()
llist.printList()
print('\nAfter delete from position 4')
llist.delete_at_position(2)
llist.printList()



