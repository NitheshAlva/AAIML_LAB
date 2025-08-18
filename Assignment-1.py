# 1. Simple Grid using lists
grid = [["-" for _ in range(5)] for _ in range(5)]
for row in grid:
    print(" ".join(row))


# 2. Read ASCII grid, find S and list T
ascii_grid = [
    "-----",
    "-S--T",
    "--T--",
    "-----",
]
start = None
tasks = []
for i in range(len(ascii_grid)):
    for j in range(len(ascii_grid[i])):
        if ascii_grid[i][j] == "S":
            start = (i, j)
        elif ascii_grid[i][j] == "T":
            tasks.append((i, j))
print("Start:", start)
print("Tasks:", tasks)


# 3. Number Guessing Game
import random
secret = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print(f"Correct! The number was {secret}. Attempts: {attempts}")
        break
