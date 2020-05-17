class Solution(object):
    def twoSum(self, nums, target):
        index = 0
        while index < len(nums):
            index2 = index
            while index2 < len(nums):
                number1 = nums[index]
                number2 = nums[index2]
                subtotal = target - number2
                if subtotal == number1 and index is not index2:
                    return [index, index2]
                index2 = index2 + 1
            index = index + 1
        return


def main():
    do = Solution
    print(do.twoSum(do, [2222222, 2222222], 4444444))


if __name__ == "__main__":
    main()
