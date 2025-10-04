import time
from saveInfoToFile import saveStaticstc


class Problem:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def goalFound(self, state):
        return state == self.goal


class Node:
    def __init__(self, state, parent=None, cost=0, depth=0, moves=None):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.depth = depth
        self.moves = moves if moves is not None else []

    def add_move(self, move):
        self.moves.append(move)


def Expand(wezel, order):
    children = []
    state = wezel.state
    row, col = whereIsZeroPosition(wezel)

    move_dict = {
        (-1, 0): "U", (1, 0): "D", (0, -1): "L", (0, 1): "R"
    }

    direction = {
        'L': (0, -1),  # Left
        'R': (0, 1),   # Right
        'U': (-1, 0),  # Up
        'D': (1, 0)    # Down
    }

    directions = [direction[char] for char in order]

    for (dr, dc) in directions:
        newRow = row + dr
        newCol = col + dc

        if 0 <= newRow < 4 and 0 <= newCol < 4:
            newState = [r.copy() for r in state]
            newState[row][col], newState[newRow][newCol] = newState[newRow][newCol], newState[row][col]

            newNode = Node(state=newState, parent=wezel, depth=wezel.depth + 1, moves=wezel.moves.copy())
            newNode.add_move(move_dict[(dr, dc)])
            children.append(newNode)

    return children


def is_cycle(wezel):
    rodzic = wezel.parent
    while rodzic:
        if rodzic.state == wezel.state:
            return True
        rodzic = rodzic.parent
    return False


def whereIsZeroPosition(node):
    for row in range(0, 4):
        for col in range(0, 4):
            if node.state[row][col] == 0:
                return row, col


def DepthLimitedSearch(puzzle, lam, order="LR"):
    problem = Problem(puzzle, [[1, 2, 3, 4],
                               [5, 6, 7, 8],
                               [9, 10, 11, 12],
                               [13, 14, 15, 0]])

    startTime = time.time()
    visited = 0
    processed = 0
    maxDepth = 0

    stack = [Node(problem.initial, moves=[])]
    visited_nodes = set()

    while stack:
        node = stack.pop()
        visited += 1
        maxDepth = max(maxDepth, node.depth)

        if problem.goalFound(node.state):
            endTime = time.time()
            return node.moves, len(node.moves), visited, processed, maxDepth, endTime - startTime

        if node.depth < lam:
            children = Expand(node, order)
            for child in reversed(children):
                if not is_cycle(child):
                    processed += 1
                    stack.append(child)

    endTime = time.time()
    return -1, -1, visited, processed, maxDepth, endTime - startTime
