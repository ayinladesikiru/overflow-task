def compress(string: str) -> str:
    compressed = ""
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            compressed += string[i - 1] + str(count)
            count = 1
    compressed += string[-1] + str(count)
    return compressed if len(compressed) < len(string) else string

# The time complexity of the compress function is O(n), where n is the length of the input string.
# This is because the function iterates over the input string once, and the number of operations performed in the
# loop is constant. The only additional operation performed is the concatenation of the compressed string at the end
# of the function, but this operation also takes constant time.
