class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        wdw = set()
        L = 0 
        for R in range(len(nums)):
            if R-L > k:
                wdw.remove(nums[L])
                L += 1
            if nums[R] in wdw:
                return True
            wdw.add(nums[R])
        return False
        