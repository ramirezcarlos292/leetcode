class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        ranks = ["Gold Medal","Silver Medal","Bronze Medal"]
        result = [""] * n
        heap = []
        for i in range(n):
            heap.append((-score[i], i))
        heapq.heapify(heap)
        
        for rank in range(n):
            score, idx = heapq.heappop(heap)
            if rank < 3:
                result[idx] = ranks[rank]
            else:
                result[idx] = str(rank+1)
        return result
            

        

