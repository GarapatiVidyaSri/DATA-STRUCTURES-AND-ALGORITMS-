class circularqueue():
    def __init__(self,size):
        self.items=[25,30,45]
        self.size=size
        self.front=0
        self.rear=2
    def enqueue(self,item):
        if (self.front==0  and self.rear==self.size-1 or self.front==self.rear+1):
            print("overflow")
        elif (self.front==-1 and self.rear==-1):
            self.front= self.front+1
            self.rear=self.rear+1
            self.items.insert(self.rear,item)
            return self.items
        else:
            self.rear=(self.rear+1)%self.size
            self.items.insert(self.rear,item)
            return self.items
    def dequeue(self):
        if (self.front==-1 and self.rear==-1):
            print("underflow")
        elif (self.front==self.rear):
            self.items.pop(self.front)
            self.front=-1
            self.rear=-1
            return self.items
        else:
            self.items.pop(self.front)
            self.front=(self.front+1)%self.size
            return self.items
q=circularqueue(4)
print(q.items)
q.enqueue(55)
print(q.items)
q.dequeue()
print(q.items)
q.enqueue(75)
print(q.items)
q.dequeue()
print(q.items)
q.enqueue(85)
print(q.items)
q.enqueue(90)
print(q.items)
q.enqueue(100)
print(q.items)
if q.front<q.rear:
    print(q.items[q.front:])
else:
    print(q.items[0:q.rear+1]+q.items[q.front:])
