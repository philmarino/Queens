#Queens
#place a queen on a nxn board where each queen
#1 is not on the same row as another queen
#2 is not on the same column as another queen
#3 is not within 1 square as another queen (different rule than the chess queen from which the puzzle derives its name)

#https://www.mindgames.com/game/Daily%20Queens
#7x7
#To Do:
#1 make the solution agnostic to board size

#row, column starting from bottom left

#[6, 0] [6, 1] [6, 2] [6, 3] [6, 4] [6, 5] [6, 6]
#[5, 0] [5, 1] [5, 2] [5, 3] [5, 4] [5, 5] [5, 6]
#[4, 0] [4, 1] [4, 2] [4, 3] [4, 4] [4, 5] [4, 6]
#[3, 0] [3, 1] [3, 2] [3, 3] [3, 4] [3, 5] [3, 6]
#[2, 0] [2, 1] [2, 2] [2, 3] [2, 4] [2, 5] [2, 6]
#[1, 0] [1, 1] [1, 2] [1, 3] [1, 4] [1, 5] [1, 6]
#[0, 0] [0, 1] [0, 2] [0, 3] [0, 4] [0, 5] [0, 6]

from itertools import combinations

regions = [
    [[0, 0],[1, 0],[2, 0],[0,1],[0,2]], #teal
    [[6,0],[5,0],[4,0],[3,0],[3,1]], #blue
    [[6,1],[6,2],[6,3],[5,1],[5,2],[5,3],[5,4],[4,1],[4,2],[5,1]], #red
    [[6,4],[6,5]], #green
    [[6,6],[5,5],[5,6],[4,4],[4,5],[4,6],[3,4],[3,5],[3,6],[2,4],[2,5],[2,6]], #yellow
    [[0,3],[0,4]], #orange
    [[4,3],[3,3],[2,1],[2,2],[2,3],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[0,5],[0,6]] #purple
    ]

def valid(locations):
    for comb in combinations(locations, 2):
        if comb[0][0] == comb[1][0]:
            return False #same row
        if comb[0][1] == comb[1][1]:
            return False #same column
        if abs(comb[0][0] - comb[1][0]) == 1 and abs(comb[0][1] - comb[1][1]) == 1:
            return False #within 1 on the diagonal

    #otherwise, it is valid
    return True

for a in regions[0]:
    for b in regions[1]:
        for c in regions[2]:
            for d in regions[3]:
                for e in regions[4]:
                    for f in regions[5]:
                        for g in regions[6]:
                            if valid([a,b,c,d,e,f,g]):
                                print(a, b, c, d, e, f, g)

