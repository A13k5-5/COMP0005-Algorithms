from Digraph import Digraph, sample_digraph
from DirectedCycle import DirectedCycle
from DepthFirstOrder import DepthFirstOrder


class TopologicalSort:
    def __init__(self, g: Digraph):
        directedCycle: DirectedCycle = DirectedCycle(g)
        hasCycle = directedCycle.hasCycle()
        if hasCycle:
            return
        dfs: DepthFirstOrder = DepthFirstOrder(g)
        self.reversePostOrder = dfs.getReversePost()

    def getTopologicalSort(self):
        return self.reversePostOrder


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
    print(f"Topological order: {topSort.reversePostOrder}")
