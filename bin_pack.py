def numOfRods(rods: [list], big_rod: int, size) -> int:
    res = 0
    rods.sort(reverse=True)
    size_remaining = [None] * size
    j = 0
    for i in range(0, size):
        for j in range(0, res):
            if size_remaining[j] >= rods[i]:
                size_remaining[j] -= rods[i]
                break
        if j == res:
            size_remaining[res] = big_rod - rods[i]
            res += 1
    return res


if __name__ == '__main__':
    list_rods = [37, 34, 38, 38, 44, 37, 42, 42, 78, 41, 68, 42, 78, 45, 42, 42, 43, 36, 41, 38]
    big_rod_size = 144
    size = len(list_rods)

    print(numOfRods(list_rods, big_rod_size, size))
