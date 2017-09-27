def inputMaze(name="mediumMaze.txt"):
    with open(name) as mazeTxt:
    # read every line of the txt file, while ignoring last two chars of each line, since they are line break symbols
        maze = [list(line)[0:-1] for line in mazeTxt]
        rows = len(maze)
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

def DFSBFS(maze,search_method):
    # search_method 0 for dfs
    # 1 for bfs
    height = len(maze)
    width = len(maze[0])

    start = (findStartNGoal(maze))[0]
    goal = (findStartNGoal(maze))[1]

    #set up the matrix for visited matrix
    visited = (height * width) * [False]
    # set up the matrix for the path
    path = (height*width) * [None]

    ele_list = []
    ele_list.insert(0,start)
   
    count = 0 
    #mark as visited
    visited[start[0]*width+start[1]] = True

    while ele_list:
        curr = ele_list.pop()
        count+=1
        if curr == goal:
            break

        neighbors = valid_neighbors(curr,maze,height,width)
        for n in neighbors:
            if n!= None:
                if visited[n[0]*width+n[1]] == False:
                    if search_method == 0: #stack, insert at back
                        ele_list.append(n)
                    else:
                            #bfs(queue), insert at front
                        ele_list.insert(0,n)
                    visited[n[0]*width+n[1]] = True
                    path[n[0]*width+n[1]] = curr

    bookkeeping = []
    curr = goal
    while curr!=None:
        bookkeeping.insert(0,curr)
        curr = path[curr[0]*width+curr[1]]
    #print(count)
    return [bookkeeping,count]

def hn(curr,goal):
    h = abs(goal[0]-curr[0])+abs(goal[1]-curr[1])
    return (h,curr)

def Lowesthn(ele_list,maze,goal):  
    n_list = {}
    for i in range(len(ele_list)):
        m = (hn(ele_list[i],goal))
        n_list.update({m[1]:m[0]})
    s = sorted(n_list, key=n_list.__getitem__)
    return list(s)


def GreedyBestFirst(maze):
    height = len(maze)
    width = len(maze[0])

    start = (findStartNGoal(maze))[0]
    goal = (findStartNGoal(maze))[1]

    #set up the matrix for visited matrix
    visited = (height * width) * [False]
    # set up the matrix for the path
    path = (height*width) * [None]

    ele_list = []
    ele_list.insert(0,start)
   
    count = 0 
    #mark as visited
    visited[start[0]*width+start[1]] = True

    while ele_list:
        # sort the list with respect to hn
        ele_list = Lowesthn(ele_list,maze,goal)
        ele_list.reverse()
        curr = ele_list.pop()
        count+=1
        if curr == goal:
            break
        #print(neighbors)
        neighbors = valid_neighbors(curr,maze,height,width)
        for n in neighbors:
            if n!= None:
                if visited[n[0]*width+n[1]] == False:
                    ele_list.append(n)
                    visited[n[0]*width+n[1]] = True
                    path[n[0]*width+n[1]] = curr

    bookkeeping = []
    curr = goal
    while curr!=None:
        bookkeeping.insert(0,curr)
        curr = path[curr[0]*width+curr[1]]
    #print(goal)
    #print(start)
    return [bookkeeping,count]

def outputMaze(maze,search_method,filename):
    #import time
    #t = time.time()
    if search_method < 2:
        ret = (DFSBFS(maze,search_method))
    else:
        if search_method == 2:
            ret = GreedyBestFirst(maze)
        else:
            ret = Astar(maze) 
    #t = time.time()-t
    path = ret[0]
    mem = ret[1]
    for i in range(1,len(path)):
        maze[(path[i])[0]][(path[i])[1]] = '.'
    f = open(filename,"w")
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            f.write(maze[i][j])
        f.write('\n')
    f.write("cost is %d \n" %(len(path)-1))
    f.write("number of expanded nodes is %d \n"%mem)
    #f.write("time elapsed is %f s" %t)
    f.close()

def fn(curr,goal,cost,width):
    h = abs(curr[0]-goal[0])+abs(curr[1]-goal[1])
    f = h+cost[curr[0]*width+curr[1]]
    #print(f,curr)
    return (f,curr)

def Lowestfn(ele_list,maze,goal,cost,width):
    n_list = {}
    for i in ele_list:
        m = fn(i,goal,cost,width)
        n_list.update({m[1]:m[0]})
    s = sorted(n_list, key=n_list.__getitem__)
    return s

def Astar(maze):
    height = len(maze)
    width = len(maze[0])

    start = (findStartNGoal(maze))[0]
    goal = (findStartNGoal(maze))[1]

    #set up the matrix for visited matrix
    visited = (height * width) * [False]
    # set up the matrix for the path
    path = (height*width) * [None]
    # set up the cost matrix
    cost = (height*width) * [9999]

    ele_list = []
    ele_list.insert(0,start)
   
    count = 0 
    #mark as visited
    visited[start[0]*width+start[1]] = True
    cost[start[0]*width+start[1]] = 0

    while ele_list:
        curr = ele_list.pop()
        count+=1  #count the expansion     
        if curr == goal:
            break
        neighbors = valid_neighbors(curr,maze,height,width)
        #print(neighbors)
        for n in neighbors:
            if n!= None:
                pos = n[0]*width+n[1] 
                if visited[pos] == False:
                    ele_list.insert(0,n)
                    visited[pos] = True
                    c = cost[curr[0]*width+curr[1]]
                    if c+1 < cost[pos]:
                        path[pos] = curr 
                        cost[pos] = c+1
          
        ele_list = Lowestfn(ele_list,maze,goal,cost,width)
        ele_list.reverse()
        #print(ele_list)
        
    bookkeeping = []
    curr = goal
    while curr!=None:
        bookkeeping.insert(0,curr)
        curr = path[curr[0]*width+curr[1]]
    #print(cost)
    #print(start)
    return [bookkeeping,count]

maze = inputMaze("openMaze.txt")
filename0 = "DFS_open"
outputMaze(maze,0,filename0)

maze = inputMaze("openMaze.txt")
filename1 = "BFS_open"
outputMaze(maze,1,filename1)

maze = inputMaze("openMaze.txt")
filename2 = "Greedy_open"
outputMaze(maze,2,filename2)

maze = inputMaze("openMaze.txt")
filename3 = "Astar_open"
outputMaze(maze,3,filename3)


maze = inputMaze("bigMaze.txt")
filename4 = "DFS_big"
outputMaze(maze,0,filename4)

maze = inputMaze("bigMaze.txt")
filename5 = "BFS_big"
outputMaze(maze,1,filename5)

maze = inputMaze("bigMaze.txt")
filename6 = "Greedy_big"
outputMaze(maze,2,filename6)

maze = inputMaze("bigMaze.txt")
filename7 = "Astar_big"
outputMaze(maze,3,filename7)

maze = inputMaze("mediumMaze.txt")
filename8 = "DFS_med"
outputMaze(maze,0,filename8)

maze = inputMaze("mediumMaze.txt")
filename9 = "BFS_med"
outputMaze(maze,1,filename9)

maze = inputMaze("mediumMaze.txt")
filename10 = "Greedy_med"
outputMaze(maze,2,filename10)

maze = inputMaze("mediumMaze.txt")
filename11 = "Astar_med"
outputMaze(maze,3,filename11)