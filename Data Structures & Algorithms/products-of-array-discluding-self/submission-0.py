class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        for i in range(1, len(nums)):
            pref.append(nums[i-1] * pref[-1])

        suff = [1]
        for i in range(len(nums)-2, -1, -1):
            suff.append(nums[i+1] * suff[-1])

        suff = suff[::-1]
        res = []
        for i in range(len(nums)):
            res.append(pref[i] * suff[i])
        
        return res