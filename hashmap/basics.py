# A hash set stores a single value.
class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Initialize list of lists
        # Use _ when index value is not important
        self.bucket = [[] for _ in range(20)]

    def hashFunction(self, key):
        return key % 5

    def add(self, key: int) -> None:
        if key not in self.bucket[self.hashFunction(key)]:
            self.bucket[self.hashFunction(key)].append(key)
        print(self.bucket)

    def remove(self, key: int) -> None:
        if key in self.bucket[self.hashFunction(key)]:
            self.bucket[self.hashFunction(key)].remove(key)
        print(self.bucket)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.bucket[self.hashFunction(key)]

# A hash map stores key value pairs.
class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = [[] for _ in range(20)]

    def hashFunction(self, key):
        return key % 5

    def if_exist(self, key):
        return key in self.bucket[self.hashFunction(key)].keys()

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        temp = self.bucket[self.hashFunction(key)]
        for i in temp:
            if i[0] == key:
                temp.remove(i)
                temp.append((key, value))
                return self.bucket

        temp.append((key, value))

        return self.bucket

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        temp = self.bucket[self.hashFunction(key)]
        for i in temp:
            if i[0] == key:
                return i[1]

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        temp = self.bucket[self.hashFunction(key)]
        for i in temp:
            if i[0] == key:
                temp.remove(i)
                return

        return -1

hashMap = MyHashMap()    
print(hashMap.put(1, 1))          
print(hashMap.put(2, 2)) 
print(hashMap.get(1))            # returns 1
print(hashMap.get(3))            # returns -1 (not found)
print(hashMap.put(2, 1))         # update the existing value
print(hashMap.get(2))            # returns 1 
print(hashMap.remove(2))         # remove the mapping for 2
print(hashMap.get(2))            # returns -1 (not found) 