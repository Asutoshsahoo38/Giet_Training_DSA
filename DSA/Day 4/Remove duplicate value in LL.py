class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def isempty(self):
        if self.head == None:
            return True 
        return False
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end = " ")
            temp = temp.next
    def SLinkedList(self,data):
        new_node = Node(data)
        if self.isempty():
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
    def checkduplicates(self):
        ptr1 = None
        ptr2 = None
        ptr1 = self.head
        while(ptr1 != None and ptr1.next != None):
            ptr2 = ptr1
            while(ptr2.next != None):
                if(ptr1.data == ptr2.next.data):
                    ptr2.next = ptr2.next.next
                else:
                    ptr2 = ptr2.next
            ptr1 = ptr1.next        
ls = LinkedList()
ls.SLinkedList(10)
ls.SLinkedList(20)
ls.SLinkedList(30)
ls.SLinkedList(40)
ls.SLinkedList(50)
ls.SLinkedList(10)

ls.printList()
print("\nAfter removing the duplicate values")
ls.checkduplicates()
ls.printList()
