class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 2:
            return 0

        first = float('-inf')
        second = float('-inf')

        for num in nums:
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num

        return (first - 1) * (second - 1)

def run_tests():
    sol = Solution()

    # ✅ Test Case 1: Basic case
    result = sol.maxProduct([3, 4, 5, 2])
    expected = 12
    assert result == expected, f"Test Case 1 Failed: Expected {expected}, got {result}"

    # ✅ Test Case 2: Case with negative numbers
    result = sol.maxProduct([-1, -2, -3, -4])
    expected = 6
    assert result == expected, f"Test Case 2 Failed: Expected {expected}, got {result}"

    # ✅ Test Case 3: Case with all elements the same
    result = sol.maxProduct([5, 5, 5, 5])
    expected = 16
    assert result == expected, f"Test Case 3 Failed: Expected {expected}, got {result}"

    # ✅ Test Case 4: Case with only two elements
    result = sol.maxProduct([1, 5])
    expected = 0
    assert result == expected, f"Test Case 4 Failed: Expected {expected}, got {result}"

    # ✅ Test Case 5: Case with all zeros
    result = sol.maxProduct([0, 0, 0, 0])
    expected = 1
    assert result == expected, f"Test Case 5 Failed: Expected {expected}, got {result}"

    # ✅ Test Case 6: Case with one element (edge case)
    result = sol.maxProduct([10])
    expected = 0  # Assuming we return 0 in case there's not enough data
    assert result == expected, f"Test Case 6 Failed: Expected {expected}, got {result}"

    # ✅ Test Case 7: Case with two equal maximums
    result = sol.maxProduct([10, 10, 5, 2])
    expected = 81
    assert result == expected, f"Test Case 7 Failed: Expected {expected}, got {result}"

    # ✅ Test Case 8: Case with large numbers
    result = sol.maxProduct([1000, 10000, 100000])
    expected = 999890001
    assert result == expected, f"Test Case 8 Failed: Expected {expected}, got {result}"

    print("✅ All test cases passed!")


run_tests()