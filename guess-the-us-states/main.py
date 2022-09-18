import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

# displaying the image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

tim = turtle.Turtle()
tim.penup()
tim.hideturtle()

"""
# now, for the names of the countries to show up, we need the coordinates of the countries
# this can be done by getting the coordinates of mouse clicks over the countries in the map
def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)   
turtle.mainloop()  # makes sure screen remains after code ends
"""

data = pandas.read_csv("50_states.csv")
state_names = data.state.to_list()

correct_guesses = []

while len(correct_guesses) < 50:
    user_answer = screen.textinput(
        title=f"{len(correct_guesses)}/50 States Correct",
        prompt="Name a state :\n'Exit' to save progress",
    ).title()

    if user_answer == "Exit":  # since it is title case
        states_to_learn = [
            state for state in state_names if state not in correct_guesses
        ]  # list comprehension

        df = pandas.DataFrame(states_to_learn)  # list
        df.to_csv("states_to_learn.csv")
        break

    if user_answer in state_names:
        row = data[data.state == user_answer]
        tim.goto(int(row.x), int(row.y))
        tim.write(
            user_answer, align="center", font=("Courier", 8, "normal")
        )  # or data.state.item()
        correct_guesses.append(user_answer)

screen.exitonclick()
