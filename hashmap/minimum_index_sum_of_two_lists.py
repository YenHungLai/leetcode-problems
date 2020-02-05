list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Burger King", "Tapioca Express", "Shogun"]


def findRestaurant(list1, list2):
    my_map = {}

    for i in range(len(list1)):
        if list1[i] in list2:
            my_map[list1[i]] = i + list2.index(list1[i])

    print(my_map)
    min_sum = my_map[min(my_map, key=lambda k: my_map[k])]
    return [i for i in my_map.keys() if my_map[i] == min_sum]


print(findRestaurant(list1, list2))
