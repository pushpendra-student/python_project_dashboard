import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'purple', 'black', 'brown', 'cyan', 'grey']


def get_number_of_turtle():
    racers = 0
    while True:
        racers = input("How many turtle you want to participate (2 -10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print(" invalid Please enter a number!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2-10. Try again!")


def create_turtle(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) +1)
    for i, color in enumerate(colors):  #enumerate func - give the index also give the valu
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        # set pos
        racer.setpos(-WIDTH // 2 + (i+1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles


def race(colors):
    turtles = create_turtle(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")


racers = get_number_of_turtle()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"The winner is thr turtle with color: {winner}")
time.sleep(5)
