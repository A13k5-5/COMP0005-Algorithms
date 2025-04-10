from collections import deque


class Graph:
    def __init__(self, V: int):
        self.E: int = 0
        self.V: int = V
        self.adj = {vertex: [] for vertex in range(V)}

    def getV(self) -> int:
        return self.V

    def getE(self) -> int:
        return self.E

    def addEdge(self, v: int, w: int):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1

    def getAdj(self, v: int) -> list[int]:
        return self.adj[v]

    def __repr__(self):
        s = ""
        for node in self.adj:
            s += str(f"{node}: {self.adj[node]}\n")
        return s


class DepthFirstSearch:
    def __init__(self, g: Graph, s: int):
        self.edgeTo = [None for _ in range(g.getV())]
        self.marked = [False for _ in range(g.getV())]
        self.s = s
        self.dfs(g, s)

    def dfs(self, g: Graph, v: int):
        self.marked[v] = True
        for w in g.getAdj(v):
            if self.marked[w]:
                continue
            self.edgeTo[w] = v
            self.dfs(g, w)

    def hasPathTo(self, v: int):
        return self.marked[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        path = []
        x = v
        while x != self.s:
            path.append(x)
            x = self.edgeTo[x]
        path.append(self.s)
        return path


class BreadthFirstSearch:
    def __init__(self, g: Graph, s: int):
        self.marked = [False for _ in range(g.getV())]
        self.edgeTo = [None for _ in range(g.getV())]
        self.distToSource = [None for _ in range(g.getV())]
        self.s = s
        self.bfs(g, s)

    def bfs(self, g: Graph, s: int):
        q = deque()
        q.append(s)
        self.distToSource[s] = 0
        while len(q) > 0:
            v = q.popleft()
            for w in g.getAdj(v):
                if self.distToSource[w] is not None:
                    continue
                q.append(w)
                self.distToSource[w] = self.distToSource[v] + 1
                self.edgeTo[w] = v

    def hasPathTo(self, v: int):
        return self.marked[v]

    def pathTo(self, v: int):
        if not self.hasPathTo(v):
            return None
        x = v
        path = []
        while x != self.s:
            path.append(x)
            x = self.edgeTo[x]
        path.append(x)
        return path


class CC:
    def __init__(self, g: Graph):
        self.marked = [False for _ in range(g.getV())]
        self.id = [-1 for _ in range(g.getV())]
        self.count = 0
        for s in range(g.getV()):
            if self.marked[s]:
                continue
            self._dfs(g, s)
            self.count += 1

    def _dfs(self, g: Graph, v: int):
        self.marked[v] = True
        self.id[v] = self.count
        for w in g.getAdj(v):
            if self.marked[w]:
                continue
            self._dfs(g, w)

    def connected(self, v: int, w: int) -> bool:
        return self.id[v] == self.id[w]

    def getCount(self) -> int:
        return self.count

    def getId(self, v: int) -> int:
        return self.id[v]


class Cycle:
    def __init__(self, g: Graph):
        self.marked = [False for _ in range(g.getV())]
        self.hasCycle = False
        for s in range(g.getV()):
            if not self.marked[s]:
                self._dfs(g, -1, s)

    # u is the vertex we came from, v is the current vertex
    def _dfs(self, g: Graph, u: int, v: int):
        self.marked[v] = True
        for w in g.getAdj(v):
            if not self.marked[w]:
                self._dfs(g, v, w)
            # if neighbour is marked and is not the vertex we came from, then there is a different way to get there - there exists a cycle
            elif w != u:
                self.hasCycle = True


class Bipartite:
    def __init__(self, g: Graph):
        self.marked = [False for _ in range(g.getV())]
        # True - red, False - black
        self.colour = [False for _ in range(g.getV())]
        self.isBipartite = True
        for s in range(g.getV()):
            if not self.marked[s]:
                self._dfs(g, s)

    def _dfs(self, g: Graph, v: int):
        self.marked[v] = True
        for w in g.getAdj(v):
            if not self.marked[w]:
                self.colour[w] = not self.colour[v]
                self._dfs(g, w)
            elif self.colour[v] == self.colour[w]:
                self.isBipartite = False


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

    g2: Graph = Graph(4)
    g2.addEdge(0, 1)
    g2.addEdge(1, 2)
    g2.addEdge(2, 3)
    # print(g)
    # d: DepthFirstSearch = DepthFirstSearch(g, 0)
    # print(d.pathTo(5))
    # print(d.marked)
    # b: BreadthFirstSearch = BreadthFirstSearch(g, 0)
    # print(b.pathTo(3))
    # print(b.distToSource)
    connectedComponents: CC = CC(g)
    # print(connectedComponents.id)
    cycle: Cycle = Cycle(g)
    # print(cycle.hasCycle)
    bipartite: Bipartite = Bipartite(g)
    print(bipartite.isBipartite)
