def inputMaze(name="mediumMaze.txt"):
	with open(name) as mazeTxt:
	    maze = [list(line) for line in mazeTxt]
	return maze