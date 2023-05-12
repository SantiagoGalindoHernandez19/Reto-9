
if __name__ == "__main__":

    P= int(input("Ingrese la cantidad de panes(P): "))
    M= int(input("Ingrese la cantidad de leche (M): "))
    H= int(input("Ingrese la cantidad de huevos (H): "))
    B= int(input("Ingrese la cantidad de leche (B): "))
    FuncionTotal = (lambda P, M, H, B: (P*300),(M*3300)+(H*350)-B)
    print("El dinero a devolver o deber es: ",FuncionTotal)


if __name__ == "__main__":   
  c = int(input("Ingresar valor del prestamo(c): "))
  i = int(input("Ingresar porcentaje tasa de interes(i): "))
  n = int(input("Ingrese la cantidad de meses(n): "))
  tasadeinteres = (lambda i, c:((i * c) / 100) ** n)(c, i , n)

print("El valor del prestamos es de")
  
if __name__ == "__main__":   
    D = int(input("Ingrese el numero de dias: "))
    C = int(input("Ingrese el numero de contagiados actuales: "))
    Total = (lambda D, C : C* (D**2))(D,C)
print("El numero de contagiados despues de tantos dias es de", Total)

