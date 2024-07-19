class node():
    def __init__(self,data):
        self.data=data
        self.head=None
        self.next=None
class circularsinglylinkedlist():
    def __init__(self):
        self.tail=None
    def insertionatbegin(self,data):
        if self.tail==None:
            newnode=node(data)
            self.tail=newnode
            newnode.next=self.tail
            return self.tail.data
        else:
            newnode=node(data)
            newnode.next=self.tail.next
            self.tail.next=newnode
            return self.tail.data
    def insertionatend(self,data):
        if self.tail==None:
            newnode=node(data)
            self.tail=newnode
            newnode.next=self.tail
            return self.tail.data
        else:
            newnode=node(data)
            
            newnode.next=self.tail.next
            self.tail.next=newnode
            self.tail=newnode
            return self.tail.data
    def insertionafteritem(self,data,item):
        if self.tail==None:
            return
        temp=self.tail
        while temp.data!=None:
            if temp.data==item:
                newnode=node(data)
                newnode.next=temp.next
                temp.next=newnode
                break
            temp=temp.next
        return self.tail
            
            
                            
    def traversal(self):
        if self.tail==None:
            print("list is empty")
        else:
            temp=self.tail.next
            while temp:
                print(temp.data)
                temp=temp.next
                if temp==self.tail.next:
                    break

    def deletionatbegin(self):
        if self.tail==self.tail.next:
            self.tail.next=None
            self.tail=None
        else:
            temp=self.tail.next
            #print(temp.data)
            #print(temp.next.data)
            self.tail.next=temp.next
            #print("hii")
            temp=None
            return self.tail.data
    def deletionatend(self):
        if self.tail!=None:
            temp=self.tail.next
            while temp.next!=self.tail:
                temp=temp.next
            temp.next=self.tail.next
            temp=None
    def deletionatposition(self,position):
        if self.tail!=None:
            temp=self.tail.next
            i=0
            while i<position:
                temp=temp.next
                i+=1
            tem=self.tail.next
            while i>1:
                tem=tem.next
            prev=tem
            prev.next=temp.next
            temp=None
            
            
            
       
q=circularsinglylinkedlist()
q.insertionatbegin(7)
q.insertionatbegin(8)
q.insertionatbegin(9)
q.insertionatend(6)
q.deletionatbegin()
q.deletionatbegin()
q.insertionatend(1)
q.insertionatend(2)
q.deletionatend()
q.deletionatposition(1)
#q.traversal()
#q.insertionafteritem(1,9)
temp=q.tail.next
while temp:
    print(temp.data)
    temp=temp.next
    if temp==q.tail.next:
        break
        
