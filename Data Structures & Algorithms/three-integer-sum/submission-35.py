class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and nums[i-1] == n:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if n + nums[l] + nums[r] == 0:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                elif n + nums[l] + nums[r] < 0:
                    l+= 1
                else:
                    r-= 1
        return res

