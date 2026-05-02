class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, prefix = 0, 0
        prefixSums = { 0 : 1 }
        
        for num in nums:
            prefix += num
            diff = prefix - k

            res += prefixSums.get(diff, 0)
            prefixSums[prefix] = 1 + prefixSums.get(prefix, 0)

        return res 
            
                