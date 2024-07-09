import turtle
import time
import random
import json

# Move the snake in the desired direction.
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def load_past_high_score():
    filename = "score.json"
    try:
        with open(filename) as file:
            raw_score = json.load(file)
    except FileNotFoundError:
        raw_score = 0
    return raw_score

def save_current_high_score():
    filename = "score.json"
    with open(filename, 'w') as file:
        json.dump(high_score, file, indent=4)

win = turtle.Screen()
win.title("The Snake Game")
win.bgcolor("#16161a")
win.setup(width=600, height=600)
win.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.shapesize(1.2, 1.2, 2)
head.color('yellow', '#7f5af0')
head.penup()
head.goto(0, 100)
head.right(90)
head.direction = "stop"

win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_right, "d")
win.onkeypress(go_left, "a")

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.shapesize(0.6, 0.6)
food.color("#e53170")
food.penup()
food.goto(0, 0)

score = 0
high_score = load_past_high_score()
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 277)
pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Verdana", 15, "normal"))

segments = []
delay = 0.1

while True:
    win.update()
    move()
    time.sleep(delay)

    if head.distance(food) < 15:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Verdana", 15, "normal"))

        color_shop = ["#2cb67d", "#2dfe54", "#730039", "#f682ae", "#f582ae", "#26f7fd"]
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(random.choice(color_shop))
        new_segment.penup()
        segments.append(new_segment)

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        score = 0
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Verdana", 15, "normal"))

        for segment in segments:
            segment.goto(1000, 1000)

        segments = []

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            score = 0
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Verdana", 15, "normal"))

            for segment in segments:
                segment.goto(1000, 1000)

            segments = []

    save_current_high_score()
