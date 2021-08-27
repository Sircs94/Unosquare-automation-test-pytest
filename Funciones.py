# def suma():
#     x = 10
#     y = 11
#     res = y + x
#     print("tu resultado es ", res)
#
# suma()
#
# def resta():
#     x = 567
#     y = 4
#     z = x-y
#     return z
#
# print(resta())

# def division(numero1, numero2):
#     res = numero1/numero2
#     return res
#
# print(division(40,5))

# def infinito(*args):
#     for args in args:
#         print(args)
#
# infinito("Hola",23,34,56,7,"kanna", [1,2,3,4,5])
#
# def infiniDicc(**kwargs):
#     print(kwargs)
#
# infiniDicc(A = "lalo", B = 2, C = "Loaksj")


#Ejercicio 1

# def nombre():
#     name = input("¿cual es tu nombre? ")
#     print(f"Hola! {name} ¿como estas?")
#
# nombre()

#Ejercicio 2

# def email(direccion):
#     res = direccion
#     print(res)
#     if res.find("@") == -1:
#         print("Invalid email address, you missing the @")
#     else:
#         print("valid Email")
#
# email(input("¿Cual es tu correo?"))

# Ejercicio 3
#
# def infinito(**kwargs):
#     f=0
#     for i in kwargs:
#         kwargs[i] = f
#         f=f+1
#         print(kwargs)
#
# infinito(a=0,b=0,c=0,d=0,e=0,f=0,g=0)

#Ejercicio 4

def pares(*args):
   lista = []
   for i in args:
      if (i % 2) == 0:
          lista.append(i, args[i])

   return lista


print(pares(1,23,43,45,67,89,87,65443,34,56,7,7,65,5,443,5,7,898,9,9,988,7,7,6,55,90,65,667,7788,8,9))