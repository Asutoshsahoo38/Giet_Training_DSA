class Node:
    def __init__(self,dataval):
        self.dataval = dataval
        self.nextval = None
class Slinkedlist:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    def Inbetween(self,middle_node,data):
        if middle_node is None:
            print("The mention element is not available ")
        else:
            newNode = Node(data)
            newNode.nextval =middle_node.nextval
            middle_node.nextval = newNode
            
list = Slinkedlist()
list.headval = Node('Monday')
e2 = Node('Tuesday')
e3 = Node('Wednesday')
list.headval.nextval = e2
e2.nextval = e3
list.Inbetween(list.headval.nextval,'sat')
list.listprint()
