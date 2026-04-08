#Write a python code to create a complete graph with vertices user defines and greater than 3
import networkx as nx
import matplotlib.pyplot as plt

n = int(input("Enter number of vertices (greater than 3): "))

if n <= 3:
    print("Number of vertices must be greater than 3.")
else:
    G = nx.complete_graph(n)
    nx.draw(G, with_labels=True)
    plt.title(f"Complete Graph with {n} vertices")
    plt.show()
