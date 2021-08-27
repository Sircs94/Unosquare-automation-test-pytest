class Jedi:
    def __init__(self,rango,color_sable,habilidad):
        self.rango=rango
        self.color_sable=color_sable
        self.habilidad=habilidad

    def DatosJedi(self):
        print("El rango del Jedi es: ", self.rango)
        print("Su color de sable es: ", self.color_sable)
        print("Su habilidad principal es: ", self.habilidad)

class Sith:
    def __init__(self,titulo,color_de_sable,habilidad_oscura):
        self.titulo=titulo
        self.color_de_sable=color_de_sable
        self.habilidad_oscura=habilidad_oscura

    def DatosSith(self):
        print("El titulo del Sith es: ", self.titulo)
        print("El color de su sable es: ", self.color_de_sable)
        print("Su habilidad es: ", self.habilidad_oscura)


class Trooper:
    def __init__(self, era, designacion, nombre):
        self.era=era
        self.designacion=designacion
        self.nombre=nombre


    def DatosTrooper(self):
        print("La era del Trooper es: ", self.era)
        print("El rango del trooper es: ", self.designacion)
        print("El nombre del Trooper es", self.nombre)


personaje1 = Jedi("Maestro", "Azul", "Force Healing")
personaje2 = Sith("Lord" , "Rojo" , "Force Choke")
personaje3 = Trooper("Republic", "ARC", "5s")

personaje1.DatosJedi()
personaje2.DatosSith()
personaje3.DatosTrooper()