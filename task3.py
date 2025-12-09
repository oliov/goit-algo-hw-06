import task1

def dijkstra(graph, start):
    #breakpoint()
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            try:
                distance = distances[current_vertex] + weight['weight']
            except KeyError:
                continue

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
        
        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    next_hops = {node: None for node in graph} # keeps nexthop for each vertex
    
     
    # rolls for each vertex and finds nexthop based on distance
    for node, distance in distances.items(): 
        for neighbor, weight in graph[node].items():
            try:
                if distances[neighbor] == distance + weight['weight']:
                    next_hops[neighbor] = node
            except KeyError:
                if distances[neighbor] == distance:
                    next_hops[neighbor] = node

    return distances, next_hops 


# prints shortest path based on dijkstra calcs
def shortest_path(graph, source, target):
   _, next_hops = dijkstra(graph, source)

   path = []
   current_node = target # starts from target and backtracks to source

   while current_node:
       path.append(current_node)
       current_node = next_hops[current_node]

   path.reverse() # backtrack needs reverse

   return path

task1.leaf_spine['leafA1']['spineA1']['weight'] = 20
task1.leaf_spine['leafA1']['spineA2']['weight'] = 10
task1.leaf_spine['leafA2']['spineA1']['weight'] = 30
task1.leaf_spine['leafA2']['spineA2']['weight'] = 20
task1.leaf_spine['leafA3']['spineA1']['weight'] = 40
task1.leaf_spine['leafA3']['spineA2']['weight'] = 30


task1.leaf_spine['leafB1']['spineB1']['weight'] = 20
task1.leaf_spine['leafB1']['spineB2']['weight'] = 10
task1.leaf_spine['leafB2']['spineB1']['weight'] = 30
task1.leaf_spine['leafB2']['spineB2']['weight'] = 30
task1.leaf_spine['leafB3']['spineB1']['weight'] = 40
task1.leaf_spine['leafB3']['spineB2']['weight'] = 30

task1.leaf_spine['spineA1']['spineB2']['weight'] = 7
task1.leaf_spine['spineA1']['spineB1']['weight'] = 14 

task1.leaf_spine['spineA2']['spineB2']['weight'] = 14
task1.leaf_spine['spineA2']['spineB1']['weight'] = 12


costs_table, _ = dijkstra(task1.nx.to_dict_of_dicts(task1.leaf_spine), 'leafA1')
print(f"Таблиця маршрутизації 'leafA1' : {costs_table}")
print(f"Traceroute from leafA1 to leafB2 is {shortest_path(task1.nx.to_dict_of_dicts(task1.leaf_spine), 'leafA1', 'leafB3')}")

"""shortest_paths = task1.nx.single_source_dijkstra_path(task1.leaf_spine, source='leafA1')
for dst, path in shortest_paths.items():
    print(f"Шлях від leafA1 до {dst}: {path}")"""