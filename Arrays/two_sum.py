# Problem: https://leetcode.com/problems/two-sum/
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

def run_tests():
    sol = Solution()

    # ✅ Test Case 1: Basic input
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]

    # ✅ Test Case 2: Negative numbers
    assert sol.twoSum([-3, 4, 3, 90], 0) == [0, 2]

    # ✅ Test Case 3: Duplicates allowed
    assert sol.twoSum([3, 3], 6) == [0, 1]

    # ✅ Test Case 4: Multiple possible pairs (only first valid returned)
    result = sol.twoSum([1, 2, 3, 4, 5], 6)
    assert result in [[1, 3], [0, 4]]  # both are valid

    # 🚨 Test Case 5: No valid pair
    assert sol.twoSum([1, 2, 3], 7) == [-1, -1]

    print("✅ All test cases passed!")

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i in range(0, len(nums)):
            cur = target-nums[i]
            if cur in seen:
                return [seen[cur],i]
            else:
                seen[nums[i]] = i
        
        return [-1,-1]

run_tests()