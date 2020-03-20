def magic_index(lis, size):
    return helper(l, 0, size-1)

def helper(l, start, end):

    if end < start:
        return -1
    midIndex = (start + end) // 2
    midValue = l[midIndex]
    if midIndex == midValue:
        return midIndex

    leftIndex = min(midIndex - 1, midValue)
    left = helper(l, start, leftIndex)
    if left >= 0:
        return left

    rightIndex = max(midIndex + 1, midValue)
    right = helper(l, rightIndex, end)
    if right < len(l):
        return right


if __name__ == '__main__':

    l = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
    size = len(l)
    print(magic_index(l, size))
