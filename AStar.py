global g
g = 0
def solvable(start):
    inversion = 0
    for i in range(9):
        if start[i] == -1:
            continue
        for j in range(i+1, 9):
            if start[j] == -1:
                continue
            if start[i] > start[j]:
                inversion += 1

    if inversion%2 == 0:
        return True
    return False

def printPuzzle(puzlist):
    for i in range(9):
        if i%3 == 0:
            print()
        if puzlist[i] == -1:
            print("_", end = " ")
        else:
            print(puzlist[i], end = " ")
    print()

def heuristic(start, goal):
    global g
    h = 0
    for i in range(9):
        for j in range(9):
            if start[i] == goal[j] and start[i] != -1:
                h += (abs(j-i))//3 + (abs(j-i))%3
    return g+h

def moveLeft(start, position):
    start[position], start[position-1] = start[position-1], start[position]

def moveRight(start, position):
    start[position], start[position+1] = start[position+1] , start[position]

def moveUp(start, position):
    start[position], start[position-3] = start[position-3], start[position]

def moveDown(start, position):
    start[position], start[position+3] = start[position+3], start[position]

def moveTile(start, goal):

    blank = start.index(-1)
    row = blank//3
    col = blank%3

    t1, t2, t3, t4 = start[:], start[:], start[:], start[:]
    f1, f2, f3, f4 = 100, 100, 100, 100

    if col-1 >=0:
        moveLeft(t1, blank)
        f1 = heuristic(t1, goal)
    if col+1 < 3:
        moveRight(t2, blank)
        f2 = heuristic(t2, goal)
    if row+1 < 3:
        moveDown(t3, blank)
        f3 = heuristic(t3, goal)
    if row - 1 >= 0:
        moveUp(t4, blank) 
        f4 = heuristic(t4, goal)
    
    minHeuristic = min(f1, f2, f3, f4)

    if f1 == minHeuristic:
        moveLeft(start, blank)
    if f2 == minHeuristic:
        moveRight(start, blank)
    if f3 == minHeuristic:
        moveDown(start, blank)
    if f4 == minHeuristic:
        moveUp(start, blank)

def solvePuzzle(start, goal):
    global g
    g+=1
    moveTile(start, goal)
    printPuzzle(start)
    f = heuristic(start, goal)
    if f == g:
        print(f"Solved in {f} moves.")
        return
    solvePuzzle(start, goal)

start = list()
goal = list()
print("Enter the start state:(Enter -1 for empty):")
for i in range(9):
    start.append(int(input()))
print("Enter the goal state:(Enter -1 for empty):")
for i in range(9):
    goal.append(int(input()))

if (solvable(start)):
    print("Solvable")
    print('-------------------------------')
    printPuzzle(start)
    print('-------------------------------')
    solvePuzzle(start, goal)
else:
    print("Cannot solve the puzzle")



# # Input
# start = [1, 2, 3, -1, 4, 6, 7, 5, 8]
# goal = [1, 2, 3, 4, 5, 6, 7, 8, -1]