print("--------STACK IMPLEMENTATION--------")
class stack():
    def __init__(self,size):
        self.items=[]
        self.size=size
    def pop(self):
        if len(self.items)!=0:
             return self.items.pop()
        else:
            print("underflow")
    def push(self,item):
        if len(self.items)!= self.size:
            return self.items.append(item)
        else:
            print("overflow")
    def isfull(self):
          if len(self.items)!=self.size:
              return isfull
    def isempty(self):
        if len(self.items)==0:
            print("is empty")
    def peek(self):
        if len(self.items)!=0:
            return self.items[-1]

s=stack(5)
p=int(input("enter a number for operation"))
q=int(input("enter num for operation to be done"))
if p==1:
      print("pop")
      s.pop()
if p==2:
      print("push")
      s.push(q)
if p==3:
      print("isfull")
      s.isfull()
if p==4:
      print("isempty")
      s.isempty()
print(s.items)
    
            
            
        
        
