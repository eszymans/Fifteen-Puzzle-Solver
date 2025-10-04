from queue import PriorityQueue
import time as t

class Node:
    def __init__(self, state, moves, parent, priority):
        self.state = state
        self.parent = parent
        self.moves = moves #jako sciezka
        self.priority = priority

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.state))

    def __lt__(self, other):
        return self.priority < other.priority

def isGoal(state):
    return state == [[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9,10,11,12],
                     [13,14,15, 0]]

def whereIsZeroPosition(node):
    for row in range(0,4):
        for col in range(0,4):
            if node.state[row][col] == 0:
                return row, col

def hamming(state):
    value = 0
    for row in range(0, 4):
        for col in range(0, 4):
            if row == 3 and col == 3:
                if state[row][col] != 0:
                    value = value + 1
            elif state[row][col] != row * 4 + col + 1:
                value = value + 1
    return value

def manhattan(state):
    value = 0
    for row in range(4):
        for col in range(4):
            val = state[row][col]
            if val != 0:  # zakładamy, że 0 to puste pole
                goalRow = (val - 1) // 4
                goalCol = (val - 1) % 4
                value += abs(goalRow - row) + abs(goalCol - col)
    return value

def currentDepth(node):
    return len(node.moves)

def neighbours(node, heuristicFunction):
    neighbors = []
    state = node.state
    row, col = whereIsZeroPosition(node)

    moves = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]

    for dr, dc, move in moves:
        newRow = row + dr
        newCol = col + dc

        if 0 <= newRow < 4 and 0 <= newCol < 4:
            newState = [row.copy() for row in state]
            newState[row][col], newState[newRow][newCol] = newState[newRow][newCol], newState[row][col]

            priority = heuristicFunction(newState) + currentDepth(node) + 1
            newMoves = node.moves + [move]
            newNode = Node(state=newState, moves=newMoves, parent=node, priority=priority)
            neighbors.append(newNode)

    return neighbors

def astar(start, heuristic):
    if heuristic == "manh":
        heuristicFunction = manhattan
    elif heuristic == "hamm":
        heuristicFunction = hamming

    numerOfVisitedStates = 0
    numberOfProcessedStates = 0
    maxDepth = 0

    startTime = t.time()
    startNode = Node(state=start, moves=[], parent=None, priority=0)
    closedList = set()
    priorityQueue = PriorityQueue()

    priorityQueue.put((0, startNode))

    while not priorityQueue.empty():
        _, node = priorityQueue.get()
        numberOfProcessedStates += 1
        if node not in closedList:
            if isGoal(node.state):
                endTime = t.time()
                time = round(endTime - startTime, 3)
                return node.moves, len(node.moves), numerOfVisitedStates, numberOfProcessedStates,  maxDepth, time
            closedList.add(node)
            for n in neighbours(node, heuristicFunction):
                numerOfVisitedStates += 1
                maxDepth = max(maxDepth, len(n.moves))
                if n not in closedList:
                    priority = currentDepth(n) + heuristicFunction(n.state)
                    priorityQueue.put((priority, n))

    endTime = t.time()
    time = round(endTime - startTime, 3)
    return -1, -1, numerOfVisitedStates, numberOfProcessedStates,  maxDepth, time