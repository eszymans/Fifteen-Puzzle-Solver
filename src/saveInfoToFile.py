import time

def saveStaticstc(file, found, Solutionlength, Visited, processed, depth, time):
    with open(file, "w") as f:
        if found != -1:
            f.write(f"{Solutionlength}\n")
        else:
            f.write(f"Solution has not been founc\n")
        f.write(f"{Visited}\n")
        f.write(f"{processed}\n")
        f.write(f"{depth}\n")
        f.write(f"{time:.6f} \n")