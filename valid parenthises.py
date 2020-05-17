def isValid(s):
    pattern = {')': '(', ']': '[', '}': '{'}
    heads = []
    for char in s:
        if char in pattern:
            if len(heads) > 0:
                head = heads.pop()
            else:
                head = 'X'
            if pattern[char] != head:
                return False
        else:
            heads.append(char)
    if len(heads) is 0:
        return True
    else:
        return False


def main():
    test = "([][})"
    print(isValid(test))


if __name__ == '__main__':
    main()