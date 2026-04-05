class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        unique = set()

        for n in nums:
            if n != 0:
                unique.add(n)
        
        return len(unique)


        

        


        