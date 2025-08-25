import os
import time
from collections import deque

# Game mapk
game_map = [
    "##########",
    "#________#",
    "#___#____#",
    "#___#__X_#",
    "#___#____#",
    "#________#",
    "#___#_#__#",
    "#_X______#",
    "#____#_X_#",
    "##########",
]

n = 10
x, y = 1, 1
points = 0
max_points = 3

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def neighbors(i, j):
    """Return valid neighbors of a cell."""
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = i + dx, j + dy
        if game_map[nx][ny] != "#":
            yield nx, ny

def bfs(start, goal):
    """Return shortest path (list of positions) from start to goal using BFS."""
    queue = deque([start])
    visited = {start: None}
    while queue:
        cur = queue.popleft()
        if cur == goal:
            # reconstruct path
            path = []
            while cur:
                path.append(cur)
                cur = visited[cur]
            return path[::-1]  # reverse
        for nxt in neighbors(*cur):
            if nxt not in visited:
                visited[nxt] = cur
                queue.append(nxt)
    return []

def find_targets():
    """Find all remaining X positions."""
    targets = []
    for i in range(n):
        for j in range(n):
            if game_map[i][j] == "X":
                targets.append((i, j))
    return targets

def print_board():
    for i in range(n):
        for j in range(n):
            if x == i and y == j:
                print("P", end='')
            else:
                print(game_map[i][j], end='')
        print()

def main():
    global x, y, points, game_map
    steps = 0
    while points < max_points:
        clear_screen()
        print(f"Step - {steps}")
        print(f"Points - {points}")
        print_board()
        time.sleep(0.2)

        # find nearest target
        targets = find_targets()
        if not targets:
            break
        # choose nearest target by BFS distance
        shortest_path = None
        for t in targets:
            path = bfs((x,y), t)
            if path and (shortest_path is None or len(path) < len(shortest_path)):
                shortest_path = path

        # move one step along the shortest path
        if shortest_path and len(shortest_path) > 1:
            x, y = shortest_path[1]

        # check if collected
        if game_map[x][y] == 'X':
            game_map[x] = game_map[x][:y] + '_' + game_map[x][y+1:]
            points += 1

        steps += 1

    clear_screen()
    print(f"Step - {steps}")
    print(f"Points - {points}")
    print_board()
    print("🎉 Game over! All points collected.")

main()
