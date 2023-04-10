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
    def insertionatbegining(self,data):
        newNode = Node(data)
        newNode.nextval = self.headval
        self.headval = newNode
list = Slinkedlist()
list.headval = Node('Monday')
e2 = Node('Tuesday')
e3 = Node('Wednesday')
list.headval.nextval = e2
e2.nextval = e3
list.insertionatbegining('Sunday')
list.listprint()
