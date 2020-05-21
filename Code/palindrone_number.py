def isPalindrome(x):
    x = str(x)
    li = list(x)
    ran = len(li) - 1
    index = 0
    while index < ran:
        if li[index] not in li[ran]:
            return False
        index = index + 1
        ran = ran - 1
    return True


def main():
    testcase = 121
    bool = isPalindrome(testcase)
    print(testcase)
    print(bool)


if __name__ == '__main__':
    main()
