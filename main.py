from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right-1] >= target:
                right -= 1
                continue
            if numbers[left+1] + numbers[right] >= target:
                left += 1
                continue


sol = Solution()

numbers1 = [2, 7, 11, 15]
target1 = 9
output1 = [1, 2]

twoSums = sol.twoSum(numbers1, target1)

assert twoSums == output1

numbers2 = [2, 3, 4]
target2 = 6
output2 = [1, 3]

twoSums = sol.twoSum(numbers2, target2)

assert twoSums == output2

numbers3 = [-1, 0]
target3 = -1
output3 = [1, 2]

twoSums = sol.twoSum(numbers3, target3)

assert twoSums == output3

numbers4 = [5, 25, 75]
target4 = 100
output4 = [2, 3]

twoSums = sol.twoSum(numbers4, target4)

assert twoSums == output4
