# Code is taken from https://www.programiz.com/ 
class circularQueue():
    def __init__(self, k):
        self.k = k
        self.queue = [None]*k
        self.head = self.tail = -1
    
    def enqueue(self, data):
        if((self.tail+1) % self.k == self.head):
            print('the queue is full \n')
        
        elif(self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail+1) % self.k
            self.queue[self.tail] = data
    def dequeue(self):
        if self.head == -1:
            print('queue is empty!')
        elif(self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head+1) % self.k
            return temp




