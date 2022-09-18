import random
import turtle as t

t.colormode(255)
tim = t.Turtle()
my_screen = t.Screen()
tim.speed("fastest")
tim.hideturtle()


"""
# RANDOM COLORS
# if not hirst painting colors, use this to generate random colors ->
def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# or use
import randomcolor
rand_color = randomcolor.RandomColor()

# and call ->
tim.color(rand_color())
"""


"""
# DEFINE COLORS
# or create a list of many colors and use random to select color
import random
colors = ["blue","red" etc etc using turtle colors]
# and call ->
tim.color(random.choice(colors))
"""


"""
# HIRST COLORS
# to get the hirst colors, run the following script
import colorgram
color_objects = colorgram.extract('hirst.jpg', 30)
colors = []
for color in color_objects:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    tup = (r, g, b)
    colors.append(tup)
"""

hirst_colors = [
    (201, 164, 112),
    (152, 75, 50),
    (221, 201, 138),
    (57, 95, 126),
    (170, 152, 44),
    (138, 31, 20),
    (135, 163, 183),
    (196, 94, 75),
    (49, 121, 88),
    (143, 177, 149),
    (95, 75, 77),
    (76, 39, 32),
    (164, 146, 157),
    (16, 98, 71),
    (232, 176, 165),
    (54, 46, 48),
    (32, 61, 76),
    (22, 83, 89),
    (182, 204, 176),
    (141, 22, 25),
    (86, 147, 127),
    (45, 66, 85),
    (8, 68, 53),
    (177, 94, 97),
    (222, 177, 182),
    (109, 128, 151),
]

# start the motion of the turtle
tim.penup()
tim.setpos(-250, -250)
position = tim.pos()
m = -250
for i in range(10):
    for j in range(10):
        tim.color(random.choice(hirst_colors))
        tim.dot(20)
        tim.forward(50)
    m += 50
    tim.setpos(-250, m)

my_screen.exitonclick()
