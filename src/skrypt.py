import os
import subprocess
import time

# Ścieżki (zmień jeśli trzeba)
input_dir = "input"
output_dir = "output"
program_exec = "program.py"  # użyj 'program.exe' jeśli jesteś na Windowsie

orders = [
    "RDUL", "RDLU", "DRUL", "DRLU",
    "LURD", "LUDR", "ULDR", "ULRD"
]

heuristics = ["hamm", "manh"]
python = "python"

files = sorted(f for f in os.listdir(input_dir) if f.endswith(".txt"))

# Tworzenie folderu głównego i podfolderów
os.makedirs(output_dir, exist_ok=True)
os.makedirs(os.path.join(output_dir, "bfs"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "dfs"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "astr"), exist_ok=True)

total = len(files)
start_global = time.time()

# BFS i DFS
for strat in ["bfs", "dfs"]:
    for order in orders:
        for i, filename in enumerate(files):
            basename = filename.split(".")[0]
            subdir = os.path.join(output_dir, strat)
            sol_file = os.path.join(subdir, f"{basename}_{strat}_{order.lower()}_sol.txt")
            stats_file = os.path.join(subdir, f"{basename}_{strat}_{order.lower()}_stats.txt")

            cmd = [
                python,
                program_exec,
                strat,
                order,
                os.path.join(input_dir, filename),
                sol_file,
                stats_file
            ]
            print(f"[{strat.upper()}-{order}] ({i+1}/{total}): {filename}")
            subprocess.run(cmd)

# A* z heurystykami
for heuristic in heuristics:
    for i, filename in enumerate(files):
        basename = filename.split(".")[0]
        subdir = os.path.join(output_dir, "astr")
        sol_file = os.path.join(subdir, f"{basename}_astr_{heuristic}_sol.txt")
        stats_file = os.path.join(subdir, f"{basename}_astr_{heuristic}_stats.txt")

        cmd = [
            python,
            program_exec,
            "astr",
            heuristic,
            os.path.join(input_dir, filename),
            sol_file,
            stats_file
        ]
        print(f"[A*-{heuristic.upper()}] ({i+1}/{total}): {filename}")
        subprocess.run(cmd)

end_global = time.time()
print(f"\n✅ Wszystkie testy zakończone w {end_global - start_global:.2f} sekundy.")
