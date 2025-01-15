opposite = {")": "(", "]": "["}


def balanced_brackets(str):
    stack = []
    for br in str:
        if br in ["(", "["]:
            stack.append(br)
        elif br in [")", "]"]:
            if len(stack) == 0 or stack.pop() != opposite[br]:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    print(balanced_brackets("(x) + (x - 2) - a[3] / [a10]"))
