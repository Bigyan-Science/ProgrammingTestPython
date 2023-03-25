#Write a function to find out the longest palindrome in a given string?
class Longest_palindrome:

    #constructor of the class taking a string as input and initializes as an instance variable self.s
    def __init__(self, s):
        self.s = s

    def find_longest_palindrome(self):
        if len(self.s) == 0:
            return ""

        longest_palindrome = self.s[0]

        for i in range(len(self.s)):
            for j in range(i + 1, len(self.s) + 1):
                sub_string = self.s[i:j]
                #checking whether the formed substring is palindrome or not by reversing and equating it.
                if sub_string == sub_string[::-1]:
                    if len(sub_string) > len(longest_palindrome):
                        longest_palindrome = sub_string

        return longest_palindrome

user_input =input("Enter a string to check the longest palindrome\n")

#creating instance of class as obj
obj = Longest_palindrome(user_input)
print("The longest palindrome in the given string is:",obj.find_longest_palindrome())
# print(obj.find_longest_palindrome()) 