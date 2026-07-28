class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        key = {}
        for i in range(len(nums)):
            if (target - nums[i]) in key:
                return [key[target - nums[i]], i]
            key[nums[i]] = i
