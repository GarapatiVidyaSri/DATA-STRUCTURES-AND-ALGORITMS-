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
            #print("hi")
            if dist[v]<minii and selected[v]==False:
                minii=dist[v]
                #print(minii)
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
         
    
                
                
    
            
    
