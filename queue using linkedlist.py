print("-----------------QUEUE IMPLEMENTATION USING LINKEDLIST--------------")
class node():
    def __init__(self,data):
        self.data=data
        self.next=None

class queue():
    
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,data):
        if self.rear==None:
            newnode=node(data)
            self.front=self.rear=newnode
            #print(self.front.data)
            return
        
        
        else:
            newnode=node(data)
            self.rear.next=newnode
            self.rear=self.rear.next
            #print(self.front.data)
            return
    def dequeue(self):
        if self.front==None:
            return None
        else:
            to_return = self.front.data
            self.front = self.front.next
            return to_return
 
        
    
        
q=queue()
#q.enqueue(5)
q.enqueue(7)
print(q.data)

            
            
            
