import sys
import os

import Astar as astr
import BreadthFirstSearch as bfs
import DepthLimitedSearch as dfs
from saveInfoToFile import saveStaticstc

def fileStartUpLoading(file):
    puzzle = []
    with open(file, 'r') as f:
        w, k = map(int, f.readline().split())
        for line in f:
            puzzle.append(list(map(int, line.split())))
    return w, k, puzzle

def fileSolutionSaving(file, n, moves):

    with open(file, 'w') as f:
        if n == -1:
            f.write("-1\n")
        else:
            f.write(f"{n}\n")
            for move in moves:
                f.write(f"{move}")

def main():
    print("Argumenty:", sys.argv)

    if len(sys.argv) != 6:
        print("Błędna liczba argumentów!")
        return

    _, strategy, order, fileStartUp, fileSolution, fileStats = sys.argv

    print(f"Wybrana strategia: {strategy}")
    print(f"Plik startowy: {fileStartUp}")

    if not os.path.exists(fileStartUp):
        print(f"Plik {fileStartUp} nie istnieje.")
        return

    if strategy not in ["bfs", "dfs", "astr"]:
        print("Nieprawidłowa strategia!")
        return

    print("Zaczynam przetwarzanie...")

    if strategy == "astr":
        # Załaduj dane i wykonaj A*
        w, k, puzzle = fileStartUpLoading(fileStartUp)
        #return node.moves, len(node.moves), numerOfVisitedStates, numberOfProcessedStates,  maxDepth, time
        moves, n, visited, processed, maxDepth, time = astr.astar(puzzle, order)

    elif strategy == "bfs":
        # Załaduj dane i wykonaj BFS
        w, k, puzzle = fileStartUpLoading(fileStartUp)
        moves, n, visited, processed, maxDepth, time = bfs.BreadthFirstSearch(puzzle, order)  # Użyj odpowiedniej funkcji z modułu BFS


    elif strategy == "dfs":
        # Załaduj dane i wykonaj DFS
        w, k, puzzle = fileStartUpLoading(fileStartUp)
        moves, n, visited, processed, maxDepth, time = dfs.DepthLimitedSearch(puzzle, 20, order)  # Użyj odpowiedniej funkcji z modułu DFS

    fileSolutionSaving(fileSolution, n, moves)
    saveStaticstc(
        file=fileStats,
        found=n,
        Solutionlength=n,
        Visited=visited,
        processed=processed,
        depth=maxDepth,
        time=time,
    )

if __name__ == "__main__":
    main()
