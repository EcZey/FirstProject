turtle.goto(100,-200)

def ciz(kenar,buyukluk):
    for a in range(kenar):
        turtle.forward(buyukluk)
        turtle.right(360/kenar)

for a in range(5):
    turtle.penup()
    xx=random.randint(-200,200)
    yy=random.randint(-200,200)
    turtle.goto(xx,yy)
    turtle.pendown()
    turtle.color(random.choice(renkler))
    b=random.randint(50,200)
    ciz (random.randint(3,7),b)