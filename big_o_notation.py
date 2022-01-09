#Ley de la suma

def f(n):

    for i in range(n):
        print(i)
    
    for i in range(n):
        print(i)
    
#0(n) + 0(n) = 0(n + n) = 0(2n) = 0(n)

def f(n):

    for i in range(n):
        print(i)

    for i in range(n * n):
        print(i)

#O(n) + 0(n * n) = O(n + n^2) = 0(n^2)



#Ley de la multiplicacion

def f(n):

    for i in range(n):

        for j in range(n):
            print(i, j)

# O(n) * O(n) = O(n * n) = O(n^2)



#Recursividad multiple

def fibonacci(n):

    if n == 0 or n == 1:
        return
    
    return fibonacci(n - 1) + fibonacci(n - 2)

# O(2**n)

