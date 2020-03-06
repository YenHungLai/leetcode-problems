a = "1010"
b = "1011"


# def addBinary(a, b):
#     """Brute force"""
#     max_digit = max(len(a), len(b))
#     a, b = a.zfill(max_digit), b.zfill(max_digit)
#     carry = False
#     result = []

#     print(a, b)

#     for idx in range(max_digit - 1, -1, -1):
#         if a[idx] == '1' and b[idx] == '1':
#             if carry:
#                 result.insert(0, '1')
#             else:
#                 result.insert(0, '0')
#                 carry = True
#         elif a[idx] == '1' or b[idx] == '1':
#             if carry:
#                 result.insert(0, '0')
#             else:
#                 result.insert(0, '1')
#         else:
#             if carry:
#                 result.insert(0, '1')
#                 carry = False
#             else:
#                 result.insert(0, '0')
#     if carry:
#         result.insert(0, '1')

#     return ''.join(result)


# print(addBinary(a, b))


def addBinary(a, b):
    max_digit = max(len(a), len(b))
    a, b = a.zfill(max_digit), b.zfill(max_digit)
    carry = 0
    result = []

    for idx in range(max_digit - 1, -1, -1):
        if a[idx] == '1':
            carry += 1

        if b[idx] == '1':
            carry += 1

        if carry % 2 == 1:
            result.append('1')
        else:
            result.append('0')

        carry //= 2

    if carry == 1:
        result.append('1')

    result.reverse()
    return ''.join(result)


print(addBinary(a, b))
