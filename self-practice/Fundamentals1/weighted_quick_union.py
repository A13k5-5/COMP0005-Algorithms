from quick_union import root, union as basic_union, find


def init(n):
    return [i for i in range(n)], [1 for i in range(n)]


def union(u, v, network, size):
    r_u = root(u, network)
    r_v = root(v, network)
    if size[r_u] < size[r_v]:
        network[r_u] = r_v
        size[r_v] += size[r_u]
    else:
        network[r_v] = r_u
        size[r_u] += size[r_v]


if __name__ == "__main__":
    network, size = init(10)
    nums, _ = init(10)
    union(2, 1, network, size)
    union(0, 3, network, size)
    union(1, 0, network, size)
    # union(4, 3, network, size)
    # union(6, 5, network, size)
    # union(5, 0, network, size)
    # union(0, 1, network, size)
    # union(2, 1, network, size)
    # union(7, 1, network, size)
    # union(9, 8, network, size)
    print(network)
    print(size)
