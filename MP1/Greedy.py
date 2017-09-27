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
