import turtle
import csv
import pandas as pd
screen = turtle.Screen()
screen.title("U.S States Game")

# turtle.shape("square")
image = "blank_states_img.gif"
turtle.addshape(image)

turtle.shape(image)
# def get_mouse_click_coor(x, y):
#     print(f"You clicked at {x}, {y}")
# turtle.onscreenclick(get_mouse_click_coor)


data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

correct_states = []  # List to store correct state names

while len(correct_states) < 50:
    # Prompt the user for a state name
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 States Correct",
                                   prompt="Enter a U.S. state name:").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in correct_states:
                missing_states.append(state)
        break

    if answer_state in all_states and answer_state not in correct_states:
        correct_states.append(answer_state)
        state_data = data[data.state == answer_state]
     
    
    state_writer = turtle.Turtle()
    state_writer.hideturtle()
    state_writer.penup()
    state_writer.goto(int(state_data.x), int(state_data.y))
    state_writer.write(state_data.state.item())

#states to learn


# Save the missed states to a CSV file
missed_states_df = pd.DataFrame({"Missed States": missing_states})
missed_states_df.to_csv("missed_states.csv", index=False)




turtle.mainloop() #keep the window open
screen.bye()