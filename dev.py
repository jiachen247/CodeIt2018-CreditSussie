# 1. Sorting Game
import sys

sys.setrecursionlimit(362880000)

input = '{' \
  '"puzzle":[' \
            '[1,2,3],' \
            '[4,8,5]' \
            '[7,6,0]' \
          ']' \
    '}'
'}'

puzzle = (
    (1,2,3),
(4,8,5),
(7,6,0)
)

matrix_dimensions = 3



state = []
SOLN = (
    (1,2,3),
    (4,5,6),
    (7,8,0)
)

def _hash(p):
    return (p[0][0] * 1) * \
           (p[0][1] * 2) * \
           (p[0][2] * 3) * \
           (p[1][0] * 5) * \
           (p[1][1] * 7) * \
           (p[1][2] * 9) * \
           (p[2][0] * 11) * \
           (p[2][1] * 13) * \
           (p[2][2] * 17)

def find_zero(p):

    for x in range(matrix_dimensions):
        for y in range(matrix_dimensions):
            if p[x][y] == 0:
                return [x,y]

    print("[+] zero not found.")
    return [-1, -1]



def calculate_moves(zero_index):
    moves = []

    x = zero_index[0]
    y = zero_index[1]



    if y > 0:
        moves.append([x, y-1])

    if y < 2:
        moves.append([x, y+1])

    if x > 0:
        moves.append([x - 1, y])

    if x < 2:
        moves.append([x + 1, y])

    return moves

TARGET_HASH = 304

def swap_moves(p, zero_index, target):
    p1 = [list(x) for x in p]
    p1[zero_index[0]][zero_index[1]] = p1[target[0]][target[1]]
    p1[target[0]][target[1]] = 0
    return tuple(p1)

def solve(p, history):
    global state
    # print("P : {}".format(p))
    #print("s: {}".format(state))
    # current_hash = _hash(p)
    # print("HASH : {}".format(current_hash))

    if p == SOLN:
        print("FOUNDDDDDDDDDD PLS")
        return p

    if p in state:
        print("repeat")
        return None

    state  = state + [p]
    zero_index = find_zero(p)

    moves = calculate_moves(zero_index)

    for move in moves:
        # print("history {}".format(history))
        target = p[move[0]][move[1]]

        newp = swap_moves(p, zero_index, move)
        if newp not in state:
            history.append(target)
            if solve(newp, history[:]) is not None:
                print("FOUNDDDD FOUNDDD")
                # print(history)
                return history

    # print("endign state : {}".format(state))
    # return None





# print(_hash([
#     [1,2,3],
#     [4,5,6],
#     [7,8,0]
# ])) # 304


print(solve(puzzle, []))



# caculate possible moves



