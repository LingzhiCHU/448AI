def bfs(maze):
    height = len(maze)
    width = len(maze[0])

    start = (findStartNGoal(maze))[0]
    goal = (findStartNGoal(maze))[1]

    #set up the matrix for visited matrix
    visited = (height * width) * [False]
    # set up the matrix for the path
    path = (height*width) * [None]

    # use queue for BFS implementation
    # set up the queue

    queue = []
    queue.insert(0,start)
    #mark as visited
    visited[start[0]*width+start[1]] = True


    while queue:
        curr = queue.pop()
        if curr == goal:
            break

        neighbors = valid_neighbors(curr,maze,height,width)
        for n in neighbors:
            if n!= None:
                if visited[n[0]*width+n[1]] == False:
                    queue.insert(0,n);
                    visited[n[0]*width+n[1]] = True
                    path[n[0]*width+n[1]] = curr

    bookkeeping = []
    curr = goal
    while curr!=None:
        bookkeeping.insert(0,curr)
        curr = path[curr[0]*width+curr[1]]

    return bookkeeping

