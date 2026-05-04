class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for n in nums:
            curr = 1

            while n+1 in nums:
                n += 1
                curr += 1
            longest = max(longest, curr) 
        return longest