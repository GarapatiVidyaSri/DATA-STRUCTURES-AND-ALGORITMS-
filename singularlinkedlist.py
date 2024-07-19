class node():
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.prev=None
        self.next=None
class link():
    def __init__(self):
        self.head=None
    def insertionatbegin(self,data):
        if self.head==None:
            newnode=node(data)
            self.head=newnode
            return self.head.data
        else:
            newnode=node(data)
            newnode.next=self.head
            self.head=newnode
            return self.head.data
   
    def insertionatend(self,data):
        if self.head!=None:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            newnode=node(data)
            newnode.next=None
            temp.next=newnode
            return temp.next.data
    def insertionatposition(self,data,position):
        if self.head!=None:
            temp=self.head
            i=0
            while(i!=position-1):
              temp=temp.next
              i+=1
            if temp!=None:
                newnode=node(data)
                newnode.next=temp.next
                temp.next=newnode
                return temp.next.data
    def deletionatbegin(self):
        if self.head!=None:
            temp=self.head
            if temp!=None:
                self.head=temp.next
            temp=None
            return 
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
            temp=None
                
    def deletionatend(self):
         if self.head!=None:
            temp=self.head
            i=0
            while(temp.next!=None):
                temp=temp.next
                i+=1
            tem=self.head

            while(i>1):
                tem=tem.next
                i-=1
            prev=tem
                
            temp=None
            prev.next=None
            return
    def traversal(self):
        if self.head!=None:
            temp=self.head
            while temp!=None:
                
                print(temp.data)
                temp=temp.next
        
q=link()
"""s1=q.insertionatbegin(7)
q.insertionatbegin(6)
q.insertionatbegin(6)
q.insertionatposition(9,1)
q.traversal()"""

q.insertionatbegin(11)
q.insertionatend(12)
q.insertionatend(8)
q.insertionatend(18)
q.insertionatend(16)
q.insertionatend(5)
q.insertionatend(18)
q.insertionatend(0)
q.deletionatposition(7)
tem=q.head
while tem!=None:
    print(tem.data,"->",end="")
    tem=tem.next
print("Null")
