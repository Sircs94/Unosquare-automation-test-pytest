class rectangulo:
    def __init__(self,x1,y1, x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2


    def Vercoordenada(self):
        print("x1 =  ", self.x1)
        print("y1 =  ", self.y1)
        print("x2 =  ", self.x2)
        print("y2 =  ", self.y2)

    def base(self):
        base = self.x2 - self.x1
        if base < 0:

            print("La base del rectangulo es: ", abs(base))
        else:
            print("La base del rectangulo es: ", base)

        return base

    def altura(self):
        altura = self.y2 - self.y1
        if altura < 0:

            print("La altura del rectangulo es: ", abs(altura))
        else:
            print("La altura del rectangulo es: ", altura)

        return altura


    def area(self,bas,alt):
        area = bas*alt
        print("El area del rectangulo es (Base*Altura): ", area)


def construirRectangulo():
    punto1a=input("Dame la coordenada de las Abscisas (x) del primer punto: ")
    if not punto1a:
            punto1a=0
    else:
        punto1a = int(punto1a)

    punto2a=input("Dame la coordenada de las ordenadas (y) del primer punto : ")
    if not punto2a:
            punto2a=0
    else:
        punto2a = int(punto2a)

    punto1b = input("Dame la coordenada de las Abscisas (x) del segundo punto: ")
    if not punto1b:
        punto1b = 0
    else:
        punto1b = int(punto1b)

    punto2b = input("Dame la coordenada de las ordenadas (y) del segundo punto : ")
    if not punto2b:
        punto2b = 0
    else:
        punto2b = int(punto2b)

    print(f"Los puntos del rectangulo son: ({punto1a},{punto2a}), ({punto1b},{punto2b})")

    coordenada = rectangulo(punto1a,punto2a,punto1b,punto2b)
    coordenada.Vercoordenada()
    a= coordenada.base()
    b= coordenada.altura()
    coordenada.area(a,b)
    return punto1a, punto2a, punto1b, punto2b




a = construirRectangulo()