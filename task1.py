import networkx as nx
import matplotlib.pyplot as plt

leaf_spine = nx.Graph()

leaf_spine.add_nodes_from(['spineA1', 'spineA2'])
leaf_spine.add_nodes_from([
    'leafA1', 'leafA2', 'leafA3'
])

leaf_spine.add_edges_from([
    ('leafA1', 'spineA1'),
    ('leafA1', 'spineA2'),
    ('leafA2', 'spineA1'),
    ('leafA2', 'spineA2'),
    ('leafA3', 'spineA1'),
    ('leafA3', 'spineA2'),
])


leaf_spine.add_nodes_from(['spineB1', 'spineB2'])
leaf_spine.add_nodes_from([
    'leafB1', 'leafB2', 'leafB3'
])


leaf_spine.add_edges_from([
    ('leafB1', 'spineB1'),
    ('leafB1', 'spineB2'),
    ('leafB2', 'spineB1'),
    ('leafB2', 'spineB2'),
    ('leafB3', 'spineB1'),
    ('leafB3', 'spineB2'),
])

leaf_spine.add_edges_from([
    ('spineA1', 'spineB1'),
    ('spineA1', 'spineB2'),
    ('spineA2', 'spineB1'),
    ('spineA2', 'spineB2'),
])

pos = nx.spring_layout(leaf_spine,scale=2)

nx.draw(leaf_spine, with_labels=True, pos=pos)
plt.show()

print('Кількість вершин: ', leaf_spine.number_of_nodes())
print('Кількість ребер: ', leaf_spine.number_of_edges())
for record in leaf_spine.degree:
    node, degree = record
    print(f"Вершина {node} має ступінь {degree}")