s = ["H", "a", "n", "n", "a", "h"]


def reverseString(s):
    head, tail = 0, len(s) - 1
    while head < tail:
        head_val = s[head]
        tail_val = s[tail]
        s[head] = tail_val
        s[tail] = head_val
        head += 1
        tail -= 1


reverseString(s)
print(s)
