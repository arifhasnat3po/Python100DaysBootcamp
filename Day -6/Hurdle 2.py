def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    turn_left()
    turn_left()
def step(): 
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal()==0:
    step()
    
    




################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
