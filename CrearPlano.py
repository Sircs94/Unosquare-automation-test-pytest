import turtle as T
import time

def construirplano(pun1,pun2,vector):
    T.pensize(5)
    T.forward(300)
    T.back(600)
    T.home()
    T.left(90)
    T.forward(300)
    T.back(600)
    T.penup()
    T.goto(0,301)
    T.write("Y")
    T.goto(301,0)
    T.write("X")
    time.sleep(1)
    x=pun1[0],pun1[1]
    T.goto(x)
    T.write(x, font=("Arial",10,"normal"))
    time.sleep(1)
    T.dot(5)
    y = pun2[0],pun2[1]
    T.goto(y)
    T.write(y, font=("Arial", 10, "normal"))
    time.sleep(1)
    T.dot(5)


    if pun1[0] <= pun2[0]:
       T.penup()
       T.goto(x)
       T.pendown()
       T.right(90)
       T.pensize(1)
       difx = pun2[0] - pun1[0]
       T.forward(difx)
       time.sleep(1)
       if pun1[1] <= pun2[1]:
          T.left(90)
          dify = pun2[1] - pun1[1]
          T.forward(dify)
          time.sleep(2)
          T.pencolor("red")
          T.goto(x)
          T.penup()
          T.goto(0,350)
          text = "El vector es: ", vector
          T.write(text, font=("Arial",15,"normal"))
          time.sleep(3)
       else:
           T.right(90)
           dify = pun1[1] + abs(pun2[1])
           T.forward(dify)
           time.sleep(1)
           T.pencolor("red")
           T.goto(x)
           T.penup()
           T.goto(0, 350)
           text = "El vector es: ", vector
           T.write(text, font=("Arial", 15, "normal"))
           time.sleep(3)

    if pun1[0] > pun2[0]:
       T.penup()
       T.goto(x)
       T.pendown()
       T.left(90)
       T.pensize(1)
       difx = abs(pun2[0] - pun1[0])
       T.forward(difx)
       time.sleep(1)
       if pun1[1] <= pun2[1]:
          T.right(90)
          dify = pun2[1] - pun1[1]
          T.forward(dify)
          time.sleep(2)
          T.pencolor("red")
          T.goto(x)
          T.penup()
          T.goto(0, 350)
          text = "El vector es: ", vector
          T.write(text, font=("Arial", 15, "normal"))
          time.sleep(3)
       else:
           T.left(90)
           dify = pun1[1] + abs(pun2[1])
           T.forward(dify)
           time.sleep(1)
           T.pencolor("red")
           T.goto(x)
           T.penup()
           T.goto(0, 350)
           text = "El vector es: ", vector
           T.write(text, font=("Arial", 15, "normal"))
           time.sleep(3)
