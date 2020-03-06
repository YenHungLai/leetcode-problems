haystack = "a"
needle = "a"


def strStr(haystack, needle):
    """Have two pointers that are len(needle) apart."""
    if needle == '':
        return 0
    elif haystack == '':
        return -1

    head = 0
    tail = len(needle) - 1

    while tail <= len(haystack) - 1:
        if haystack[head:tail+1] == needle:
            return head
        else:
            head += 1
            tail += 1

    return -1


print(strStr(haystack, needle))
