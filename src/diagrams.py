import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Styl wykresów
sns.set(style="whitegrid")

# --- [1] Wczytanie danych z plików CSV ---
# Zmień ścieżki na odpowiednie jeśli dane są w innych lokalizacjach
bfs_df = pd.read_csv("bfs_stats.csv")
dfs_df = pd.read_csv("dfs_stats.csv")
astr_df = pd.read_csv("astar_stats.csv")

# --- [2] Agregacja danych ---

# Średnie arytmetyczne strategii ogólnie
avg_bfs = bfs_df.groupby(['depth']).mean(numeric_only=True).assign(algorithm='BFS').reset_index()
avg_dfs = dfs_df.groupby(['depth']).mean(numeric_only=True).assign(algorithm='DFS').reset_index()
avg_astar = astr_df.groupby(['depth']).mean(numeric_only=True).assign(algorithm='ASTR').reset_index()
avg_all = pd.concat([avg_bfs, avg_dfs, avg_astar], ignore_index=True)

# Rozbicia wg porządków / heurystyk
bfs_by_order = bfs_df.groupby(['depth', 'order']).mean(numeric_only=True).reset_index()
dfs_by_order = dfs_df.groupby(['depth', 'order']).mean(numeric_only=True).reset_index()
astar_by_heuristic = astr_df.groupby(['depth', 'heuristic']).mean(numeric_only=True).reset_index()

# --- [3] Funkcja pomocnicza do rysowania jednego wykresu ---
def plot_metric_grouped(data, x, y, hue, title, ylabel, hue_title, palette='Set2', save_path=None):
    plt.figure(figsize=(8, 5))
    sns.barplot(data=data, x=x, y=y, hue=hue, palette=palette, errorbar=None)
    plt.title(title, fontsize=12)
    plt.xlabel("Głębokość stanu początkowego", fontsize=10)
    plt.ylabel(ylabel, fontsize=10)
    plt.legend(title=hue_title, fontsize=9, title_fontsize=10, loc='upper left')
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
    plt.show()

# --- [4] Funkcja rysująca wszystkie widoki dla danej metryki ---
def plot_all_metric_views(metric, ylabel, title_prefix, save_prefix=None):
    # Średnie BFS, DFS, A*
    plot_metric_grouped(
        data=avg_all, x='depth', y=metric, hue='algorithm',
        title=f"{title_prefix} – Średnie dla strategii",
        ylabel=ylabel, hue_title="Strategia", palette='Set2',
        save_path=f"{save_prefix}_{metric}_avg.png" if save_prefix else None
    )

    # BFS wg porządków
    plot_metric_grouped(
        data=bfs_by_order, x='depth', y=metric, hue='order',
        title=f"{title_prefix} – BFS wg porządku przeszukiwania",
        ylabel=ylabel, hue_title="Porządek", palette='tab10',
        save_path=f"{save_prefix}_{metric}_bfs_orders.png" if save_prefix else None
    )

    # DFS wg porządków
    plot_metric_grouped(
        data=dfs_by_order, x='depth', y=metric, hue='order',
        title=f"{title_prefix} – DFS wg porządku przeszukiwania",
        ylabel=ylabel, hue_title="Porządek", palette='tab10',
        save_path=f"{save_prefix}_{metric}_dfs_orders.png" if save_prefix else None
    )

    # A* wg heurystyki
    plot_metric_grouped(
        data=astar_by_heuristic, x='depth', y=metric, hue='heuristic',
        title=f"{title_prefix} – A* wg heurystyki",
        ylabel=ylabel, hue_title="Heurystyka", palette='Dark2',
        save_path=f"{save_prefix}_{metric}_astar_heuristics.png" if save_prefix else None
    )

# --- [5] Wywołanie dla wszystkich metryk ---
plot_all_metric_views("solution_length", "Długość rozwiązania", "Długość znalezionego rozwiązania",
                      save_prefix="length")
plot_all_metric_views("visited", "Liczba odwiedzonych stanów", "Liczba odwiedzonych stanów",
                      save_prefix="visited")
plot_all_metric_views("processed", "Liczba przetworzonych stanów", "Liczba przetworzonych stanów",
                      save_prefix="processed")
plot_all_metric_views("max_depth", "Maksymalna głębokość", "Maksymalna głębokość rekursji",
                      save_prefix="depth")
plot_all_metric_views("time", "Czas [s]", "Czas trwania obliczeń",
                      save_prefix="time")
