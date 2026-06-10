class Solution:
    def findRotation(self, matrix: List[List[int]], target: List[List[int]]) -> bool:
        def rotate90(m):
            n = len(m)
            return [[m[n - 1 - r][c] for r in range(n)] for c in range(n)]
        
        for _ in range(4):
            if matrix == target:
                return True
            matrix = rotate90(matrix)
        
        return False