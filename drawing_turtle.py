
import turtle
form = turtle.Turtle()
form.shape("turtle")


form.backward(50)
for i in range(3, 11):
    for j in range(i):
        form.forward(100)
        form.left((180/i) * 2)
        form.speed("slow")
        form.color("red")
        form.fillcolor("green")

screen = turtle.Screen()
screen.mainloop()
