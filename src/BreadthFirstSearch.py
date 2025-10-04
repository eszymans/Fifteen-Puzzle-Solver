from collections import deque
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

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.state))

    def add_move(self, move):
        self.moves.append(move)


def Expand(node, order="LR"):
    childrean = []
    state = node.state
    row, col = whereIsZeroPosition(node)

    move_dict = {
        (-1, 0): "U",  (1, 0): "D", (0, -1): "L", (0, 1): "R"
    }

    direction = {
        'L': (0, -1),  # Left
        'R': (0, 1),  # Right
        'U': (-1, 0),  # Up
        'D': (1, 0)  # Down
    }

    directions = [direction[char] for char in order]

    for (dr, dc) in directions:
        newRow = row + dr
        newCol = col + dc
        if 0 <= newRow < 4 and 0 <= newCol < 4:
            newState = [r.copy() for r in state]
            newState[row][col], newState[newRow][newCol] = newState[newRow][newCol], newState[row][col]
            newNode = Node(state=newState, parent=node, depth=node.depth + 1, moves=node.moves.copy())
            newNode.add_move(move_dict[(dr, dc)])
            childrean.append(newNode)

    return childrean



def whereIsZeroPosition(node):
    for row in range(0, 4):
        for col in range(0, 4):
            if node.state[row][col] == 0:
                return row, col


def failture():
    return "Expected state has not been found"


def BreadthFirstSearch(puzzle, order="LR"):
    problem = Problem(puzzle, [[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9,10,11,12],
                     [13,14,15, 0]])

    startTime = time.time()
    visited = 0
    processed = 0
    maxDepth = 0


    node = Node(problem.initial, moves=[])
    if problem.goalFound(node.state):
        endTime = time.time()
        return node.moves, len(node.moves), visited, processed, maxDepth, endTime - startTime

    limit = deque()
    limit.append(node)
    acquired = set()
    acquired.add(tuple(map(tuple, problem.initial)))  # Konwertuje listę na krotkę

    while limit:
        node = limit.popleft()
        processed += 1

        childrean = Expand(node, order)

        for child in childrean:
            if tuple(map(tuple, child.state)) not in acquired:
                child.parent = node
                child.depth = node.depth + 1
                visited += 1
                maxDepth = max(maxDepth, child.depth)

                if problem.goalFound(child.state):
                    endTime = time.time()
                    return child.moves, len(child.moves), visited, processed, maxDepth, endTime - startTime

                acquired.add(tuple(map(tuple, child.state)))
                limit.append(child)

    endTime = time.time()
    return -1, -1, visited, processed, maxDepth, endTime - startTime
