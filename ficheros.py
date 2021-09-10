from io import open
import pickle
#
# fichero = open("miprimerarchivo.txt","w")
# texto = "kanna, hola soy un fichero siendo leido \n Tohru sama \n Elma\n Lucoa\n iruru"
# fichero.write(texto)
# fichero.close
#
# fichero = open("miprimerarchivo.txt","r")
# texto = fichero.read()
# fichero.close()
# print(texto)
#
# fichero = open("miprimerarchivo.txt","r")
# linea = fichero.readlines()
# fichero.close()
# print(linea)
#
# fichero = open("miprimerarchivo.txt","r")
# fichero.seek(10)
# print(fichero.read())
# fichero.close()
#
# fichero = open("miprimerarchivo.txt","r")
# fichero.seek(len(fichero.read())/2)
# print(fichero.read())
# fichero.close()


# fichero = open("miprimerarchivo.txt","w")
# texto = "Hola esto es python"
# fichero.write(texto)
# fichero.close()

lista = ["Maria, Antonio, Kanna, Luis"]
fichero = open("lista_nombre.txt","wb")
pickle.dump(lista,fichero)
fichero.close()

fichero = open("lista_nombre.txt","rb")
lista=pickle.load(fichero)
print(lista)
fichero.close()