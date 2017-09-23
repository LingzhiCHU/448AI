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
   
    #mark as visited
    visited[start[0]*width+start[1]] = True

    while ele_list:
        curr = ele_list.pop()
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

    return bookkeeping


def outputMaze(maze,search_method,filename):
    path = DFSBFS(maze,search_method)
    for i in range(1,len(path)):
        maze[(path[i])[0]][(path[i])[1]] = '.'
    f = open(filename,"w")
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            f.write(maze[i][j])
        f.write('\n')
    f.close()