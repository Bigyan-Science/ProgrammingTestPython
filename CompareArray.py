#Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which number is not present in the second array.
class ArrayComparator:
    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2

    def find_missing_number(self):
        for num in self.arr1:
            if num not in self.arr2:
                return num


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 1, 0, 5]
comparator = ArrayComparator(arr1, arr2)
missing_number = comparator.find_missing_number()
print("The missing number is",missing_number)