from turtle import *

# Update window title
title("Fidget Spinner")

state = {'turn': 0}
print("Fidget - Press SPACEBAR to rotate")

def spinner():
    clear()
    angle = state['turn'] / 10
    right(angle)
    
    # Enhanced dots
    for i in range(6):
        forward(100)
        if i % 2 == 0:
            dot(120, 'red')
        else:
            dot(120, 'green')
        back(100)
        right(60)
    
    # Inner circle
    for i in range(6):
        forward(50)
        if i % 2 == 0:
            dot(60, 'blue')
        else:
            dot(60, 'yellow')
        back(50)
        right(60)
    
    update()

def animate():
    if state['turn'] > 0:
        state['turn'] -= 1

    spinner()
    ontimer(animate, 20)

def flick():
    state['turn'] += 20

setup(600, 600, 370, 0)  #the larger window for better view
hideturtle()
tracer(False)
width(10)  #reduced width for a more sleek look
onkey(flick, 'space')
listen()
animate()
done()
