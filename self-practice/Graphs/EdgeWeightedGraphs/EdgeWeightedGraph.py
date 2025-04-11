from Edge import Edge


class EdgeWeightedGraph:
    def __init__(self, V: int):
        self.adj: list[list[Edge]] = [[] for _ in range(V)]
        self.V = V
        self.E = 0
        self.edges: list[Edge] = []

    def addEdge(self, e: Edge):
        v = e.either()
        w = e.other(v)
        self.adj[v].append(e)
        self.adj[w].append(e)
        self.E += 1
        self.edges.append(e)

    def getAdj(self, v: int) -> list[Edge]:
        return self.adj[v]

    def getV(self):
        return self.V

    def getEdges(self):
        return self.edges

    def __repr__(self):
        s = ""
        for i in range(self.getV()):
            s += f"{i}: {str(self.getAdj(i))}\n"
        return s


def loadEWG(filename: str) -> EdgeWeightedGraph:
    with open(filename, "r") as file:
        lines = [line.strip() for line in file]
    V: int = int(lines[0])
    E: int = int(lines[1])
    g: EdgeWeightedGraph = EdgeWeightedGraph(V)
    for i in range(2, len(lines)):
        parts = lines[i].split()
        v, w, weight = int(parts[0]), int(parts[1]), float(parts[2])
        g.addEdge(Edge(v, w, weight))
    return g


if __name__ == "__main__":
    # g: EdgeWeightedGraph = EdgeWeightedGraph(5)
    g: EdgeWeightedGraph = loadEWG("tinyEWG.txt")
    print(g)
