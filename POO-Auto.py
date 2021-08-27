class serie():
    def __init__(self):
        self.formato="Live action"
        self.__episodios=23
        self.actores="Bradd Pitt"
        self.duracion="23 minutos"
        self.nombre="24 Hours"

    def comenzar(self, comenzar_Serie):
        self.empezar=comenzar_Serie
        if(self.empezar):
            return "ya empezaste la serie"
        else:
            return "No has comenzado la serie"

    def __str__(self):
        return "Has comenzado la serie {} cuyo formato es {}, con numero de episodios {} y tiene a {} como actor " \
               "ademas de durar {}  ".format(self.nombre,
            self.formato, self.__episodios, self.actores, self.duracion)

    def __del__(self):
        print("Se ha terminado la serie  {} ".format(self.nombre))

miSerie=serie()
print(str(miSerie))
print(miSerie.comenzar(True))
miSerie.episodios=2344
del(miSerie)