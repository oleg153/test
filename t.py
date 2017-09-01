import turtle

digiMap = ["886224",  # 0
        "u8d922",  # 1
        "u88d6216",  # 2
        "u88d6161",  # 3
        "u88d268u2d2",  # 4
        "68486",  # 5
        "u886d422684",  # 6
        "u88d612",  # 7
        "688422u8d6",  # 8
        "688426"  # 9
           ]

my_turtle = turtle.Turtle()
my_turtle.hideturtle()


def write_num(w, h, num):
    """

    :rtype: none
    """

    def write_dig(d, x, y):
        global digiMap

        if d < 0:
            d = 0
        elif d > 9:
            d = 9

        p = digiMap[d]
        for i in range(len(p)):
            if p[i] == '1':
                my_turtle.setpos(my_turtle.xcor() - w, my_turtle.ycor() - h)
            elif p[i] == '2':
                my_turtle.setpos(my_turtle.xcor() - 0, my_turtle.ycor() - h)
            elif p[i] == '3':
                my_turtle.setpos(my_turtle.xcor() + w, my_turtle.ycor() - h)
            elif p[i] == '4':
                my_turtle.setpos(my_turtle.xcor() - w, my_turtle.ycor() - 0)
            elif p[i] == '6':
                my_turtle.setpos(my_turtle.xcor() + w, my_turtle.ycor() - 0)
            elif p[i] == '7':
                my_turtle.setpos(my_turtle.xcor() - w, my_turtle.ycor() + h)
            elif p[i] == '8':
                my_turtle.setpos(my_turtle.xcor() - 0, my_turtle.ycor() + h)
            elif p[i] == '9':
                my_turtle.setpos(my_turtle.xcor() + w, my_turtle.ycor() + h)
            elif p[i] == 'u':
                my_turtle.penup()
            elif p[i] == 'd':
                my_turtle.pendown()
                # end write_dig

    cx = my_turtle.xcor()
    cy = my_turtle.ycor()
    snum = str(num)

    for j in range(len(snum)):
        write_dig(int(snum[j]), cx, cy)
        cx = cx + w + w / 5
        my_turtle.penup()
        my_turtle.setpos(cx, cy)
        my_turtle.pendown()


# end write_num

def main():
    write_num(30, 35, 1234567890)


main()
pass
