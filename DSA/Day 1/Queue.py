class queue:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements = ['None']* self.__max_size
        self.__front = 0
        self.__rear = -1
    def is_full(self):
        if (self.__rear == self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.__front > self.__rear):
            return True
        return False
    def enqueue(self,data):
        if(self.is_full()):
            print('Queue is full')
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data
            
        
    def dequeue(self):
        if(self.is_empty()):
            print('The queue is empty')
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data
        
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])
        
    def get_max_size(self):
        return self.__max_size
Queue1 = queue(10)
print('Is it full',Queue1.is_full())
print('Is it empty',Queue1.is_empty())
Queue1.enqueue(500)
Queue1.enqueue(600)
Queue1.enqueue(700)
Queue1.enqueue(800)
Queue1.display()
print("element deleted",Queue1.dequeue())
Queue1.display()
print('Size of queue',Queue1.get_max_size())
