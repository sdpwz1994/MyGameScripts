
def getLine(scene, idx):
    return [scene[0][idx], scene[1][idx], scene[2][idx], scene[3][idx]]

def matched(scene):
    flag = [True] * 12
    # 靴子格式校验
    for i in range(0,12):
        line = getLine(scene, i)
        if(line not in [[0,0,0,0],[0,0,1,1],[1,1,1,1]]):
            return False
        if(line == [0,0,1,1]):
            flag[i] = False
    # 锤子格式校验
    for i in range(0,12):
        if(flag[i]):
            continue
        if(flag[i-1] and flag[(i+1)%12]):
            return False
    return True

# print(matched(board))

# 左移一位
def doRowMoveStep(scene, idx) -> str:
    a=scene[idx][0]
    for i in range(0, 11):
        scene[idx][i]=scene[idx][(i+1) % 12]
    scene[idx][11]=a

def rowMoveStep(scene, idx, step) -> str:
    for i in range(0, step):
        doRowMoveStep(scene, idx)
    return "第"+str(idx+1)+"行，左移"+str(step)+"次"

#for i in range(0, 11):
#    rowMoveStep(board, 3)
#print(board)

# 下移一位
def doLineDownStep(scene, idx):
    otherIdx = (idx+6) % 12
    a = scene[0][idx]
    scene[0][idx] = scene[0][otherIdx]
    scene[0][otherIdx] = scene[1][otherIdx]
    scene[1][otherIdx] = scene[2][otherIdx]
    scene[2][otherIdx] = scene[3][otherIdx]
    scene[3][otherIdx] = scene[3][idx]
    scene[3][idx] = scene[2][idx]
    scene[2][idx] = scene[1][idx]
    scene[1][idx] = a

def lineDownStep(scene, idx, step) -> str:
    for i in range(0, step):
        doLineDownStep(scene, idx)
    return "第"+str(idx+1)+"列，下移"+str(step)+"次"

#lineDownStep(board, 0)
#print(board)

def doMove(board, stack, time):
    if(time<=0):
        return
    for row in range(0, 4):
        for i in range(1, 12):
            stack.append(rowMoveStep(board, row, i))
            if(matched(board)):
                for s in stack:
                    print(s)
                print(board)
            doMove(board, stack, time-1)
            stack.pop()
            rowMoveStep(board, row, 12-i)
    for line in range(0, 6):
        for i in range(1, 8):
            stack.append(lineDownStep(board, line, i))
            if(matched(board)):
                for s in stack:
                    print(s)
                print(board)
            doMove(board, stack, time-1)
            stack.pop()
            lineDownStep(board, line, 8-i)


# test case
# board = [
#     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
#     [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0]
# ]

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
]

doMove(board, [], 2)

