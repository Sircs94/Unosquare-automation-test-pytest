class punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def Vercoordenada(self):
        print("x =  ", self.x)
        print("y =  ", self.y)

    def Vercuadrante(self):
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

a = construirPunto()
b = construirPunto()
vector(a,b)