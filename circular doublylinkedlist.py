print("----------------CIRCULAR DOUBLE LINKEDLIST-----------------")
class node():
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class circulardoublylinkedlist():
    def __init__(self):
        self.head=None
        self.tail=None
    def insertionatbegin(self,data):
        if self.head==None:
            newnode=node(data)
            self.head=self.tail=newnode
            return
        else:
            newnode=node(data)
            newnode.prev=self.tail.next
            newnode.next=self.head
            self.head=newnode
            return
    def insertionatend(self,data):
        if self.tail!=None:
            newnode=node(data)
            newnode.prev=self.tail.next
            
            newnode.next=self.tail.next
            self.head=newnode
            self.tail.next=newnode
            #print(self.tail.data)
            return
            

q=circulardoublylinkedlist()
q.insertionatbegin(2)
q.insertionatbegin(1)
q.insertionatbegin(0)
q.insertionatbegin(3)
q.insertionatend(5)


temp=q.head
while temp!=q.tail.next:
    print(temp.data)
    temp=temp.next
    
