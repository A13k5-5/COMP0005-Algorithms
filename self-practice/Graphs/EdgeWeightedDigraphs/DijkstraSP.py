from DirectedEdge import DirectedEdge
from EdgeWeightedDigraph import EdgeWeightedDigraph


class DijkstraSP:
    def __int__(self, g: EdgeWeightedDigraph, s: int):
        self.distTo: list[float] = [float("int") for _ in range(g.getV())]
        self.edgeTo = [None for _ in range(g.getV())]
        self.pq: list[DirectedEdge] = []

    def relax(self):
        pass
