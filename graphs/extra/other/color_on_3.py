#0-green,1-blue,2-red

def color(G,v,option,visited,res = []):
    if option == 0:
        for neigh in G[v]:
            if visited[neigh] == False:
                visited[neigh] = True
                color(G,neigh,1,visited,res+[(neigh,1)])
                color(G, neigh, 2, visited, res + [(neigh, 2)])
        return res
    if option == 1:
        for neigh in G[v]:
            if visited[neigh] == False:
                visited[neigh] = True
                color(G, neigh, 0, visited, res + [(neigh, 0)])
                color(G, neigh, 2, visited, res + [(neigh, 2)])
        return res
    if option == 2:
        for neigh in G[v]:
            if visited[neigh] == False:
                visited[neigh] = True
                color(G, neigh, 0, visited, res + [(neigh, 0)])
                color(G, neigh, 1, visited, res + [(neigh, 1)])
        return res


G = [[1,3],[2,0],[3,1],[2,0]]
visited = [False]*4
print(color(G,0,0,visited))

