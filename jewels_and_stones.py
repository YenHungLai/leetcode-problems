j = "aA"
s = "aAAbbbb"


# def numJewelsInStones(j, s):
#     """Brute force"""
#     result = 0
#     for stone in s:
#         if stone in j:
#             result += 1

#     return result


# print(numJewelsInStones(j, s))


# def numJewelsInStones(j, s):
#     stone_map = {stone: s.count(stone) for stone in s}
#     return sum(stone_map[jewel] for jewel in j if jewel in stone_map)


# print(numJewelsInStones(j, s))


def numJewelsInStones(j, s):
    j_map = set(j)
    # Boolean value as increment value.
    return sum(s in j_map for s in s)


print(numJewelsInStones(j, s))
