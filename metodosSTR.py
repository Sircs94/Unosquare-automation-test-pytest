#STR methods

# i = input("Como te llamas? ")
# print("El nombre de la persona es ", i.upper())
#
# i = input("Como te llamas? ")
# print("El nombre de la persona es ", i.lower())
#
# i = input("Como te llamas? ")
# print("El nombre de la persona es ", i.capitalize())
#
# i = input("Como te llamas? ")
# print("El nombre de la persona es ", i.strip()) #devuelve una copia del string sin los espacios al inicio o final
#
# i = input("Como te llamas? ")
# print("El nombre de la persona es ", i.capitalize())

# i = input("Como te llamas? ")
# print("El texto que buscas se encuentra: ", i.count("a"), " veces")

# i = input("Como te llamas? ")
# print("El texto que buscas se encuentra: ", i.find("ame"))

# i = input("Como te llamas? ")
# print(i.isdigit())

# i = input("Dame una frase ")
# print(i.split())

# i = input("Dame una frase ")
# print(i.isalnum())

# i = input("Dame una frase ")
# print(i.isalpha())

    #List (Methods)

# lista = ["ale","kanna","iruru"]
# lista.append("Marquitos")
# print(lista)

# lista = ["ale","kanna","iruru"]
# lista.clear()
# print(lista)

# lista = ["ale","kanna","iruru"]
# lista2 = ["reo","ren","rao"]
# lista.extend(lista2)
# print(lista)

# lista = ["ale","kanna","iruru"]
# lista2 = ["reo","ren","rao"]
# lista.extend(lista2)
# print(lista)

# lista = ["ale","kanna","iruru"]
# print(lista.index("kanna"))

# lista = ["ale","kanna","iruru"]
# lista.insert(0, "kanna2")
# print(lista)

# lista = ["ale","kanna","iruru"]
# lista.insert(0, "kanna2")
# print(lista)

    #Conjuntos

# conjunto1 = set({1,2,3,4,5,6})
# conjunto1.add(22)
# print(conjunto1)

# conjunto1 = set({1,2,3,4,5})
# conjunto2=conjunto1.copy()
# print(conjunto2)

# conjunto1 = set({1,2,3,4,5,6,7})
# conjunto1.discard(1)
# print(conjunto1)

        #Diccionarios:

# diccionario = {
#         "clave1":123,
#         "clave2":"kanna",
#         "clave3":{1,2,3,4,5}
# }
#
# print(type(diccionario["clave3"]))

# diccionario = {
#         "clave1":123,
#         "clave2":"kanna",
#         "clave3":{1,2,3,4,5}
# }
#
# print(diccionario.keys())


# diccionario = {
#         "clave1":123,
#         "clave2":"kanna",
#         "clave3":{1,2,3,4,5}
# }
#
# print(diccionario.values())



# diccionario = {
#         "clave1":123,
#         "clave2":"kanna",
#         "clave3":{1,2,3,4,5}
# }
#
# print(diccionario.items())


diccionario = {
        "clave1":123,
        "clave2":"kanna",
        "clave3":{1,2,3,4,5}
}
for i,c in diccionario.items():
        print(i,c)
# print(diccionario.items())