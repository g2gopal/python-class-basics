def alternating_pattern(length):
    pattern = ""
    for i in range(length):
        if i % 2 == 0:
            pattern += "0"
        else:
            pattern += "1"
    return pattern

# Example usage:
length = 100  # Length of the pattern
pattern = alternating_pattern(length)
print(pattern)
