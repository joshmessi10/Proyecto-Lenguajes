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

def ln(x, terms=20):
    if x <= 0:
        raise ValueError("ln(x) está definido solo para x > 0")
    k = 0
    while x > 2:
        x = racine(x, 2)
        k += 1
    while x < 0.5:
        x = x * x
        k -= 1
    z = (x - 1) / (x + 1)
    z2 = z * z
    result = 0

    for n in range(terms):
        term = (1 / (2 * n + 1)) * puissance(z, 2 * n + 1)
        result += term

    return 2 * result * puissance(2, k)  # Aproximación ajustada

def log(x, base=10):
    return ln(x) / ln(base)


def racine(x, y):
    return x ** (1 / y)  # Se permite potencia como operador interno

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

def tan(x):
    result = sinus(x)/cosinus(x)
    return result

def abst(x):
    return x if x >= 0 else -x

def somme(a, b):
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

def exp(x, terms=20):
    result = 1
    term = 1
    for i in range(1, terms):
        term *= x / i
        result += term
    return result

def sigmoid(x):
    return 1 / (1 + exp(-x))

def sigmoid_deriv(x):
    sx = sigmoid(x)
    return sx * (1 - sx)

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
    
_A = 1664525
_C = 1013904223
_M = 2**32
_seed = 234235235

def _lcg():
    global _seed
    _seed = (_A * _seed + _C) % _M
    return _seed

def randint( min_val: int, max_val: int) -> int:
    rnd = _lcg()
    return min_val + rnd % (max_val - min_val + 1)
