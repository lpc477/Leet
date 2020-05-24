def remove_element(nums, val):
    index = 0
    for num in nums:
        if num is not val:
            nums[index] = num
            index += 1
    return index


def main():
    return


if __name__ == '__main__':
    main()