from EdgeWeightedGraph import EdgeWeightedGraph
from Edge import Edge
import heapq


class KruskalMST:
    def __init__(self, g: EdgeWeightedGraph):
        self.mst = []
        pq = []
        for e in g.getEdges():
            heapq.heappush(pq, e)
