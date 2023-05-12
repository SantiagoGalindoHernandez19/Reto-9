
import time
def factor(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factor(n-1)
    
if __name__ == "__main__":
    num = int(input("Ingrese numero: ")) #pide valores enteros
    p = int(input("potencia: "))
    start_time = time.time()
    result = factor()
    end_time = time.time()
    timer = end_time - start_time
print(timer)