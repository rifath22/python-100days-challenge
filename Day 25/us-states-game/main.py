import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S. States Game")
# image = "c:/Users/azabdul2001/Desktop/PythonChallenge/Version 2/Day 25/us-states-game/blank_states_img.gif"
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("./50_states.csv")
# print(data)
# state_list = data['state'].to_list
# print(state_list)
guessed_state = []
score = 0
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="Whats the another state?").title()
    print(answer_state)
    if answer_state == "Exit":
        break
    if answer_state in data.state.values:
        score += 1
        guessed_state.append(answer_state)
        location = data.loc[data['state'] == answer_state]
        x_cor = location.x.values
        y_cor = location.y.values
        # print(f"{x_cor[0]} and its type is: {type(x_cor[0])}")
        tom = turtle.Turtle()
        tom.hideturtle()
        tom.penup()
        tom.goto(x_cor[0], y_cor[0])
        tom.write(answer_state)


# screen.mainloop()
# missed_states = []
# for state in data.state.values:
#     if state not in guessed_state:
#         missed_states.append(state)

missed_states = [state for state in data.state.values if state not in guessed_state]

print(f"missed_states: {missed_states}")
df = pd.DataFrame(missed_states, columns=["states"])
df.to_csv('missed_states.csv', index=False)