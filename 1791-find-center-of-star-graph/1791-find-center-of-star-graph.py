class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        map = {}
        for i in range(len(edges)):
            for j in range(len(edges[i])):
                if edges[i][j] in map:
                    map[edges[i][j]] += 1
                else:
                    map[edges[i][j]] = 1                    
                    
        larg = 0
        for item in map:
            if map[item] > larg:
                larg = item
        
        return larg