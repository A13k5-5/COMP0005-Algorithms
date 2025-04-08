class Graph:
    def __init__(self, V: int):
        self.E: int = 0
        self.V: int = V
        self.adj = {vertex: [] for vertex in range(V)}

    def V(self) -> int:
        return self.V

    def E(self) -> int:
        return self.E

    def addEdge(self, v: int, w: int):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1

    def adj(self, v: int) -> list[int]:
        return self.adj[v]

    def __repr__(self):
        s = ""
        for node in self.adj:
            s += str(f"{node}: {self.adj[node]}\n")
        return s


if __name__ == "__main__":
    g: Graph = Graph(13)
    g.addEdge(0, 6)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 5)
    g.addEdge(5, 3)
    g.addEdge(5, 4)
    g.addEdge(3, 4)
    g.addEdge(4, 6)
    g.addEdge(7, 8)
    g.addEdge(9, 10)
    g.addEdge(9, 12)
    g.addEdge(9, 11)
    g.addEdge(11, 12)
    print(g)
