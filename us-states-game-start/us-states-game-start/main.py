import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US states Guess")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"Guess ({len(guessed_states)}/50 guessed)", prompt="Name a US State").title()
    if answer == "Exit":
        missed =[]
        for state in all_states:
            if state not in guessed_states:
                missed.append(state)
        df = pd.DataFrame(missed)
        df.to_csv("states_to_learn.csv")
        break
    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer.title())