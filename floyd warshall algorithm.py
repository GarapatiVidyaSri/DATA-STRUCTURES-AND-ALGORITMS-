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
                
                
