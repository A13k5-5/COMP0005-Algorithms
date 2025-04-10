from Digraph import Digraph, loadDigraph
from DepthFirstOrder import DepthFirstOrder


class KosarajuSharirSCC:
    def __init__(self, g: Digraph):
        # Get reverse post order of the reverse of graph g
        dfs: DepthFirstOrder = DepthFirstOrder(g.reverse())
        self.reversePostOrder = dfs.getReversePost()
        self.marked = [False for _ in range(g.getV())]
        self.id = [-1 for _ in range(g.getV())]
        self.count = 0
        for s in self.reversePostOrder:
            if self.marked[s]:
                continue
            self._dfs(g, s)
            self.count += 1

    def _dfs(self, g: Digraph, v: int):
        self.marked[v] = True
        self.id[v] = self.count
        for w in g.getAdj(v):
            if self.marked[w]:
                continue
            self._dfs(g, w)


if __name__ == "__main__":
    g: Digraph = loadDigraph("tinyDG.txt")
    scc: KosarajuSharirSCC = KosarajuSharirSCC(g)
    print(scc.id)
