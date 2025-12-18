import networkx as nx
import matplotlib.pyplot as plt

def handshake_count(n):
    return n * (n - 1) // 2

def draw_handshake_graph(n):
    G = nx.complete_graph(n)
    labels = {i: chr(65 + i) for i in range(n)}
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=False, node_size=1000)
    nx.draw_networkx_labels(G, pos, labels, font_color='white')
    plt.title(f"Handshake Graph for {n} Guests")
    plt.show()

guests = int(input("Enter number of guests: "))
print(f"Handshakes = {handshake_count(guests)}")

draw_handshake_graph(guests)
