from quick_find import init


def root(i, network):
    if network[i] == i:
        return i

    return root(network[i], network)


def find(u, v, network):
    return root(u, network) == root(v, network)


def union(u, v, network):
    network[root(u, network)] = network[root(v, network)]


if __name__ == "__main__":
    network = init(10)
    union(6, 5, network)
    union(2, 1, network)
    union(7, 1, network)
    union(4, 3, network)
    union(9, 8, network)
    print(network)
