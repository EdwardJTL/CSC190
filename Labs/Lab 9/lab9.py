def quicksort(u, ini, fin):
    if ini < fin:
        pIndex = partition(u, ini, fin)
        quicksort(u, ini, pIndex-1)
        quicksort(u, pIndex+1, fin)
    return True


def partition(u, ini, fin):
    p = fin
    pIndex = ini-1
    for i in range(ini, fin, 1):
        if u[i] < u[p]:
            pIndex += 1
            helper_swap(u, i, pIndex)
    pIndex += 1
    helper_swap(u, p, pIndex)
    return pIndex


def helper_swap(u, a, b):
    if a >= len(u) or b >= len(u):
        return False
    else:
        temp = u[a]
        u[a] = u[b]
        u[b] = temp
        return True


def hanoi(n, start, tmp, final):
    if n > 0:
        hanoi(n-1, start, final, tmp)
        final.append(start.pop())
        hanoi(n-1, tmp, start, final)
        print start, tmp, final
        return True
    else:
        return True
