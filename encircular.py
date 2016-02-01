# Complete the function below.


def  doesCircleExist( commands):
    dirs = ['N', 'E', 'S', 'W']
    movement = {}
    for d in dirs:
        movement[d] = 0
        
    dIdx = 0
    direction = 'N'
    for c in commands:
        if c == 'R':
            dIdx += 1
            direction = dirs[dIdx % 4]
        elif c == 'L':
            dIdx -= 1
            direction = dirs[dIdx % 4]
        elif c == 'G':
            #print direction
            movement[direction] += 1
            
    #if (movement['N'] == movement['S']) and (movement['E'] == movement['W']):
        #return "YES"
    #else:
        #return "NO"
        
    if ((movement['N'] != movement['S']) or (movement['E'] != movement['W'])) and (direction == 'N'):
        return "NO"
    else:
        return "YES"
      
