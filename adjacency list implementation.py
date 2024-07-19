class graph():
    def __init__(self,Nodes):
        self.nodes=Nodes
        self.adj_list={}
        for node in self.nodes:
            self.adj_list[node]=[]
    def add_edge(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    def print_adj_list(self):
        for node in self.nodes:
            print(node,'->',self.adj_list[node])
    visited=set()
    output=[]
    def dfs(self,node):
        if node not in graph.visited:
            graph.visited.add(node)
            graph.output.append(node)
            for neighbour in self.adj_list[node]:
                self.dfs(neighbour)
        #return graph.output
        print(graph.output)
    def bfs(self):
        q=[]
        visited=[]
        output=[]
        for i in adj_list.keys():
            visited[i]=False
        s="A"
        visited[s]=True
        q.append(s)
        while q!=[]:
            u=q.pop(0)
            output.append(u)
            for i in adj_list[u]:
                if not visited[i]:
                    visited[i]=True
                    q.append(i)
        return output
                    
        
            
nodes=["A","B","C","D","E"]
graph=graph(nodes)
graph.add_edge("A","B")
graph.add_edge("C","A")
graph.add_edge("D","E")
graph.add_edge("A","C")
graph.print_adj_list()
graph.dfs("A")
