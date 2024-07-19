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


