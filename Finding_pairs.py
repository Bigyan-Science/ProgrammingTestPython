#How to find all pairs in an array of integers whose sum is equal to the given number
class FindPairs:
    def __init__(self, arr, target_sum):
        self.arr = arr
        self.target_sum = target_sum

    def find_pairs(self):
        pairs = []
        for i in range(len(self.arr)):
            for j in range(i + 1, len(self.arr)):
                if self.arr[i] + self.arr[j] == self.target_sum:
                    pairs.append((self.arr[i], self.arr[j]))
        return pairs


arr = [2, 4, 6, 8, 10]
target_sum = 12
finder = FindPairs(arr, target_sum)
pairs = finder.find_pairs()
print(pairs)