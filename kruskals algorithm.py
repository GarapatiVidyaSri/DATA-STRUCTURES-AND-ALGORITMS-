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
