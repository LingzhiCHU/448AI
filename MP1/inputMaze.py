def inputMaze(name="mediumMaze.txt"):
    with open(name) as mazeTxt:
        maze = [list(line)[0:-2] for line in mazeTxt]
    return maze