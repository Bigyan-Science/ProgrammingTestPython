#How to count the occurrence of a given character in a String?
class CharCounter:
    def __init__(self, string):
        self.string = string

    def count(self, char):
        count = 0
        for c in self.string:
            if c == char:
                count += 1
        return count


counter = CharCounter("hello world")
print(counter.count("l"))