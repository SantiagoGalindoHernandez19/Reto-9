
def Promedio(*args)-> int:
    for nums in args:
        Promedio = ((args[0])+(args[1])+(args[2])+(args[3])+(args[4])) // 5
    return Promedio


if __name__ == "__main__":

    a = int(input("Ingrese numero a: "))
    b = int(input("Ingrese numero b: "))
    c = int(input("Ingrese numero c: "))
    d = int(input("Ingrese numero d: "))
    e = int(input("Ingrese numero e: "))

    print("El promedio de los numeros es",(Promedio(a,b,c,d,e)))



def Carne(*args)-> int:
    for num in args:
        suma = (args[0]*6)+(args[1]*7)+(args[2]*7)
    return suma

if __name__ == "__main__":

    N = int(input("Ingresar cantidad de gallinas "))
    M = int(input("Ingresar cantidad de gallos "))
    K = int(input("Ingresar cantidad de pollitos "))
print("La cantidad total de carne de aves en kilogramos es de",(Carne(N,M,K)))


def CantidadDevolver(*args)-> int:
    for num in args:
        total = ((args[0]*300)+(args[1]*330)+(args[2]*350))-(args[3])
    return total

if __name__ == "__main__":
 
    P= int(input("Ingrese la cantidad de panes(P): "))
    I= int(input("Ingrese la cantidad de leche (M): "))
    H= int(input("Ingrese la cantidad de huevos (H): "))
    B= int(input("Ingrese la cantidad de leche (B): "))
print("El dinero a devolver o deber es",CantidadDevolver(P,I,H,B))

