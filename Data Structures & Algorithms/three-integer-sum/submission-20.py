class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)
        for l, n in enumerate(nums):
            if n > 0:
                break
            if l > 0 and nums[l - 1] == n:
                continue
            
            i, j = l + 1, len(nums) - 1
            while i < j:
                if (nums[l] + nums[i] + nums[j]) < 0:
                    i += 1
                elif (nums[l] + nums[i] + nums[j]) > 0:
                    j -= 1
                else:
                    res.append([nums[l], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while nums[i] == nums[i - 1] and i < j:
                        i += 1
                    
        return res