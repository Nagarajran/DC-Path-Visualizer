import networkx as nx
import mplcursors
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

G = nx.DiGraph()

G.add_node("O")
G.add_node("UCS-FI-A", color="red")

G.add_edge('VM', 'ESX', weight=1)
G.add_edge('ESX', 'UCS-FI-B', weight=1)
G.add_edge('ESX', 'UCS-FI-A', weight=1, label="ABC")
G.add_edge('UCS-FI-A','leaf1', weight=1, color="red", label="ABC")
G.add_edge('UCS-FI-A','leaf2', weight=1, color="red", label="ABC")
G.add_edge('UCS-FI-B', 'leaf2', weight=1, label="ABC")
G.add_edge('UCS-FI-B', 'leaf1', weight=1, label="ABC")
G.add_edge('leaf1', 'spine1', weight=2, label="ABC")
G.add_edge('leaf1', 'spine2', weight=2, label="ABC")
G.add_edge('leaf1', 'spine3', weight=2, label="ABC")
G.add_edge('leaf1', 'spine4', weight=2, label="ABC")
G.add_edge('leaf2', 'spine1', weight=2, label="ABC")
G.add_edge('leaf2', 'spine2', weight=2, label="ABC")
G.add_edge('leaf2', 'spine3', weight=2, label="ABC")
G.add_edge('leaf2', 'spine4', weight=2, label="ABC")

G.add_edge('leaf3', 'spine1', weight=2, label="ABC")
G.add_edge('leaf3', 'spine2', weight=2, label="ABC")
G.add_edge('leaf3', 'spine3', weight=2, label="ABC")
G.add_edge('leaf3', 'spine4', weight=2, label="ABC")
G.add_edge('leaf4', 'spine1', weight=2, label="ABC")
G.add_edge('leaf4', 'spine2', weight=2, label="ABC")
G.add_edge('leaf4', 'spine3', weight=2, label="ABC")
G.add_edge('leaf4', 'spine4', weight=2, label="ABC")


G.add_edge('Cluster_Node1', 'leaf3', label="ABC")
G.add_edge('Cluster_Node1', 'leaf4', label="ABC")   
G.add_edge('VFiler1', 'Cluster_Node1', label="ABC")


figure(figsize=(8, 6), dpi=120)



node_size = 20
font_size = 8
linewidths = 0.5
arrowstyle = '-'
arrow_size = 10
default_edge_color = 'blue'
edge_colors = [G[u][v].get('color', default_edge_color) for u,v in G.edges()]

default_node_color = 'green'
color_map = [G.nodes[u].get('color', default_node_color) for u in G.nodes()]

node_pos = {'O':(-2,0),'VM':(5,1),'ESX':(5,2),'UCS-FI-A':(2,3),'UCS-FI-B':(8,3),'leaf1':(2,4),
            'leaf2':(8,4),'spine1':(5,5),'spine2':(9,5),
            'spine3':(13,5),'spine4':(17,5),'leaf3':(14,4),
            'leaf4':(20,4),'Cluster_Node1':(17,3),'VFiler1':(17,2)}


nx.draw_networkx(G, node_pos, node_color=color_map, edge_color=edge_colors,
                 node_size=node_size,  linewidths=linewidths,
                 arrowstyle=arrowstyle, arrowsize=arrow_size, with_labels=False)



nx.draw_networkx_labels(G, node_pos, font_size=font_size,
                            verticalalignment="bottom",horizontalalignment="right")



# uncomment following two lines to see edge labels
#edge_labels = nx.get_edge_attributes(G, "label")
#nx.draw_networkx_edge_labels(G, node_pos, edge_labels)

cursor = mplcursors.cursor(hover=True)

plt.show() 