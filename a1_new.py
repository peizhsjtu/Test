"""
CSSE1001 2019s2a1
"""

from a1_support import *


#global size
#size = level_size(level)
#level = load_level(filename)
# Write the expected functions here
def get_position_in_direction(position, direction):

    x , y = position

    if direction == 'r':
        position =  x+1, y 
    elif direction == 'l':
        position = x-1, y 
    elif direction == 'u':
        position = x, y+1
    elif direction == 'd':
        position = x, y-1
    return position

def get_tile_at_position(level,position):
    size = level_size(level)
    index = position_to_index(position, size)
    return level[index]

def get_tile_in_direction(level, position, direction):
    position = get_position_in_direction(position, direction)
    index = position_to_index(position, size)
    return level[index]
    
def remove_from_level(level,position):
    index = position_to_index(position, size)
    size = level_size(level)
    level=  level[ : index] + ' ' + level[index+1: ]
    return level

def move(level, position, direction):
    which = get_tile_in_direction(level, position, direction)
    position = get_position_in_direction(position, direction)
    if which == '#':
        tempDirection = 'u'
        tempPosition = get_position_in_direction(position, tempDirection) 
        position = tempPosition
#        position = get_position_in_direction(position, direction) 
    elif which == ' ':
        tempDirection = 'd'
#        tempPosition = get_position_in_direction(position, tempDirection) 
#        tempPosition = get_position_in_direction(position, direction)         
        if get_tile_in_direction(level, position, tempDirection) == ' ':
           position =  get_position_in_direction(position, tempDirection)
#        else:
#            position = tempPosition
    return position
#    if dirction == 'r'
#        if (which == "#") and (get_tile_in_direction(level, newPosition, 'u') == " "):    
#            postion = get_position_in_direction(newPosition, direction)
#        elif (which == " ") and (:

#            if level(position_to_index(temp, size)) == " ":
#            break
#    prePosition = position
#    preIndex = position_to_index(position, size)
#    x, y  = get_position_in_direction(position, direction)
#    size = level_size(level)
#    index = position_to_index(position, size)
#    while level[index] != '#':
#        y += 1
#        if level[index] == ' ':
#            return x,y
#        for line in level:
#            while level[index-len(line)] == ' ':
#                y -= 1
#                if  level[index-len(line)] != ' ':
#                    return position.tuple()


def print_level(level,position):
    size = level_size(level)
    index = position_to_index(position, size)
    level = level[ : index] + '*' + level[index+1: ]
    print(level)

def attack(level, position):
    size = level_size(level)
#    index = position_to_index(position, size)
    direction1 = 'r'
    direction2 = 'l'
    position1 = get_position_in_direction(position, direction1)
    print("position1: ", position1)
    position2 = get_position_in_direction(position, direction2)
    print("position2: ", position2)
    index1 = position_to_index(position1, size)
    index2 = position_to_index(position1, size)
    if level[index2] == '@' :
        print('Attacking the monster on your right!')
        level=level[:index2]+ ' '+level[index2+1:]
        return level
    elif level[index2] == '@':
        print('Attacking the monster on your left')
        level=level[:index1]+' '+level[index1+1:]
        return level
    else:
        print('No monsters to attack!')
        return level

def tile_status(level, position):
    
    size = level_size(level)
    index = position_to_index(position, size)
    if level[index]== 'I':
        print('Congratulations!You finished the level.')
    elif level[index]=='@':
        print('Hit a momster!')
    elif level[index]== '$' or '^':
        level = level[ : index] + ' ' + level[index+1: ]
    return (level[index],level)
    

def main():
    filename = input("Please enter the name of the level file(e.g. level1.txt):")
    Score = 0
    global size
    level = load_level(filename)
    position = (0, 1)
    size = level_size(level)
    index = position_to_index(position, size)
    print("index", position_to_index(position, size))  
    print('Score:' + str(Score))
    print_level(level, position)

    while True:
        action = input("Please enter an action(enter'?')for help:")
        direction = str(action)
        print("action: ", action)
#        which = get_tile_in_direction(level, position, direction)
#        if which = " ":
#            position = get_position_in_direction(position, direction)
#        elif which = "#" and dirction == 
        status = tile_status(level, position)
#        print("index", position_to_index(position, size))       
        if action == '?':
            print(HELP_TEXT)
            print('Score:' + str(Score))
            print_level(level, position)
            
        elif action == 'r' or action == 'l' or action == 'u' or action == 'd':
#            print("position: ", position)
            oldIndex = position_to_index(position, size)
#            print("oldIndex:", oldIndex)  
#            print(level[oldIndex])
            newPosition = move(level, position, direction)
#            print("new position: ", newPosition)
            level = level[ : oldIndex] + ' ' + level[oldIndex+1: ]            
            index = position_to_index(newPosition, size)
            position = newPosition
            
            print(index)
            if level[index] == '@' :
                break
            elif level[index] == 'I':
                print("Congradulations!You failed")
                break
            elif level[index] == '$':
                Score += 1
            
            level = level[ : index] + '*' + level[index+1: ]  
            print('Score:'+str(Score))
            print_level(level, position)
                
        elif action == 'a':
#            print("temmmmmp")
            level = attack(level, position)
            print('Score:' + str(Score))
            print_level(level, position)
        
        elif direction == 'q':
            break 
        
if __name__ == "__main__":
    main()
