import task1

task1.leaf_spine['leafA1']['spineA1']['weight'] = 20
task1.leaf_spine['leafA1']['spineA2']['weight'] = 10
task1.leaf_spine['leafA2']['spineA1']['weight'] = 30
task1.leaf_spine['leafA2']['spineA1']['weight'] = 30
task1.leaf_spine['leafA3']['spineA1']['weight'] = 40
task1.leaf_spine['leafA3']['spineA2']['weight'] = 30


task1.leaf_spine['leafB1']['spineB1']['weight'] = 20
task1.leaf_spine['leafB1']['spineB2']['weight'] = 10
task1.leaf_spine['leafB2']['spineB1']['weight'] = 30
task1.leaf_spine['leafB2']['spineB1']['weight'] = 30
task1.leaf_spine['leafB3']['spineB1']['weight'] = 40
task1.leaf_spine['leafB3']['spineB2']['weight'] = 30

task1.leaf_spine['spineA1']['spineB2']['weight'] = 7
task1.leaf_spine['spineA1']['spineB1']['weight'] = 14 

task1.leaf_spine['spineA2']['spineB2']['weight'] = 14
task1.leaf_spine['spineA2']['spineB1']['weight'] = 12


shortest_paths = task1.nx.single_source_dijkstra_path(task1.leaf_spine, source='leafA1')
for dst, path in shortest_paths.items():
    print(f"Шлях від leafA1 до {dst}: {path}")