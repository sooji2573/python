import turtle

t=turtle.Turtle()

for i in range(10):
    direc = input("왼쪽 L, 오른쪽 R")
    if direc == "L" :
        t.left(90)
        t.forward(100)
    elif direc == "R" :
        t.right(90)
        t.forward(100)
    else :
        print("잘못 입력")
