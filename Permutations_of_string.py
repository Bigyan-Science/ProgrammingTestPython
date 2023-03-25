#Print all permutation of String both iterative and Recursive way?
def iterative_permutation(word):
    stack = list(word)
    result = [stack.pop()]
    while len(stack) != 0:
        letter = stack.pop()
        temp = []
        for i in result:
            for j in range(len(i) + 1):
                temp.append(i[0:j] + letter + i[j:])
        result = temp
    return result


def recursive_permutation(word):

    # Base case
    if len(word) == 1:
        return [word]

    # Recursive case
    recursive = recursive_permutation(word[1:])

    result = []
    for elements in recursive:
        for i in range(len(elements) + 1):
            result.append(elements[:i] + word[0] + elements[i:])

    return result


string = input("Enter the word you want the permutation of:")
print('Recursive way:')
print(recursive_permutation(string))
print('Iterative way:')
print(iterative_permutation(string))
