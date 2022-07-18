class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        numOfJewels = 0
        jewelList = {}
        
        for jewel in jewels:
            jewelList[jewel] = "jewel"
        
        for stone in stones:
            if stone in jewelList:
                numOfJewels += 1
            
        return numOfJewels