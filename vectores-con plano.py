import turtle as T
import time

class punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def Vercoordenada(self):
        print("x =  ", self.x)
        print("y =  ", self.y)

    def Vercuadrante(self):
        cuadrante=""
        if self.x == 0 and  self.y != 0:
           print("El punto se encuentra en el eje Y ")

        elif self.x != 0 and self.y == 0:
            print("El punto se situa sobre el eje x")

        elif self.x == 0 and self.y == 0:
            print("El punto se encuentra en el origen ")

        elif self.x > 0 and self.y > 0:
            print("El punto se encuentra en el cuadrante 1")

        elif self.x < 0 and self.y > 0:
            print("El punto se encuentra en el cuadrante 2 ")

        elif self.x < 0 and self.y <0:
            print("El punto se encuentra en el cuadrante 3 ")

        elif self.x > 0 and self.y < 0:
            print("El punto se encuentra en el cuadrante 4")




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

def construirPunto():
    punto1=input("Dame la coordenada de las Abscisas (x): ")
    if not punto1:
            punto1=0
    else:
        punto1 = int(punto1)

    punto2=input("Dame la coordenada de las ordenadas (y): ")
    if not punto2:
            punto2=0
    else:
        punto2 = int(punto2)

    print(f"Tu punto es: ({punto1},{punto2})")

    coordenada = punto(punto1,punto2)
    coordenada.Vercoordenada()
    coordenada.Vercuadrante()
    return punto1, punto2

def vector(pun1,pun2):
    print("Obtendras el vector de: ", pun1,pun2)
    i=0
    conjunto = []
    for i in range(2):

        j = pun2[i] - pun1[i]
        conjunto.insert(i,j)

    print(conjunto)
    return conjunto

a = construirPunto()
b = construirPunto()
c = vector(a,b)
construirplano(a,b,c)