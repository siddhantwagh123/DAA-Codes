from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    # Add edge to the graph
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        # Ensure both nodes are in the adjacency list
        if v not in self.adj_list:
            self.adj_list[v] = []

    # DFS function to count all paths
    def count_paths(self, u, dest, visited, count):
        visited[u] = True

        if u == dest:
            count[0] += 1
        else:
            for v in self.adj_list[u]:
                if not visited[v]:
                    self.count_paths(v, dest, visited, count)

        # Backtrack
        visited[u] = False

    def find_paths(self, start, end):
        visited = {node: False for node in self.adj_list}
        count = [0]  # Using a list to pass by reference
        self.count_paths(start, end, visited, count)
        return count[0]

if __name__ == "__main__":
    g = Graph()

    # Add edges based on the input graph
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "E")
    g.add_edge("C", "D")
    g.add_edge("C", "E")
    g.add_edge("D", "E")

    # Count paths between A and E
    print("Total paths between A and E are:", g.find_paths("A", "E"))

    # Count paths between A and C
    print("Total paths between A and C are:", g.find_paths("A", "C"))
