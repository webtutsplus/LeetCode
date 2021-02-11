class LC1020(object):
    def numEnclaves(self, grid):
        """
         global_ans = 0
        for each one, which are not in boundary
            we can do a BFS
             keep track of number of 1 connected
             if we dont reach the boundary
                increment global_ans
                mark all the points as visited

        """
        #These are the possible directions where we can go,i.e. vertically and horizontally
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        ROW = len(grid)
        # This if condition checks whether the Row is zero or not. If it is 0 then return 0.
        if ROW == 0:
            return 0

        COLUMN = len(grid[0])
        #This if condition checks whether the Column is zero or not. If it is 0 then return 0.
        if COLUMN == 0:
            return 0

        #We create a visited matrix of size equal to the grid to keep track of visited grid locations.
        visited = [[False for i in range(COLUMN) ] for j in range(ROW)]

        #This utility method helps to find valid neighbours for a given point(x,y) i.e. finds all the possible points which can be visited from a given point(x,y)
        def find_valid_neighbour(x, y):
            valid_neighbours = []
            for d in DIRECTIONS:
                r, c = x+ d[0], y + d[1]
                if r >= 0 and r < ROW and c >= 0 and c < COLUMN:
                    valid_neighbours.append((r, c))
            return valid_neighbours
        #This is the bfs method. When we visited a point (x,y) , it marks it as visited and adds it to the queue. Also assign the current area value to 1.
        #we now pop the queue and for valid neighbours , we mark them as visited and increament the area value . Also we add those elements to the queue.
        #We do this process until the queue is empty.
        def bfs(x, y, visited):
            queue = [(x, y)]
            visited[x][y] = True
            area = 1
            #this boolean value basically keeps track whether we have touched the boundary ,
            is_boundary_touched = False
            while len(queue):
                pop = queue.pop(0)
                for neighbours in find_valid_neighbour(pop[0], pop[1]):
                    r, c = neighbours
                    if grid[r][c] == 1 and not visited[r][c]:
                        #So when we reach a boundary we set the boundary set variable as true.
                        if (r == 0 or r == ROW-1) or (c == 0 or c == COLUMN-1):
                            is_boundary_touched = True
                        visited[r][c] = True
                        area += 1
                        queue.append((r, c))
            #if we can reach the boundary then we can walk off the boundary.
            if is_boundary_touched:
                return 0
            #If we don't reach the boundary , then we can return the area as it stores all the land squares from which boundary can not be reached
            return area
        #num_of_enclaves value is our answer . So when we find a point with a value of 1, we do bfs for that point . The returned area is added  with
        #the num_of_enclaves variable. After the nested for loop, we will return num_of_enclaves.
        num_of_enclaves = 0

        for x in range(1, ROW-1):
            for y in range(1, COLUMN-1):
                if grid[x][y] == 1 and not visited[x][y]:
                    #print x, y
                    area = bfs(x, y, visited)
                    num_of_enclaves += area
        return num_of_enclaves

