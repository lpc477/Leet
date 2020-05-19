def longestCommonPrefix(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]
    return shortest


def main():
    test_case = ['flight', 'fly', 'flute']
    result = longestCommonPrefix(test_case)
    print(test_case)
    print(result)
    test_case = ['Patrol', 'Patrick', 'Parent']
    result = longestCommonPrefix(test_case)
    print(test_case)
    print(result)
    test_case = ['Patrol', 'Patrick', 'Parent', 'Kid']
    result = longestCommonPrefix(test_case)
    print(test_case)
    print(result)
    test_case = ['a']
    result = longestCommonPrefix(test_case)
    print(test_case)
    print(result)
    test_case = ['c', 'acc', 'ccc']
    result = longestCommonPrefix(test_case)
    print(test_case)
    print(result)


if __name__ == '__main__':
    main()
