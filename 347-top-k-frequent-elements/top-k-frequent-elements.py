class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        b = []
        sorted_elements = sorted(d.keys(), key=lambda x: d[x], reverse=True)
        for i in range(k):
            b.append(sorted_elements[i])
        return b