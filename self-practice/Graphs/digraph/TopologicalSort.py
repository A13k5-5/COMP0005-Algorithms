from digraph import Digraph, sample_digraph
from DirectedCycle import DirectedCycle


class TopologicalSort:
    def __init__(self, g: Digraph):
        directedCycle: DirectedCycle = DirectedCycle(g)
        hasCycle = directedCycle.hasCycle()
        if hasCycle:
            return
        self.marked = [False for _ in range(g.getV())]
        self.stack = []
        for s in range(g.getV()):
            if not self.marked[s]:
                self._dfs(g, s)
        self.stack.reverse()

    def _dfs(self, g: Digraph, v: int):
        self.marked[v] = True
        for w in g.getAdj(v):
            if self.marked[w]:
                continue
            self._dfs(g, w)
        self.stack.append(v)


if __name__ == "__main__":
    g: Digraph = sample_digraph()
    topSort: TopologicalSort = TopologicalSort(g)
    print(topSort.stack)
