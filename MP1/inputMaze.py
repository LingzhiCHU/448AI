with open("mediumMaze.txt") as mazeTxt:
    maze = [list(line) for line in mazeTxt]

print(maze[8][8])