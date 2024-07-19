class node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doublylinked():
    def __init__(self):
        self.head=None
        self.tail=None
    def insertion(self,data,position):
        if  position==0 and self.head==None:
            newnode=node(data)
            self.head=newnode
            self.head.next=None
        if position==0 and self.head!=None :
            newnode=node(data)
            self.head.prev=newnode
            newnode.next=self.head
            self.head=newnode
            newnode.prev=None
        elif self.head!=None and position!=0:
            temp=self.head
            i=0
            while temp!=position:
                temp=temp.next
                i+=1
            if temp.next==None:
                newnode=node(data)
                newnode.prev=temp
                temp.next=newnode
                newnode.next=None
            elif temp.next!=None:
                newnode=node(data)
                newnode.prev=temp
                newnode.next=temp.next
                temp.next.prev=newnode
                temp.next=newnode

                
            
           

d=doublylinked()
d.insertion(4,0)
d.insertion(2,0)
d.insertion(1,0)
d.insertion(3,1)
tem=d.head
while tem!=None:
    print(tem.data)
    tem=tem.next
print("null")
