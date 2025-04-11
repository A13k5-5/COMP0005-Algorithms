from DirectedEdge import DirectedEdge


class EdgeWeightedDigraph:
    def __init__(self, V: int):
        self.adj: list[list[DirectedEdge]] = [[] for _ in range(V)]
        self.V: int = V
        self.E: int = 0
        self.edges: list[DirectedEdge] = []

    def addEdge(self, s: int, d: int, w: float):
        e: DirectedEdge = DirectedEdge(s, d, w)
        self.adj[s].append(e)
        self.edges.append(e)
        self.E += 1

    def getAdj(self, v: int) -> list[DirectedEdge]:
        return self.adj[v]

    def getV(self) -> int:
        return self.V

    def getE(self) -> int:
        return self.E

    def getEdges(self) -> list[DirectedEdge]:
        return self.edges

    def __repr__(self):
        s = ""
        for i in range(self.V):
            s += f"{i}: {self.getAdj(i)}\n"
        return s


def loadEWD(filename: str) -> EdgeWeightedDigraph:
    with open(filename, "r") as file:
        lines = [line.strip() for line in file]
    V: int = int(lines[0])
    E: int = int(lines[1])
    g: EdgeWeightedDigraph = EdgeWeightedDigraph(V)
    for i in range(2, len(lines)):
        line = lines[i].split()
        s, d, w = int(line[0]), int(line[1]), float(line[2])
        g.addEdge(s, d, w)
    return g


if __name__ == "__main__":
    g: EdgeWeightedDigraph = loadEWD("tinyEWD.txt")
    print(g)
