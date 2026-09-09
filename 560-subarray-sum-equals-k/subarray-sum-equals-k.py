class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        sum=0
        c=0
        for num in nums:
            sum+=num
            if (sum-k) in d:
                c+=d[sum-k]
            d[sum]=d.get(sum,0)+1
        return c