#!/opt/local/bin/python2.7
def valid(move, grid, r, c):
    if r > move[0] < 0 or c > move[1] < 0: return False
    try:
        state = grid[move[0]][move[1]]
        result = (state == '-') or (state == '.')
    except:
        return False 
    return result

def dfs( r, c, pacman_r, pacman_c, food_r, food_c, grid):
    goal = (food_r, food_c)
    start = (pacman_r, pacman_c) #current position
    
    stack = []
    visited = []
    parent = {}
    
    pos = start
    visited.append(pos)
    
    
    while pos != goal:
        x = pos[0]
        y = pos[1]
        moves = [(x-1, y),(x, y-1),(x, y+1),(x+1, y)]
        for move in moves:
            if valid(move, grid, r, c) and not (move in visited) and not (move in stack):
                stack.append(move)
                parent[move] = pos
        pos = stack.pop()
        visited.append(pos)
        #print str(pos[0]) + " " + str(pos[1])
            
    print len(visited) # number of nodes explored 
    for item in visited:
        print str(item[0])+" "+str(item[1]) # all the nodes we expanded

    path = []
    pos = goal
    path.append(pos) # last move is missing
    
    while pos != start:
        path.append(parent[pos])
        pos = parent[pos]
    
    print len(path)-1 # number of moves is one shorter than number of steps
    for item in path[::-1]:
        print str(item[0])+" "+str(item[1]) # the actual path to the goal
        
pacman_r, pacman_c = [ int(i) for i in raw_input().strip().split() ]
food_r, food_c = [ int(i) for i in raw_input().strip().split() ]
r,c = [ int(i) for i in raw_input().strip().split() ]
grid = []
for i in xrange(0, r):
    grid.append(raw_input().strip())

dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid)

