class DirectedEdge:
    def __init__(self, s: int, e: int, w: float):
        self.source = s
        self.destination = e
        self.weight = w

    def getWeight(self) -> float:
        return self.weight

    def getSource(self) -> int:
        return self.source

    def getDestination(self) -> int:
        return self.destination

    def __repr__(self):
        return f"{self.source, self.destination, self.weight}"


if __name__ == "__main__":
    e: DirectedEdge = DirectedEdge(0, 1, 4.2)
    print(e)
