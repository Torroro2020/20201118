graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}



def findAllPaths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newPaths = findAllPaths(graph, node, end, path)
            for newPath in newPaths:
                paths.append(newPath)
    return paths


print(findAllPaths(graph, 'A', 'D'))

