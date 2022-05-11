graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['9'],
    '8' : [],
    '9' : []
    }
visited =set()

def dfs(visited, graph, node):
    if node  not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
print("Following is the depth-First Search")
dfs(visited,graph,'3')
    
