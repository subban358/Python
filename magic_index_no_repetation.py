def magic_index(lis, size):
    return helper(l, 0, size-1)

def helper(l, start, end):

    if end < start:
        return -1
    mid = (start + end) // 2
    if l[mid] == mid:
        return mid
    elif l[mid] > mid:
        return helper(l, start, mid - 1)

    else:
        return helper(l, mid + 1, end)


if __name__ == '__main__':
    l = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
    size = len(l)
    print(magic_index(l, size))
