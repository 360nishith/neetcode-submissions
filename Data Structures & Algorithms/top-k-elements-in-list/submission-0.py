class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        mk=Counter(nums).most_common(k)
        op=[]
        for num,value in mk:
            op.append(num)
        return op