import networkx as nx
from collections import Counter
import matplotlib.pyplot as plt

def plot_entity_graph(entities, sentences):
    G = nx.Graph()
    all_entities = []
    for etype, words in entities.items():
        all_entities.extend(words)

    counter = Counter(all_entities)
    for word, count in counter.items():
        G.add_node(word, size=count*300)

    # Povezivanje entiteta koji se pojavljuju u istoj rečenici
    for sentence in sentences:
        words_in_sent = [w for w in all_entities if w in sentence]
        for i in range(len(words_in_sent)):
            for j in range(i+1, len(words_in_sent)):
                G.add_edge(words_in_sent[i], words_in_sent[j])

    plt.figure(figsize=(12, 10))
    sizes = [G.nodes[node]['size'] for node in G.nodes]
    nx.draw(G, with_labels=True, node_size=sizes, node_color='skyblue', edge_color='gray', font_size=10)
    plt.title("Graf povezanosti entiteta")
    plt.savefig("results/entity_graph.png")
    plt.show()
