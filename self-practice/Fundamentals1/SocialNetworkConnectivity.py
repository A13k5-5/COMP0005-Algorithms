from weighted_quick_union import init, union, find, root


def load_input(filename):
    with open(filename, "r") as input:
        n = 0
        requests = []
        for i, line in enumerate(input):
            if i == 0:
                n = int(line.strip())
            if i > 1:
                requests.append([int(x) for x in line.strip().split(",")])
    return n, requests


def update_roots(network):
    for i in range(len(network)):
        network[i] = root(i, network)


def everyone_connected(network):
    return all([x == network[0] for x in network])


# Union is O(log n) operation which is done n times. update_roots is of O(log n)
# time complexity and everyone_connected is O(n). Thus this algorithm is O(n * log n).


def earliest_time_everyone_connected(n, friend_requests):
    network, size = init(n)
    for i, request in enumerate(friend_requests):
        union(request[0], request[1], network, size)
        update_roots(network)
        if everyone_connected(network):
            return i + 1
    return -1


def run():
    n, requests = load_input("socnetfile.txt")
    print(earliest_time_everyone_connected(n, requests))


if __name__ == "__main__":
    run()
