class Digraph:
    def __init__(self, v: int):
        self.V: int = v
        self.E: int = 0
        self.adj: list[list[int]] = [[] for _ in range(v)]

    def addEdge(self, v: int, w: int):
        self.adj[v].append(w)
        self.E += 1

    def getAdj(self, v: int):
        return self.adj[v]

    def getV(self):
        return self.V

    def getE(self):
        return self.E

    # returns the same digraph with all the edges reversed
    def reverse(self):
        r: Digraph = Digraph(self.V)
        for v in range(self.V):
            for w in self.adj[v]:
                r.addEdge(w, v)
        return r

    def __repr__(self):
        s = ""
        for v in range(self.V):
            s += str(f"{v}: {self.adj[v]}\n")
        return s


def sample_digraph() -> Digraph:
    g = Digraph(8)

    # Adding directed edges
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
    g.addEdge(6, 7)
    g.addEdge(6, 4)

    return g
