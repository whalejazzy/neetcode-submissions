class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bst(l, r):
            idx = (r-l)//2 + l
            print(r, l)
            if idx==l and target != nums[l] and target != nums[r]:
                return -1
            elif nums[r] == target:
                return r
            if target > nums[idx]:
                return bst(idx,r)
            elif target < nums[idx]:
                return bst(l,idx)
            elif nums[idx] == target:
                return idx
            
            
        return bst(0,len(nums) - 1)
        