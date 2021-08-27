import sys

# a = 2
# b = "brian"
# c= 2.3
#
# print("Resultados son {0}, {1}, {2} ".format(a,b,c))
#
# print(f"Kanna {a} , {b}, {c}")

if len(sys.argv) == 3:
    text = sys.argv[1]
    repeticion = int(sys.argv[2])
    for i in range(repeticion):
        print(text)
else:
    print("Error: introdujo uno o mas de dos argumentos!")
    print("Aqui esta un ejemplo de como deberia hacerlo?")
    print("Solucion ejemplo: scripts.py 'texto' 3 ")