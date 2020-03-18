import turtle

t=turtle.Turtle()

t.shape("turtle")
t.width(5)
t.color("blue")

t.speed(0)

colors = ['red','green','blue','orange','pink']

length= 10;
while length < 500:
    t.forward(length)
    t.color(colors[length%len(colors)])
    length += 3;
    t.left(89)
