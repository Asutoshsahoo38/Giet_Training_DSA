## Traversing a linked list
class Node:
    def __init__(self,dataval = None):
        self.dataval = dataval
        self.nextval = None
class SlinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
list = SlinkedList()
list.headval = Node('sunday')
e2 = Node("Tuesday")
e3 = Node("Wednesday")
list.headval.nextval = e2
e2.nextval = e3
list.listprint()
