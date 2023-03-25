#In an array 1-100 multiple numbers are duplicates, how do you find it?
class FindDuplicates:
    def __init__(self, arr):
        self.arr = arr

    def find_duplicates(self):
        frequency=[]
        duplicates = []
        for num in self.arr:
            if num in frequency:
                duplicates.append(num)
            else:
                frequency.append(num)

        return duplicates


arr = [1,1, 2, 3, 4, 5, 6, 7, 7,8, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20]
finder = FindDuplicates(arr)
duplicates = finder.find_duplicates()
print(duplicates)