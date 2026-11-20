from turtle import *
import winsound

winsound.PlaySound("song.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

bgcolor("Black")
color("violet")
speed(4)

# Draw the flower
for i in range(36):
    circle(100, 90)
    left(90)
    circle(100, 90)
    left(10)

# Draw the stem
penup()
right(90)
forward(100)
pendown()
color("green")
forward(200)

# Move halfway up the stem
penup()
backward(100)
pendown()

# Draw the leaf to the right
right(90)
circle(40, 90)
left(90)
circle(40, 90)

done()