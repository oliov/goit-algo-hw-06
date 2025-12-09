import task1


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def bfs_iterative(graph, start):
    visited = set()
    queue = [start]
    #breakpoint()
    while queue:  
        vertex = queue.pop(0)
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)


print("DFS:")
dfs_recursive(task1.nx.to_dict_of_lists(task1.leaf_spine), 'leafA1')
print("")
""" dfs_tree = task1.nx.dfs_tree(task1.leaf_spine, source='leafA1')
print("Обхід графа в глибину: ", list(dfs_tree.edges())) """


print("BFS:")
bfs_iterative(task1.nx.to_dict_of_lists(task1.leaf_spine), 'leafA1')
print("")
""" bfs_tree = task1.nx.bfs_tree(task1.leaf_spine, source='leafA1')
print("Обхід графа в ширину: ", list(bfs_tree.edges())) """