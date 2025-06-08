# lib/math_ops.py

def factorial(n):
    if n == 0:
        return 1
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def puissance(x, y):
    res = 1
    for _ in range(y):
        res *= x
    return res

def racine(x, y):
    return x ** (1 / y)  # Se permite potencia como operador interno

def __init__(self, seed=1):
        self.state = seed

def next(self):
    # Algoritmo congruencial lineal (LCG)
    self.state = (1103515245 * self.state + 12345) % (2**31)
    return self.state / (2**31)  # valor entre 0 y 1

def randn(self):
    u1 = self.next()
    u2 = self.next()
    l = -self._ln(u1)  # ln(u1)
    angle = 2 * 3.141592653589793 * u2  # pi aprox
    return self._sqrt(2 * l) * self._cos(angle)

def ln(self, x, terms=10):
    x = (x - 1) / (x + 1)
    result = 0
    for n in range(terms):
        result += (1 / (2 * n + 1)) * (x ** (2 * n + 1))
    return 2 * result

def sinus(x, terms=10):
    result = 0
    for n in range(terms):
        sign = (-1)**n
        result += sign * (x**(2*n+1)) / factorial(2*n+1)
    return result

def cosinus(x, terms=10):
    result = 0
    for n in range(terms):
        sign = (-1)**n
        result += sign * (x**(2*n)) / factorial(2*n)
    return result

def somme(a, b):
    print(matrix(a))
    if matrix(a) and matrix(b) and len(a)==len(b) and len(a[0])==len(b[0]):
        return [[a[i][j]+b[i][j] for j in range(len(a[0]))]for i in range(len(a))]
    else:
        return a + b

def soustraction(a, b):
    if matrix(a) and matrix(b) and len(a)==len(b) and len(a[0])==len(b[0]):
        return [[a[i][j]-b[i][j] for j in range(len(a[0]))]for i in range(len(a))]
    else:
        return a - b

def multiplication(a, b):
    if matrix(a) and type(b)== int:
        return[[a[i][j]*b for j in range(len(a[0]))]for i in range(len(a))]
    elif matrix(b) and type(a)== int:
        return[[b[i][j]*a for j in range(len(b[0]))]for i in range(len(b))]
    else:
        return a * b

def dot(a,b):
    if matrix(a) and matrix(b) and len(a[0])==len(b):
        return [[sum([a[i][k]*b[k][j]for k in range(len(a[0]))])for j in range(len(b[0]))]for i in range(len(a))]
    else:
        return False

def trans(a):
    if matrix(a):
        return [[a[i][j]for i in range(len(a))]for j in range(len(a[0]))]
    
def inv(a):
    n = len(a)

    # Crear matriz identidad del mismo tamaño
    identidad = [[float(i == j) for i in range(n)] for j in range(n)]

    # Copiar la matriz original para no modificarla
    A = [fila[:] for fila in a]

    # Aplicar el método Gauss-Jordan
    for i in range(n):
        # Asegurarse de que el pivote no sea cero
        if A[i][i] == 0:
            for j in range(i + 1, n):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    identidad[i], identidad[j] = identidad[j], identidad[i]
                    break
            else:
                raise ValueError("La matriz no es invertible")

        # Hacer el pivote igual a 1
        pivote = A[i][i]
        for j in range(n):
            A[i][j] /= pivote
            identidad[i][j] /= pivote

        # Hacer ceros en la columna i (menos el pivote)
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(n):
                    A[k][j] -= factor * A[i][j]
                    identidad[k][j] -= factor * identidad[i][j]

    return identidad
def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro non permise")
    return a / b

def modulo(a, b):
    return a % b

def matrix(a):
    if type(a)== list:
        t=type(a[0])
        if t == list:
            for i in a:
                if len(i)!=len(a[0]):
                    return False
                for j in i:
                    if type(j)!= int:
                        return False
            return True
    else:
        return False
