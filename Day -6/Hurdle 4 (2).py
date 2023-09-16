def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    turn_left()
    turn_left()
def avoid():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
    turn_left()
    
    
while at_goal()==0:
    if front_is_clear():
        move()
        
    else:
        avoid()
    
    




################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
