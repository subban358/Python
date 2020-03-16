def num_to_str(num):
    s = str(num)
    n = len(s)
    m = n // 2
    if n % 2 == 0:
        return s[:m], '', s[m:]
    else:
        return s[:m], s[m], s[m + 1:]

def next_palindrome(num):
    if num < 9:
        return num + 1
    if num < 11:
        return 11
    left, mid, right = num_to_str(num)
    len_num = len(str(num))

    if num == 10 ** len_num - 1:
        return num + 2

    elif mid == '':
        if not int(left[::-1]) > int(right):
            left = str(int(left) + 1)
        right = left[::-1]

    else:
        if not int(left[::-1]) > int(right):
            left_mid = str(int(left + mid) + 1)
            left, mid = left_mid[: -1], left_mid[-1]

        right = left[::-1]

    return int(left + mid + right)


print(next_palindrome(1000))
print(next_palindrome(999))
print(next_palindrome(11))
print(next_palindrome(2002))
print(next_palindrome(121))
print(next_palindrome(13206))
