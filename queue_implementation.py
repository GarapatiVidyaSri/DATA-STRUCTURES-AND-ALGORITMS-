print("------------QUEUE IMPLEMENTATION---------")
class queue():
    def __init__(self,size):
        self.items=[]
        self.size=size
        self.front=-1
        self.rear=-1
    def enqueue(self,item):
        if self.front==0 and self.rear==self.size-1:
            print("overflow")
        if self.front==-1 and self.rear==-1:
             self.front+=1
             self.rear+=1
             return self.items.append(item)
        else:
            self.rear+=1
            return self.items.append(item)
    def dequeue(self):
         if self.front==-1 and self.rear==-1:
             print("underflow")
         if self.front==self.rear:
             self.front=-1
             self.rear=-1
             return self.items
         else:
             self.front=+1
             return self.items
        
q=queue(9)
q.enqueue(8)
q.enqueue(3)
q.enqueue(8)
q.enqueue(3)
q.enqueue(8)
q.enqueue(3)
q.enqueue(8)
q.enqueue(3)
q.enqueue(8)
q.enqueue(3)
q.enqueue(8)
q.enqueue(3)

q.dequeue()
q.dequeue()
print(q.items[q.front:q.rear])
            
            
        
        
