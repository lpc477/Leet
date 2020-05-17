def convert_numerals(s):
    pattern = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    skip_next = False
    for i, char in enumerate(s):
        if skip_next:
            skip_next = False
            continue
        if i + 1 <= len(s) - 1:
            if pattern[char] < pattern[s[i + 1]]:
                total += pattern[s[i + 1]] - pattern[char]
                skip_next = True
            else:
                total += pattern[char]
        else:
            total += pattern[char]

    return total


def main():
    test_case = "IV"
    result = convert_numerals(test_case)
    print(test_case)
    print(result)


if __name__ == '__main__':
    main()
