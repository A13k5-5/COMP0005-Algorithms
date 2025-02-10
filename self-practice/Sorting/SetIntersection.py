def merge(a, aux, lo, hi):
    aux = a.copy()

    mid = lo + (hi - lo) // 2
    i, j = lo, mid + 1

    for k in range(lo, hi + 1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1


def mergeSort(a, aux, lo, hi):
    if hi <= lo:
        return

    mid = lo + (hi - lo) // 2

    mergeSort(a, aux, lo, mid)
    mergeSort(a, aux, mid + 1, hi)
    if a[mid] <= a[mid + 1]:
        return
    merge(a, aux, lo, hi)


if __name__ == "__main__":
    a = [1, 4, 2, 4, 6, 123, 3, 1, 5]
    mergeSort(a, a.copy(), 0, len(a) - 1)
    print(a)
