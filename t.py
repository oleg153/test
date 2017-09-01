import turtle
import math

dMap = ["886224",       # 0
        "u8d922",       # 1
        "u88d6216",     # 2
        "u88d6161",     # 3
        "u88d268u2d2",  # 4
        "68486",        # 5
        "u886d422684",  # 6
        "u88d612",      # 7
        "688422u8d6",   # 8
        "688426"        # 9
        ]

turtle.hideturtle()


def write_num(w, h, num):
    def write_dig(d, x, y):
        global dMap

        if d < 0:
            d = 0
        elif d > 9:
            d = 9

        p = dMap[d]
        for i in range(len(p)):
            if p[i] == '1':
                turtle.setpos(turtle.xcor() - w, turtle.ycor() - h)
            elif p[i] == '2':
                turtle.setpos(turtle.xcor() - 0, turtle.ycor() - h)
            elif p[i] == '3':
                turtle.setpos(turtle.xcor() + w, turtle.ycor() - h)
            elif p[i] == '4':
                turtle.setpos(turtle.xcor() - w, turtle.ycor() - 0)
            elif p[i] == '6':
                turtle.setpos(turtle.xcor() + w, turtle.ycor() - 0)
            elif p[i] == '7':
                turtle.setpos(turtle.xcor() - w, turtle.ycor() + h)
            elif p[i] == '8':
                turtle.setpos(turtle.xcor() - 0, turtle.ycor() + h)
            elif p[i] == '9':
                turtle.setpos(turtle.xcor() + w, turtle.ycor() + h)
            elif p[i] == 'u':
                turtle.penup()
            elif p[i] == 'd':
                turtle.pendown()
                # end write_dig

    cx = turtle.xcor()
    cy = turtle.ycor()
    snum = str(num)

    for j in range(len(snum)):
        write_dig(int(snum[j]), cx, cy)
        cx = cx + w + w / 5
        turtle.penup()
        turtle.setpos(cx, cy)
        turtle.pendown()

# end write_num

def main():
    write_num(5, 5, 1234567890)


main()
