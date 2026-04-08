import matplotlib.pyplot as plt
import networkx as nx
def create_complete_graph():
    n=int(input("Enter number of vertices :"))
    if n<=3:
        print("Number of vertices must be greater than 3: ")
        return
    Graph= nx.complete_graph(n)
    pos=nx.circular_layout(Graph)
    nx.draw(Graph,pos,with_labels= True, node_color="Blue")
    plt.title("Graph Representation")
    plt.show()

create_complete_graph()

