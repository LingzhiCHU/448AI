def readMaze(name = "mediumMaze.txt"):
    f = open("mediumMaze.txt","r")
    message = f.read()
    print(message)
    f.close()

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def heuristic(current,terminate):
    return abs(current[0] - terminate[0]) + abs(current[1] - terminate[1])    
    
    
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


# return a list of all the valid neighbors's index(coordinate)
def valid_neighbors(center, maze, height, width):
    y = center[0]
    x = center[1]
    valid_neighbors = []
    if (x+1) < width and maze[y][x+1] != '%':
        valid_neighbors.append((y,x+1))
    if (x-1) >= 0 and maze[y][x-1] != '%':
        valid_neighbors.append((y,x-1))
    if (y+1) < height and maze[y+1][x] != '%':
        valid_neighbors.append((y+1,x))
    if (y-1) >= 0 and maze[y-1][x] != '%':
        valid_neighbors.append((y-1,x))
    return valid_neighbors