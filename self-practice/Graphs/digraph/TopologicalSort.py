from digraph import Digraph, sample_digraph
from DirectedCycle import DirectedCycle


class TopologicalSort:
    def __init__(self, g: Digraph):
        self.marked = [False for _ in range(g.getV())]
        self.stack = []
        directedCycle: DirectedCycle = DirectedCycle(g)
        hasCycle = directedCycle.hasCycle()
        if hasCycle:
            return
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
    # Read data from tinyDAG.txt
    with open("tinyDAG.txt", "r") as file:
        lines = [line.strip() for line in file if line.strip()]

    num_vertices = int(lines[0])
    g = Digraph(num_vertices)

    for i in range(1, len(lines)):
        v, w = map(int, lines[i].split())
        g.addEdge(v, w)

    # Run topological sort
    topSort = TopologicalSort(g)
    print(f"Topological order: {topSort.stack}")
