# Given an array of integers and a target sum, return all unique pairs of indices or values that sum up to the target.
# Do not return duplicate pairs (e.g., [2,3] and [3,2] should count as one).

def run_tests():
    sol = Solution()

    # ✅ Test Case 1: Basic pair
    result = sol.twoSumAllUnique([2, 7, 11, 15], 9)
    expected = [[2, 7]]
    assert sorted([sorted(p) for p in result]) == sorted(expected)

    # ✅ Test Case 2: Multiple valid pairs
    result = sol.twoSumAllUnique([1, 2, 3, 4, 5], 6)
    expected = [[1, 5], [2, 4]]
    assert sorted([sorted(p) for p in result]) == sorted(expected)

    # ✅ Test Case 3: Duplicates in input, only one pair expected
    result = sol.twoSumAllUnique([3, 3, 3], 6)
    expected = [[3, 3]]
    assert sorted([sorted(p) for p in result]) == sorted(expected)

    # ✅ Test Case 4: Negative numbers
    result = sol.twoSumAllUnique([-1, -2, -3, -4, -5], -8)
    expected = [[-5, -3]]
    assert sorted([sorted(p) for p in result]) == sorted(expected)

    # ✅ Test Case 5: No valid pair
    result = sol.twoSumAllUnique([1, 2, 3], 100)
    expected = []
    assert result == expected

    # ✅ Test Case 6: Mixed positive/negative
    result = sol.twoSumAllUnique([-2, 1, 3, 5, -1, 0], 1)
    expected = [[-2, 3], [-1, 2], [0, 1]]  # adjust if 2 isn't in list
    expected_filtered = [pair for pair in expected if all(x in [-2, -1, 0, 1, 3, 5] for x in pair)]
    assert sorted([sorted(p) for p in result]) == sorted(expected_filtered)

    print("✅ All test cases passed!")

class Solution(object):
    def twoSumAllUnique(self, nums, target):
        seen = set()

        result = set()

        for num in nums:
            complement = target-num
            if complement in seen:
                result.add(tuple(sorted((num, complement))))
            seen.add(num)
        
        return [list(pair) for pair in result]
    
run_tests()
# The time complexity is O(n+k) and the space complexity is O(n+k).
