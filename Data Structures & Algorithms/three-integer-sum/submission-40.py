class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sliding window solution
        nums.sort()
        
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    # print(i, j, k, [nums[i], nums[j], nums[k]])
                    res.append([nums[i], nums[j], nums[k]])

                    
                    while j + 1< k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
        return res