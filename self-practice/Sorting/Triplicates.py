def triplicates1(a, b, c):
    d = a + b + c
    d.sort()
    counter = 1
    cur = ""
    for s in d:
        if s == cur:
            counter += 1
        else:
            counter = 1
            cur = s
        if counter == 3:
            return s
    return None


def triplicates2(a, b, c):
    freq = {}
    for w in a + b + c:
        if w not in freq.keys():
            freq[w] = 1
        else:
            freq[w] += 1
    for key in freq.keys():
        if freq[key] == 3:
            return key
    return None


if __name__ == "__main__":
    sentences = []
    a = ["hello", "there", "how", "are", "you"]
    b = ["hello", "Im", "fine", "thank", "you"]
    c = ["helo", "Yeah", "Im", "all", "right", "and", "you"]
    print(triplicates1(a, b, c))
    print(triplicates2(a, b, c))
