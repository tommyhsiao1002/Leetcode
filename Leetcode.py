# Two Sum	
# Brute-Force : time-complexity = O(n^2)
    def twoSumBF(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    lst = [i,j]
        return lst
# Using hash table to reduce time-complexity
# https://www.youtube.com/watch?v=2uWRxgN1Sbo&ab_channel=OverTheShoulderCoding
# https://medium.com/@havbgbg68/leetcode-1-two-sum-python-8d77c223abd3

    def twoSum (self, nums, target):
        hashtable = {}
        target - nums = num
        for i in range(len(nums)):
            if num in hashtable:
                return [hashtable[num], i]
            else:
                hashtable[num] = i
        
        
