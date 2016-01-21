#!/opt/local/bin/python2.7
def valid(pos, grid, r, c):
    (x,y) = pos 
    # Check whether pos is on the grid and not a wall
    return ((0 <= x <= r) and (0 <= y <= c)) and ((grid[x][y] == '-') or \
    (grid[x][y] == '.'))

def reconstruct_path(start, goal, parent):
    # Given a dictionary of parent nodes, reconstruct path taken from start to 
    # gaol by walking backwards 
    pos = goal
    path = [pos]
    while pos != start:
        path.append(parent[pos])
        pos = parent[pos]
    return path[::-1]
    
def bfs(r, c, start, goal, grid):
    visited = [start]
    q = []
    parent = {}
    pos = start    
    while pos != goal:
        (x, y) = pos
        moves = [(x-1, y),(x, y-1),(x, y+1),(x+1, y)]
        for move in moves:
            if valid(move, grid, r, c) and not (move in visited) and \
            not (move in q):
                q.append(move)
                parent[move] = pos
        pos = q.pop(0)
        visited.append(pos)
    path = reconstruct_path(start, goal, parent)
    return (visited, path)

################################################################################
#### Read input  
################################################################################
start = tuple([ int(i) for i in raw_input().strip().split() ])
goal = tuple([ int(i) for i in raw_input().strip().split() ])
r,c = [ int(i) for i in raw_input().strip().split() ]
grid = []
for i in xrange(0, r):
    grid.append(raw_input().strip())

################################################################################
#### Traverse grid and print results
################################################################################
visited, path = bfs(r, c, start, goal, grid)
print len(visited) # Number of nodes explored 
for item in visited:
    print str(item[0])+" "+str(item[1]) # List of all expanded nodes
        
print len(path)-1 # Number of steps from start to gaol
for item in path:
    print str(item[0])+" "+str(item[1]) # Path from start to goal

