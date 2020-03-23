def permuteString(Str, size):
    ans = [""] * size
    d = dict()
    for i in range(size):
        if Str[i] in d:
            d[Str[i]] += 1
        else:
            d[Str[i]] = 1
    keys = list(d.keys())
    val = list(d.values())
    res = [""] * size
    ans = []
    permuteStringUtil(keys, val, res, 0, ans)
    return ans

def permuteStringUtil(keys, val, res, level, ans):
    
    if level == len(res):
        temp = list(res)
        ans.append("".join(temp))
        return

    for i in range(len(keys)):
        if val[i] == 0:
            continue
        res[level] =   keys[i]
        val[i] -= 1
        permuteStringUtil(keys, val, res, level + 1, ans)
        val[i] += 1

print(permuteString("ABC", len("ABC")))