class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bst(l, r):
            m = (r - l) // 2 + l
            if l > r:
                return -1
            if nums[m] == target:
                return m
            elif nums[m] < target:
                print("left")
                return bst(m + 1, r)
            else:
                print(m ,"right")
                return bst(l, m - 1)
                
            
        return bst(0,len(nums) - 1)
        