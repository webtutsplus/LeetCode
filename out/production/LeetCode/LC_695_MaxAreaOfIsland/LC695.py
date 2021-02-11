class LC695(object):
    def maxAreaOfIsland(self, grid):

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
            while len(queue):
                pop = queue.pop(0)
                for neighbours in find_valid_neighbour(pop[0], pop[1]):
                    r, c = neighbours
                    if grid[r][c] == 1 and not visited[r][c]:
                        visited[r][c] = True
                        area += 1
                        queue.append((r, c))
            return area
        #max_area value is our answer . So when we find a point with a value of 1, we do bfs for that point . The returned area is compared with
        #the max_area variable. After the nested for loop, we will return max_area.
        max_area = 0

        for x in range(ROW):
            for y in range(COLUMN):
                if grid[x][y] == 1 and not visited[x][y]:
                    area = bfs(x, y, visited)
                    max_area = max(max_area, area)
        return max_area