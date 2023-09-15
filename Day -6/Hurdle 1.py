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
    
for i in range(6):
    step()
    i+=1

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
