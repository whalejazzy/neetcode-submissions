class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numset = set(nums[:k+1])
        i = k + 1
        if k >= len(nums):
            return len(nums) > len(numset)

        while i < len(nums) and len(numset) == k + 1:
            numset.remove(nums[i - k - 1])
            numset.add(nums[i])
            i += 1

           
        return len(numset) != k + 1

            
