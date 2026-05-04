class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        curr = res = 0
        for R in range(len(arr)):
            if R - L < k:
                curr += arr[R]
            else:
                curr += arr[R]
                curr -= arr[L]
                L += 1
            if R - L + 1 == k and curr / k >= threshold:
                res += 1
            
        return res
