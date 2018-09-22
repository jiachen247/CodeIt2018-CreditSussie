# 1. Sorting Game
import sys

sys.setrecursionlimit(362880000)

puzzle = (
    (1,2,3),
(4,8,5),
(7,6,0)
)

x_matrix_dimensions = len(puzzle)
y_matrix_dimensions = len(puzzle)

state = []

SOLN = (
    (1,2,3),
    (4,5,6),
    (7,8,0)
)


def check(p):

    if p[x_matrix_dimensions-1][y_matrix_dimensions-1] != 0:
        return False

    else:
        i =[item for sublist in p for item in sublist]
        print(i)

        for a in range(x_matrix_dimensions * y_matrix_dimensions):
            if a == x_matrix_dimensions * y_matrix_dimensions - 1:
                if p[a] == 0:
                    return True
            if i[a] > i[a+1]


    return True

def find_zero(p):

    for x in range(x_matrix_dimensions):
        for y in range(y_matrix_dimensions):
            if p[x][y] == 0:
                return [x,y]

    print("[+] zero not found.")
    return [-1, -1]



def calculate_moves(p, zero_index):

    moves = []

    x = zero_index[0]
    y = zero_index[1]
    print(x,y)

    if y > 0:
        if y == 1:
            if not (p[0][0] == 1 and p[1][0] == 4 and p[2][0] == 7):
                moves.append([x, y - 1])
            else:
                print("147 done")
        else:
            moves.append([x, y - 1])
    if y < 2:
        moves.append([x, y+1])

    if x > 0:
        if x == 1:
            print("x == 1")
            if p[0] != (1, 2, 3):
                moves.append([x - 1, y])
            else:
                print("123 done")
        else:
            moves.append([x - 1, y])

    if x < 2:
        moves.append([x + 1, y])

    print(moves)
    return moves

TARGET_HASH = 304

def swap_moves(p, zero_index, target):
    p1 = [list(x) for x in p]
    p1[zero_index[0]][zero_index[1]] = p1[target[0]][target[1]]
    p1[target[0]][target[1]] = 0
    return tuple(p1)

def solve(p, history):
    print(p)
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

    moves = calculate_moves(p, zero_index)

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

check(puzzle)
# print(solve(puzzle, []))



# caculate possible moves



