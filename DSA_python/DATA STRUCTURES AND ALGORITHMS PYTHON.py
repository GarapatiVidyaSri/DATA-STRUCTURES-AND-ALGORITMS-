#---------------STACK IMPLEMENTATION------------------#
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
          if len(self.items)==self.size:
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




#################### POSTFIX EXPRESSION ################
print("------POSTFIX EXPRESSION------")
output=[]
operator=[]
exp=input("enter an expression")
for i in exp:
    if (i!='+' and i!='-' and i!='*' and i!='/'):
        operator.append(i)
    else:
        if len(operator)>1:
            ele1=int(operator.pop())
            ele2=int(operator.pop())
            if i=='+':
                ele3=ele2+ele1
            if i=='-':
                ele3=ele2-ele1
            if i=='*':
                ele3=ele2*ele1
            if i=='/':
                ele3=ele2/ele1
            operator.append(ele3)
print(operator)




######################QUEUE IMPLEMENTATION ####################
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
            
            
        
        
################### PRIORITY QUEUE ####################
#priority queue
print("-------------------PRIORITY QUEUE---------------")
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

################### CIRCULAR QUEUE IMPLEMENTATION #################
print("---------------------CIRCULAR QUEUE IMPLEMENTATION--------------------")
class circularqueue():
    def __init__(self,size):
        self.items=[25,30,45]
        self.size=size
        self.front=0
        self.rear=0
    def enqueue(self,item):
        if (self.front==0  and self.rear==self.size-1 or self.front==self.rear+1):
            print("overflow")
        elif (self.front==-1 and self.rear==-1):
            self.front= self.front+1
            self.rear=self.rear+1
            self.items.insert(self.rear,item)
            return self.items
        else:
            self.rear=(self.rear+1)%self.size
            self.items.insert(self.rear,item)
            return self.items
    def dequeue(self):
        if (self.front==-1 and self.rear==-1):
            print("underflow")
        elif (self.front==self.rear):
            self.items.pop(self.front)
            self.front=-1
            self.rear=-1
            return self.items
        else:
            self.items.pop(self.front)
            self.front=(self.front+1)%self.size
            return self.items
q=circularqueue(4)
print(q.items)
q.enqueue(55)
print(q.items)
q.dequeue()
print(q.items)
q.enqueue(75)
print(q.items)
q.dequeue()
print(q.items)
q.enqueue(85)
print(q.items)
q.enqueue(90)
print(q.items)
q.enqueue(100)
print(q.items)
if q.front<q.rear:
    print(q.items[q.front:])
else:
    print(q.items[0:q.rear+1]+q.items[q.front:])

                    
                    
                    
################### SINGLY LINKEDLIST #########################
    print("-------------------SINGLY LINKEDLIST-------------------")
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
###################### DOUBLY LINKEDLIST ##################
print("--------------------DOUBLY LINKEDLIST-------------------")
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
    
        
    


                
############### CIRCULAR SINGLY LINKEDLIST ##############
print("---------------CIRCULAR SINGLY LINKED LIST----------------")
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
        
################## CIRCULAR DOUBLY LINKEDLIST #######################
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
    
################ BREADTH FIRST SEARCH #####################
print("---------------------BREADTH FIRST SEARCH---------------")
from queue import Queue
adj_list={ "A":["B","C"],
           "B":["A"],
           "C":["A","D"],
           "D":["C"]}
print(adj_list)
BFS_output=[]
visited={}
queue=Queue()
for node in adj_list.keys():
    visited[node]=False
s='A'
visited[s]=True
queue.put(s)
while not queue.empty():
    u=queue.get()
    
    BFS_output.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v]=True
            queue.put(v)
print(BFS_output)


#################### DEPTH FIRST SEARCH ##############
print("-----------------------DEPTH FIRST SEARCH------------------")
graph={
    "A":["B","C"],
    "B":["A"],
    "C":["A","D"],
    "D":["C"]}
    
visited=set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
dfs(visited,graph,'A')

############# PRIM'S ALGORITHM ################            
print("---------------PRIMS ALGORITHM------------------")
INF=9999999999
n=5
adj_matrix=[[INF,2,3,INF,INF],
            [2,INF,15,2,INF],
            [3,15,INF,INF,13],
            [INF,2,INF,INF,9],
            [INF,INF,13,9,INF]]
selected={}
for node in range(n):
    print(node)
    selected[node]=False
num_edges=0
selected[0]=True
print("Edge : Weight\n")
while(num_edges<n-1):
    minimum=INF
    a=0
    b=0
    for m in range(n):
        if selected[m]:
            for p in range(n):
                if ((not selected[p])and adj_matrix[m][p]!=INF):
                    if minimum> adj_matrix[m][p]:
                        minimum= adj_matrix[m][p]
                        a=m
                        b=p
    print(str(a) +"-"+str(b) +":" +str(adj_matrix[a][b]))
    selected[b]=True
    num_edges+=1
                
##################### KRUSKAL'S ALGORITHM ##################
print("------------KRUSKAL'S ALGORITHM--------------------")
INF=9999999999
v=5
parent=[i for i in range(v)]
adj_matrix=[[INF,2,3,INF,INF],
            [2,INF,15,2,INF],
            [3,15,INF,INF,13],
            [INF,2,INF,INF,9],
            [INF,INF,13,9,INF]]
def find(i):
    while parent[i]!=i:
        i=parent[i]
    return i
def union(i,j):
    a=find(i)
    b=find(j)
    parent[a]=b
def kruskalsMST(cost):
    mincost=0
    for i in range(v):
        parent[i]=i
    edge_count=0
    while edge_count<v-1:
        min=INF
        a=-1
        b=-1
        for i in range(v):
            for j in range(v):
                if find(i)!=find(j) and cost[i][j]<min:
                    min=cost[i][j]
                    a=i
                    b=j
        union(a,b)
        print('edge{}:({},{})cost:{}' .format(edge_count,a,b,min))
        edge_count+=1
        mincost+=min
    print("minimumcost={}" .format(mincost))
kruskalsMST(adj_matrix)


################# DIJKSTRA ALGORITHM ###################
print("----------------------DIJKSTRA'S ALGORITHM-----------------------")
class Graph():
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for columns in range(vertices)]
                    for rows in range(vertices)]
    def printsolution(self,dist):
        print("vertices\tdistance")
        for node in range(self.V):
            print(node,"\t\t",dist[node])
    def minDistance(self,dist,selected):
        minii=1e7
        min_index=0
        for v in range(self.V):
            if dist[v]<minii and selected[v]==False:
                minii=dist[v]
                min_index=v
        return min_index
    def dijkstra(self,src):
        dist=[1e7]*self.V
        dist[src]=0
        print(dist)
        selected=[False]*self.V
        print(selected)
        for count in range(self.V):
            u=self.minDistance(dist,selected)
            #print(u)
            selected[u]=True
            for v in range(self.V):
                if (self.graph[u][v]>0 and selected[v]==False and dist[v]>dist[u]+self.graph[u][v]):
                    dist[v]=dist[u]+self.graph[u][v]
        self.printsolution(dist)
g=Graph(9)
g.graph=[[0,4,0,0,8,0,0,0,0],
         [4,0,8,0,11,0,0,0,0],
         [0,8,0,7,0,0,4,0,2],
         [0,0,7,0,0,0,14,9,0],
         [8,11,0,0,0,1,0,0,7],
         [0,0,0,0,1,0,2,0,6],
         [0,0,4,14,0,2,0,10,0],
         [0,0,0,9,0,0,10,0,0],
         [0,0,2,0,7,6,0,0,0]]
g.dijkstra(0)
         
    
                
################# FLOYD WARSHALL ALGORITHM #################

print("--------------------Floyd Warshall Algorithm-------------")
nv=4
inf=99999999999999
def floyd(G):
    dist=list(map(lambda p:list(map(lambda q:q,p)),G))
    print(dist)
    for r in range(nv):
        for p in range(nv):
            for q in range(nv):
                dist[p][q]=min(dist[p][q],dist[p][r]+dist[r][q])
    sol(dist)
def sol(dist):
    for p in range(nv):
        for q in range(nv):
            if (dist[p][q]==inf):
                print("inf",end="")
            else:
                print(dist[p][q],end=" ")
        print("")
G=[[0,9,-4,inf],
   [6,0,inf,2],
   [inf,5,0,inf],
   [inf,inf,1,0]]
floyd(G)
                
                
############## MERGE SORT ############
print("***********************MERGE SORT**********************")
def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        mergesort(l)
        mergesort(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<=r[j]:
                arr[k]=l[i]
                i+=1
                k+=1
            else:
                arr[k]=r[j]
                j+=1
                k+=1
        while i<len(l):
                arr[k]=l[i]
                i+=1
                k+=1
        while j<len(r):
               arr[k]=r[j]
               j+=1
               k+=1
def printlist(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()
        
arr=[1,7,6,8,9,5,2]
arr1=[56,7,99,108,4,2,1,99090,11]
mergesort(arr1)
printlist(arr1)
    
        
################### QUICK SORT #############
print("--------------------QUICK SORT-----------------")
def partition(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i+=1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[high]=array[high],array[i+1]
    return i+1
def quicksort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)
array=[10,80,9,1,87878,45,32]
quicksort(array,0,len(array)-1)
print(array)
        

################COUNTING SORT ###############
print("--------------------COUNTING SORT------------------")
def countingSort(arr):
    size = len(arr)
    output = [0] * size
    count = [0] * 10
    for m in range(0, size):
        count[arr[m]] += 1
    for m in range(1, 10):
        count[m] += count[m - 1]
        m = size - 1
    while m >= 0:
        output[count[arr[m]] - 1] = arr[m]
        count[arr[m]] -= 1
        m -= 1
    for m in range(0, size):
        arr[m] = output[m]
data = [1,4,1,2,7,5,2]
countingSort(data)
print("Sorted Array: ")
print(data)
        
#################HEAP SORT ##############
print("-------------HEAP SORT--------------")
def heapify(arr,N,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<N and arr[largest]<arr[l]:
        largest=l
    if r<N and arr[largest]<arr[r]:
        largest=r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,N,largest)
def heapsort(arr):
    N=len(arr)
    for i in range(N//2-1,-1,-1):
        heapify(arr,N,i)
    for i in range(N-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
arr=[15,5,20,1,17,10,30]
heapsort(arr)
N=len(arr)
print("Sorted array is:")
for i in range(N):
    print(arr[i],end=" ")

############ PREFIX TO POSTFIX #############
operators=["^","&","+","*","-","/"]
stack=[]
def pretopost(exp):
    exp=exp[::-1]
    for i in exp:
        if i not in operators:
            stack.append(i)
        else:
            op1=stack.pop()
            op2=stack.pop()
            d=op1+op2+i
            stack.append(d)
    return stack[0]
exp= -+ab+*c/deF
pretopost(exp)
################# INFIX TO POSTFIX############# 
 
operators=['+','-','/','*','(',')']
precidency={'+':1,'-':1,'/':2,'*':2}

def infix_to_postfix(exp):
    stack=[]
    output=""
    for i in exp:
        if i not in operators:
            output=output+i
        elif i=="(":
            stack.append("(")
        elif i==")":
            while stack!=[] and stack[-1]!='(':
                output=output+stack.pop()
            stack.pop()
        else:
            while stack!=[] and stack[-1]!='(' and precidency[i]<=precidency[stack[-1]]:
                output=output+stack.pop()
            stack.append(i)    
    while stack!=[]:
        output=output+stack.pop()

    return output
 
exp=input("enter exp")
infix_to_postfix(exp)
#################BINARY SEARCH TREE IMPLEMENTATION ###########
class Node:
    def _init_(self,data):
        self.left = None
        self.right= None
        self.data = data
        
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left= Node(data)
                else:
                    self.left.insert(data)
            if data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
            
            
    def preorder(self,root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
            
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
            
    def postorder(self,root):
        if root:
            self.preorder(root.left)
            self.preorder(root.right)
            print(root.data)
            
    def search(self,data):
        if self.data == data:
            print("key is found")
        else:
            if data < self.data:
                if self.left:
                    self.left.search(data)
                else:
                    print("not found")
            else:
                if self.right:
                    self.right.search(data)
                else:
                    print("not found")
                    
                    
    def maximum(self):
        if self.right:
            while(self.right.right!= None):
                self.right=self.right.right
            print(self.right.data)
        else:
            print(self.data)
            
            
    def minimum(self):
        if self.left:
            while(self.left.left!= None):
                self.left = self.left.left
            print(self.left.data)
        else:
            print(self.data)
            
    def deletion(self,data):
        if self.data is None:
            print("Tree is empty")
            return
        if data<self.data:
            if self.left:
                self.left=self.left.deletion(data)
            else:
                print("Given data is not present in the tree")
            return self
        elif data>self.data:
            if self.right:
                self.right=self.right.deletion(data)
            else:
                print("Given data is not present in the tree")
            return self
        else:
            if self.left is None:
                temp=self.right
                self=None
                return temp
            if self.right is None:
                temp=self.left
                self=None
                return temp
            node=self.right
            while node.left:
                node=node.left
            self.data=node.data
            self.right=self.right.deletion(node.data)
            return self
