def suma(numa, numb):
    return numa+numb

def resta(numa, numb):
    return numa-numb
def division(numa, numb):
    try:
        return numa/numb
    except ZeroDivisionError:
        print("no se puede dividir entre cero")
        return "error"

def multiplica(numa, numb):
    return numa*numb

try:
    num1 = int(input("Dame el primer numero: "))
except Exception as d:
    print("Error, tu input es incorrect: " , type(d).__name__)
try:
    num2 = int(input("Dame el segundo numero: "))
except Exception as d:
    print("Error, tu input es incorrect: " , type(d).__name__)
try:
    operacion = input("¿Que quieres hacer? (sumar, restar, multiplicar, dividir) ")
except Exception as d:
    print("Error, tu input es incorrect: " , type(d).__name__)

if operacion == "sumar":
    print(suma(num1,num2))

elif operacion == "restar":
    print(resta(num1,num2))

elif operacion == "multiplicar":
    print(multiplica(num1,num2))

elif operacion == "dividir":
    print(division(num1,num2))

else:
    print("error")
