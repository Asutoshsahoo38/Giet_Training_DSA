##Take input of some numbers and print the number which are divisible by every element in th range i.e 1 to 10
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
            for i in range(1,10+1):
                if(self.__elements[index] % i ==0):
                    s = True
                else:
                    s = False
                    break
            if(s):
                print(self.__elements[index])
                
        
    def get_max_size(self):
        return self.__max_size
Queue1 = queue(10)
print('Is it full',Queue1.is_full())
print('Is it empty',Queue1.is_empty())
Queue1.enqueue(13983)
Queue1.enqueue(10080)
Queue1.enqueue(7113)
Queue1.enqueue(2520)
Queue1.enqueue(2500)
Queue1.display()

