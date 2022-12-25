"""
Implement the num_edges() function which takes an undirected graph and computes
the total number of bidirectional edges. An illustration is also provided for
your understanding.
"""
from graph import Graph


def get_num_of_edges_quick(g: Graph) -> int:
    return sum([g.array[i].length() for i in range(g.vertices)])


def get_num_of_edges(g: Graph) -> int:
    """
    Time: O(V + E)
    """
    # sum up the size of all adjacency nodes in both directions
    unique_edges = 0
    for i in range(g.vertices):
        temp_node = g.array[i].get_head()
        while temp_node:
            unique_edges += 1
            temp_node = temp_node.next_element

    return unique_edges


def num_edges(g) -> int:
    """
    1. Use BFS to visit every node
        1. create a visited list
    2. increment counter of visited nodes
    """
    unique_edges = get_num_of_edges_quick(g)

    return unique_edges


def main():
    g = Graph(9)
    g.add_edge(0, 2)
    g.add_edge(0, 5)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(5, 3)
    g.add_edge(5, 6)
    g.add_edge(3, 6)
    g.add_edge(6, 7)
    g.add_edge(6, 8)
    g.add_edge(6, 4)
    g.add_edge(7, 8)

    assert num_edges(g) == 11


main()
