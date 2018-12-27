def selection_sort(u):
    length = len(u)
    while length != 0:
        max_element = u[0]
        max_index = 0
        for i in range(0, length, 1):
            if u[i] > max_element:
                max_element = u[i]
                max_index = i
        length -= 1
        helper_swap(u, length, max_index)
    return True


def heapify(u):
    for i in range(0, len(u), 1):
        parent = int((i-1)/2)
        if parent < 0:
            parent = 0
        index = i
        while u[index] > u[parent]:
            helper_swap(u, index, parent)
            index = parent
            parent = int((index-1)/2)
            if parent < 0:
                parent = 0
    return True


def reheapify(u, end):
    moving = True
    index = 0
    while moving:
        moving = False
        lc = index * 2 + 1
        rc = index * 2 + 2
        if lc <= end:
            swap_child = lc
            if rc <= end:
                if u[rc] > u[lc]:
                    swap_child = rc
            if u[swap_child] > u[index]:
                helper_swap(u, swap_child, index)
                index = swap_child
                moving = True
    return True


def heap_sort(u):
    heapify(u)
    end = len(u) - 1
    while end != 0:
        helper_swap(u, end, 0)
        end -= 1
        reheapify(u, end)
    return True


def merge_sort(u):
    helper_merge_sort(u, 0, len(u))
    return True


def quick_sort(u, ini, fin):
    if ini < fin:
        pIndex = partition(u, ini, fin)
        quick_sort(u, ini, pIndex-1)
        quick_sort(u, pIndex+1, fin)
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


def helper_max(a, b):
    if a > b:
        return a
    else:
        return b


def helper_swap(u, a, b):
    if a >= len(u) or b >= len(u):
        return False
    else:
        temp = u[a]
        u[a] = u[b]
        u[b] = temp
        return True


def helper_merge_sort(u, start, end):
    if start < end and end - start != 1:
        middle = int((start + end)/2)
        helper_merge_sort(u, start, middle)
        helper_merge_sort(u, middle, end)
        helper_merge(u, start, middle+1, end)
    return True


def helper_merge(u, start, middle, end):
    queue1 = []
    queue2 = []
    for i in range(start, middle-1, 1):
        queue1.append(u[i])
    for i in range(middle-1, end, 1):
        queue2.append(u[i])
    i = start
    while (len(queue1) != 0) and (len(queue2) != 0):
        if queue1[0] <= queue2[0]:
            u[i] = queue1[0]
            queue1 = queue1[1:]
        else:
            u[i] = queue2[0]
            queue2 = queue2[1:]
        i += 1
    while not len(queue1) == 0:
        u[i] = queue1[0]
        queue1 = queue1[1:]
        i += 1
    while not len(queue2) == 0:
        u[i] = queue2[0]
        queue2 = queue2[1:]
        i += 1
    return True