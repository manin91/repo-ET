def suma(num1, num2):
    return num1 + num2
def resta(num1, num2):
    return num1 - num2
def opc():
    opc = input("ingrese su opcion: (+, -)")
    return opc
def pedir_numeros():
    num1 = int(input("Ingrese su primer numero"))
    num2 = int(input("ingrese su segundo numero"))
    return num1, num2
def calculadora():
    while True:
        opcion = opc()
        match opcion:
            case "+":
                num1, num2 = pedir_numeros()
                print(suma(num1, num2))
                break
            case "-":
                num1, num2 = pedir_numeros()
                print(resta(num1, num2))
                break
                
calculadora()