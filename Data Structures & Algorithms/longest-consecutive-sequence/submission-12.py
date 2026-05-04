class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnum = set(nums)

        longest = 0
        for i, n in enumerate(nums):
            curr = 1
            tmp = n + 1
            while tmp in setnum:
                curr += 1
                tmp += 1
            longest = max(curr, longest)
        return longest

