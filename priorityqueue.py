#priority queue
class node():
    def __init__(self,data,prior):
        self.data=data
        self.prior=prior
class priorityqueue():
    def __init__(self):
        self.queue=list()
    def insert(self,data,prior):
        if self.size()==0:
            newnode=node(data,prior)
            self.queue.append(newnode)
        else:
       
            for x in range(0,self.size()):
                newnode=node(data,prior)
                if newnode.prior>self.queue[x].prior:
                    if x==(self.size())-1:
                        self.queue.insert(x+1,newnode)
                else:
                    self.queue.insert(x,newnode)
                    return True
    def size(self):
        return len(self.queue)
    def show(self):
        for i in range(0,self.size()):
            print(self.queue[i].data)
q=priorityqueue()
q.insert(6,0)
q.insert(2,1)
q.insert(7,4)
q.insert(5,9)
q.insert(4,6)
q.show()


                    
                    
                    
