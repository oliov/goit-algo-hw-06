import task1


dfs_tree = task1.nx.dfs_tree(task1.leaf_spine, source='leafA1')
print("Обхід графа в глибину: ", list(dfs_tree.edges()))

bfs_tree = task1.nx.bfs_tree(task1.leaf_spine, source='leafA1')
print("Обхід графа в ширину: ", list(bfs_tree.edges()))