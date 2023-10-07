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

# time of complexity is 0 of N
