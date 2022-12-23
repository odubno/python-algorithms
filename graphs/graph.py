"""
node (vertex): has a key and values
edges: relationship between nodes

Graphs can be expressed as adjacency matrix or adjacency lists

Using adjacency lists is more performant for algorithms.

1. Adjacency list
    An adjacency list is used to represent a finite graph. The adjacency
    list representation allows you to iterate through the neighbors of a node
    easily. Each index in the list represents the vertex and each node that is
    linked with that index represents its neighboring vertices.

1. Adjacency matrix
    An adjacency matrix is a square matrix labeled by graph vertices and is used
    to represent a finite graph. The entries of the matrix indicate whether the
    vertex pair is adjacent or not in the graph.

In the adjacency matrix representation, you will need to iterate through all
the nodes to identify a node’s neighbors.
"""

from linked_list import LinkedList


class Graph:
    """
    Graph Class ADT
    """

    def __init__(self, vertices):
        # Total number of vertices
        self.vertices = vertices
        # definining a list which can hold multiple LinkedLists
        # equal to the number of vertices in the graph
        self.array = []
        # Creating a new Linked List for each vertex/index of the list
        for i in range(vertices):
            self.array.append(LinkedList())

    def add_edge(self, source: int, destination: int):
        if (source < self.vertices and destination < self.vertices):
        # As we are implementing a directed graph, (1,0) is not equal to (0,1)
            self.array[source].insert_at_head(destination)
            # Uncomment the following line for undirected graph
            # self.array[destination].insert_at_head(source)

        # If we were to implement an Undirected Graph i.e (1,0) == (0,1)
        # We would create an edge from destination towards source as well
        # i.e self.list[destination].insertAtHead(source)=

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")


if __name__ == "__main__":

    V = 5  # Total vertices
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    g.print_graph()
