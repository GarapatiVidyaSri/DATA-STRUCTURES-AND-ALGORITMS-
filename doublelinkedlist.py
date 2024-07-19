class node():
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class doublelinkedlist():
    def __init__(self):
        self.head=None
        self.tail=None
    def insertionatbegin(self,data):
        if self.head!=None:
            newnode=node(data)
            self.head.prev=newnode
            newnode.next=self.head
            self.head=newnode
            newnode.prev=None
           
        elif self.head==None:
            newnode=node(data)
            self.head=self.tail=newnode
            self.tail.next=None
            
    def insertionatend(self,data):
        if self.head!=None:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            newnode=node(data)
            newnode.prev=temp
            temp.next=newnode
            newnode.next=None
            
        else:
            newnode=node(data)
            newnode.prev=None
            self.head=newnode
            #return self.head.data
    def deletionatbegin(self):
        if self.head==None:
            print("empty list")
        else:
            temp=self.head
            self.head=temp.next
            self.head.prev=None
            temp=None
            #return
    def insertionatmiddle(self,data,position):
        if self.head!=None:
            temp=self.head
            i=0
            while i<position-1:
                temp=temp.next
                i+=1
            newnode=node(data)
            newnode.prev=temp
            newnode.next=temp.next
            temp.next.prev=newnode
            temp.next=newnode
            
    def deletionatend(self):
        if self.head!=None:
            tenp=self.head
            i=0
            while(tenp.next!=None):
                tenp=tenp.next
                i+=1
            tem=self.head
            while i>1:
                tem=tem.next
                i-=1
            prev=tem
            prev.next=None
            tenp=None
    def deletionatposition(self,position):
        if self.head!=None:
            temp=self.head
            i=0
            while i<position:
                temp=temp.next
                i+=1
            tem=self.head
            while i>1:
                tem=tem.next
                i-=1
            prev=tem
            prev.next=temp.next
            temp.next.prev=prev
            temp=None
    def traversal(self):
        if self.head!=None:
            temp=self.head
            while temp!=None:
                print(temp.data)
                temp=temp.next
    def deletekey(self,key):
        if self.head!=None:
            temp=self.head
            i=0
            while temp.data!=key and temp.next!=None:
                temp=temp.next
                #print(temp.data)
            
                i+=1
            tem=self.head
            #print(temp.data)
            while i>1:
                tem=tem.next
                i-=1
                
            prev=tem
            #print(prev.data)
            if  temp.next!=None:
                
                prev.next=temp.next
                temp.next.prev=prev
                temp=None
            else:
                prev.next=None
                temp=None
        
                
            
                
    def reversedisplay(self):
        if self.head!=None:
            temp=self.tail
            #print(temp.data)
        while temp!=None:
            print(temp.data)
            temp=temp.prev

    def reversal(self):
        if self.head!=None:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            tail=temp
            while tail!=None:
                print(tail.data)
                tail=tail.prev
            
            
q=doublelinkedlist()
q.insertionatbegin(5)
q.insertionatbegin(8)
q.insertionatbegin(9)
#q.insertionatmiddle(3,2)
q.insertionatend(7)
q.insertionatbegin(4)
q.insertionatend(1)
q.deletionatbegin()
q.insertionatbegin(6)
q.insertionatmiddle(3,2)
q.insertionatbegin(8)
q.deletionatend()
q.deletionatposition(2)
q.insertionatend(1)
q.deletekey(5)
#q.traversal()
#q.reversedisplay()
q.reversal()
q.insertionatmiddle(3,1)
q.insertionatmiddle(2,2)
q.deletionatposition(1)

temp=q.head
while temp!=None:
    print(temp.data)
    temp=temp.next
print("null")
    
        
    
