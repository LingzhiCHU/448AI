def outputMaze(maze,search_func,filename):
    path = search_func(maze)
    for i in range(1,len(path)):
        maze[(path[i])[0]][(path[i])[1]] = '.'
    f = open(filename,"w")
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            f.write(maze[i][j])
        f.write('\n')
    f.close()
