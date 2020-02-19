# class TwoSum:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.numbers = {}

#     def add(self, number: int) -> None:
#         """
#         Add the number to an internal data structure..
#         """
#         if number in self.numbers:
#             self.numbers[number] += 1
#         else:
#             self.numbers[number] = 1

#     def find(self, value: int) -> bool:
#         """
#         Find if there exists any pair of numbers which sum is equal to the value.
#         """
#         print(self.numbers)
#         for k, v in self.numbers.items():
#             target = value - k
#             if target != k:
#                 if target in self.numbers:
#                     return True
#             else:
#                 # You need two of the same number to form a pair
#                 if self.numbers[k] > 1:
#                     return True

#         return False


class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numbers = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.numbers.append(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        self.numbers.sort()
        print(self.numbers)
        low, high = 0, len(self.numbers) - 1

        while low < high:
            sum = self.numbers[low] + self.numbers[high]
            if sum < value:
                low += 1
            elif sum > value:
                high -= 1
            else:
                return True

        return False


# Your TwoSum object will be instantiated and called as such:
obj = TwoSum()
# obj.add(1)
# obj.add(3)
# obj.add(5)
# print(obj.find(4))
# print(obj.find(7))

obj.add(3)
obj.add(1)
obj.add(2)
print(obj.find(3))
print(obj.find(6))
