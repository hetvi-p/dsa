class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1 
            
        currentGas = 0
        startingIndex = -1

        for i in range(len(gas)):
            if currentGas + gas[i] >= cost[i]:
                if startingIndex == -1:
                    startingIndex = i
                currentGas += gas[i] - cost[i]
            else: 
                startingIndex = -1
                currentGas = 0

        return startingIndex







        