def inputMaze(name="bigMaze.txt"):
with open(name) as mazeTxt:
	# read every line of the txt file, while ignoring last two chars of each line, since they are line break symbols
    maze = [list(line)[0:-2] for line in mazeTxt]
    rows = len(maze)
    maze[rows-1].append('%')
    maze[rows-1].append('%')
return maze         # returns a 2D array



# returns a list of 2 tuples, first contains index of start point, and the second index of goal point
def findStartNGoal(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'P':
                start = (i,j)
            if maze[i][j] == '.':
                goal = (i,j)
    return [start, goal]