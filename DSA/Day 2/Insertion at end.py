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
    def insertionatend(self,data):
        newNode = Node(data)
        if self.headval == None:
            self.headval = newNode
            return
        else:
            last = self.headval
            while(last.nextval):
                last = last.nextval
            last.nextval = newNode    
list = Slinkedlist()
list.headval = Node('Monday')
e2 = Node('Tuesday')
e3 = Node('Wednesday')
list.headval.nextval = e2
e2.nextval = e3
list.insertionatend('Thrusday')
list.listprint()
