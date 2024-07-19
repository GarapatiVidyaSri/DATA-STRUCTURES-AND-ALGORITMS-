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
                
