class node():
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.prev=None
        self.next=None
class link():
    def __init__(self):
        self.head=None
    def insertion(self,data,position):
        if position==0:
            if self.head==None:
                newnode=node(data)
                newnode.next=None
                self.head=newnode
            else:
                newnode=node(data)
                newnode.next=self.head
                self.head=newnode
                
        else:
            temp=self.head
            i=0
            while i!=position-1:
                temp=temp.next
                i+=1
            if temp.next!=None:
                newnode=node(data)
                
                newnode.next=temp.next
                temp.next=newnode
                
            else:
                newnode=node(data)
                
                newnode.next=None
                temp.next=newnode
    def deletion(self,position):
         if self.head==None:
             print("empty")
         if position==0 and self.head!=None:
                 temp=self.head
                 self.head=temp.next
                 temp=None
         if position!=0: 
             if self.head!=None:
                 i=0
                 temp=self.head
                 while i!=position:
                     temp=temp.next
                     i+=1
                 tem=self.head
                 while(i>1):
                     tem=tem.next
                     i-=1
                     
                 prev=tem
                 if temp.next==None:
                    temp=None
                    prev.next=None
                 else:
                     prev.next=temp.next
                     temp=None
                     
                     
                    
                    
q=link()
q.insertion(2,0)
q.insertion(9,0)
q.insertion(4,1)
q.insertion(5,0)
q.insertion(9,3)
q.deletion(0)
q.deletion(2)
q.deletion(1)
q.deletion(0)
q.deletion(0)
q.deletion(0)
tem=q.head
while tem!=None:
    print(tem.data)
    tem=tem.next
