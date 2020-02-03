def isPossible(maze, row, col, cache, path):
    elem = str(row) + str(col)

    if row < 0 or col < 0 or maze[row][col] != 0:
        return False

    if elem in cache:
        return cache[elem]

    if row == 0 and col == 0:
        return True

    success = isPossible(maze, row - 1, col, cache, path) or isPossible(maze, row, col - 1, cache, path)
    if success:
        path.append(elem)
    cache[elem] = success

    return cache[elem]


maze = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0]
]
# maze = [
#     [0, 0, 0, 1, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0]
# ]
cache = dict()
path = []
print(isPossible(maze, len(maze) - 1, len(maze[0]) - 1, cache, path))
path.insert(0, "00")
print(path)
