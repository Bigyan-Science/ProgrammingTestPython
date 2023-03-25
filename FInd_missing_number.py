#4 In an array 1-100 numbers are stored, one number is missing how do you find it?
class FIndMissingNumber:
    def __init__(self, arr):
        self.arr = arr

    def find_missing_number(self):
        n = 100
        total_sum = (n * (n + 1)) // 2
        arr_sum = sum(self.arr)
        missing_number = total_sum - arr_sum
        return missing_number


arr = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
       21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
       41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
       61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
       81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

finder = FIndMissingNumber(arr)
missing_num = finder.find_missing_number()
print("Missing number:", missing_num)