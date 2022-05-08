class Solution:
    def solve(self, moves, x, y):
        pos = [0,0]
        for move in moves:
            if(move == "NORTH"):
                pos[1] = pos[1] + 1
                continue
            if(move == "EAST"):
                pos[0] = pos[0] + 1
                continue
            if(move == "SOUTH"):
                pos[1] = pos[1] - 1
            if(move == "WEST"):
                pos[0] = pos[0] - 1
        return pos[0] == x and pos[1] == y 
solution = Solution()
print(solution.solve(moves = ["WEST", "EAST"],
x = 1,
y = 0))