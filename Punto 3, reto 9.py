
def potencia(a,b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a * potencia(a, b -1)
    
if __name__ == "__main__":
    X = int(input("Ingrese un numero: "))
    Y = int(input("Ingrese la potencia: "))

print("el numero ", str(X), "Elevado a", str(Y), "Es", potencia(X,Y))

