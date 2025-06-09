from GramaticaMKSVisitor import GramaticaMKSVisitor
import math_ops 
from collections import Counter
import graph



def sigmoid(x):
    return 1 / (1 + math_ops.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class SimpleRandom:
    def __init__(self, seed=1):
        self.state = seed

    def next(self):
        # Algoritmo congruencial lineal (LCG)
        self.state = (1103515245 * self.state + 12345) % (2**31)
        return self.state / (2**31)  # valor entre 0 y 1

    def randn(self):
        # Box-Muller sin math: aproximación usando serie de Taylor
        u1 = self.next()
        u2 = self.next()
        l = -self._ln(u1)  # ln(u1)
        angle = 2 * 3.141592653589793 * u2  # pi aprox
        return self._sqrt(2 * l) * self._cos(angle)

    def _ln(self, x, terms=10):
        # ln usando serie de Taylor para ln(1+x)
        x = (x - 1) / (x + 1)
        result = 0
        for n in range(terms):
            result += (1 / (2 * n + 1)) * (x ** (2 * n + 1))
        return 2 * result

    def _sqrt(self, x, iterations=10):
        guess = x / 2
        for _ in range(iterations):
            guess = (guess + x / guess) / 2
        return guess

    def _cos(self, x, terms=10):
        # coseno por serie de Taylor
        result = 1
        term = 1
        for i in range(1, terms):
            term *= -x * x / ((2 * i - 1) * (2 * i))
            result += term
        return result
    
def linear_regression(X, Y):
    n = len(X)
    sum_x = sum(X)
    sum_y = sum(Y)
    sum_x2 = sum([x * x for x in X])
    sum_xy = sum([X[i] * Y[i] for i in range(n)])

    mean_x = sum_x / n
    mean_y = sum_y / n

    numerator = sum_xy - n * mean_x * mean_y
    denominator = sum_x2 - n * mean_x * mean_x
    slope = numerator / denominator
    intercept = mean_y - slope * mean_x

    print("Pendiente:", slope)
    print("Intersección:", intercept)

    Y_pred = [slope * x + intercept for x in X]
    return Y_pred

class MLP:
    def __init__(self, layer_sizes, learning_rate,seed=1):

        self.layer_sizes = layer_sizes
        self.rand = SimpleRandom(seed)
        self.weights = [[[self.rand.randn()for _ in range(layer_sizes[i]) ]
                         for _ in range(layer_sizes[i + 1])]
                        for i in range(len(layer_sizes) - 1)]
        self.biases = [[self.rand.randn() for _ in range(size)]
                       for size in layer_sizes[1:]]
        self.learning_rate=learning_rate

    def _propagacion(self, entrada):
        activaciones = [entrada]
        entradas_z = []

        for l in range(len(self.weights)):
            capa_entrada = activaciones[-1]
            z = []
            a = []
            for j in range(len(self.weights[l])):
                suma = sum(self.weights[l][j][k] * capa_entrada[k] for k in range(len(capa_entrada))) + self.biases[l][j]
                z.append(suma)
                a.append(sigmoid(suma))
            entradas_z.append(z)
            activaciones.append(a)

        return activaciones, entradas_z

    def _retropropagacion(self, x, y):
        activaciones, entradas_z = self._propagacion(x)
        deltas = [0] * (len(self.layer_sizes) - 1)
        # Cálculo del error en la capa de salida
        salida = activaciones[-1]
        deltas[-1] = [
            (salida[i] - y[i]) * math_ops.sigmoid_deriv(entradas_z[-1][i])
            for i in range(len(y))
        ]

        # Retropropagación del error
        for l in range(len(deltas) - 2, -1, -1):
            deltas[l] = []
            for i in range(self.layer_sizes[l+1]):
                error = sum(
                    deltas[l+1][j] * self.weights[l+1][j][i]
                    for j in range(self.layer_sizes[l+2])
                )
                deltas[l].append(error * math_ops.sigmoid_deriv(entradas_z[l][i]))
                
        # Actualización de pesos y sesgos
        for l in range(len(self.weights)):
            for i in range(len(self.weights[l])):  # neurona actual
                for j in range(len(self.weights[l][i])):  # peso
                    self.weights[l][i][j] -= self.learning_rate * deltas[l][i] * activaciones[l][j]
                self.biases[l][i] -= self.learning_rate * deltas[l][i]

    def train(self,inputs, outputs, epochs):
        for _ in range(epochs):
            for x, y in zip(inputs, outputs):
                self._retropropagacion(x, y)

    def predict(self, input_data):
        salida, _ = self._propagacion(input_data)
        return salida[-1]
  


class MyVisitor(GramaticaMKSVisitor):
    def __init__(self):
        self.memory = {}
        self.functions = {}
        self.mlps = {}
        self.environment = {}

    # -------- Reglas de Inicio --------

    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    def visitStatement(self, ctx):
        return self.visitChildren(ctx)

    # -------- Manejo de Statements --------

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        self.environment[var_name] = value
        return None

    def visitPrintStatement(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return None

    def visitIfElseStatement(self, ctx):
        condition = self.visit(ctx.expr())
        if condition:
            for stmt in ctx.ifBlock:
                self.visit(stmt)
        else:
            if ctx.elseBlock is not None:
                for stmt in ctx.elseBlock:
                    self.visit(stmt)
        return None

    def visitIfStatement(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    def visitElseStatement(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    def visitWhileStatement(self, ctx):
        while self.visit(ctx.expr()):
            for stmt in ctx.statement():
                self.visit(stmt)
        return None

    def visitForStatement(self, ctx):
        start = self.visit(ctx.rangeExpr().expr(0))
        end = int(self.visit(ctx.rangeExpr().expr(1)))
        var_name = ctx.ID().getText()

        for i in range(start, end + 1):
            self.memory[var_name] = i
            for stmt in ctx.statement():
                self.visit(stmt)
        return None

    def visitFunctionDefinition(self, ctx):
        func_name = ctx.ID().getText()
        params = [p.getText() for p in ctx.params().ID()] if ctx.params() else []
        body = ctx.statement()
        self.functions[func_name] = (params, body)
        return None

    def visitFunctionInvoke(self, ctx):
        func_name = ctx.ID().getText()
        args = [self.visit(arg) for arg in ctx.args().expr()] if ctx.args() else []

        if func_name not in self.functions:
            raise ValueError(f"Función '{func_name}' no está definida.")

        params, body = self.functions[func_name]
        local_memory = self.memory.copy()

        for param, arg in zip(params, args):
            self.memory[param] = arg

        return_value = None
        for stmt in body:
            result = self.visit(stmt)
            if result is not None:
                return_value = result
                break

        self.memory = local_memory
        return return_value
    
    def visitGraphsStatement(self, ctx):
        width = 70
        height = 20
        symbol= ctx.SYM().getText().strip('"') if ctx.SYM() else "*"
        canvas = graph.create_canvas(width, height) if "show_graph" not in self.environment.keys() else self.environment["show_graph"]

        if ctx.STRING():  # graphs(x_min, x_max, y_min, y_max, "función")
            x_min = self.visit(ctx.expr(0))
            x_max = self.visit(ctx.expr(1))
            y_min = self.visit(ctx.expr(2))
            y_max = self.visit(ctx.expr(3))
            func_str = ctx.STRING().getText().strip('"')
            # Dibujamos el título antes de graficar
            print("\n")
            graph.draw_title(canvas, func_str)
            self.plot_function(canvas, func_str, x_min, x_max, y_min, y_max,char=symbol)
        else:
            # Recibe puntos
            points_x = self.visit(ctx.expr(0))
            points_y = self.visit(ctx.expr(1))
            x_min, x_max = min(points_x), max(points_x)
            y_min, y_max = min(points_y), max(points_y)
            for x, y in zip(points_x, points_y):
                cx = int((x - x_min) / (x_max - x_min) * (width - 1))
                cy = int((y - y_min) / (y_max - y_min) * (height - 1))  # SIN invertir aquí
                graph.plot_point(canvas, cx, cy,symbol)

        graph.draw_axes(canvas, width, height, x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max)
        self.environment["show_graph"]=canvas
        return None
    


    def plot_function(self, canvas, func_str, x_min, x_max, y_min, y_max, step=0.5,char="*"):
        width = len(canvas[0]) - 6  # ancho útil
        height = len(canvas) - 3    # alto útil

        def safe_eval(expr, x):
            expr = expr.replace("^", "**")
            return eval(expr, {
                "x": x,
                "sin": math_ops.sinus, "cos": math_ops.cosinus, "tan": math_ops.tan, "ln": math_ops.ln,
                "log": math_ops.log, "exp": math_ops.puissance, "sqrt": math_ops.racine,
                "__builtins__": {}
            })

        def to_canvas_coords(x, y):
            canvas_x = int((x - x_min) / (x_max - x_min) * (width - 1))
            canvas_y = int((y_max - y) / (y_max - y_min) * (height - 1))
            canvas_y = (height - 1) - canvas_y
            return canvas_x, canvas_y

        x = x_min
        while x <= x_max:
            try:
                y = safe_eval(func_str, x)
                y_min,y_max
                cx, cy = to_canvas_coords(x, y)
                graph.plot_point(canvas, cx, cy, char)
            except Exception:
                pass
            x += step
    def visitShowGraph(self, ctx):
        graph.draw_canvas(self.environment["show_graph"])
    
    def visitFileReadStatement(self, ctx):
        filename = ctx.STRING().getText().strip('"')
        var_name = ctx.ID().getText()
        with open(filename, "r") as file:
            data = file.read()
        self.memory[var_name] = data
        return None

    def visitFileWriteStatement(self, ctx):
        filename = ctx.STRING().getText().strip('"')
        content = self.visit(ctx.expr())
        with open(filename, "w") as file:
            file.write(str(content))
        return None

    def visitReturnStatement(self, ctx):
        value = self.visit(ctx.expr())
        return value

    def visitRandomStatement(self, ctx):
        # Obtén los valores mínimo y máximo del rango
        min_value = int(ctx.INT(0).getText())  # Primer número entero
        max_value = int(ctx.INT(1).getText())  # Segundo número entero

        # Genera un número aleatorio dentro del rango
        result = math_ops.random.randint(min_value, max_value)

        # Devuelve el número generado (o imprime, según tu necesidad)
        return result

    def visitSqrtStatement(self, ctx):
        value = self.visit(ctx.expr())
        return value**(1/2)
    
    def visitFactStatement(self, ctx):
        value = self.visit(ctx.expr())
        return math_ops.factorial(value)
    
    def visitExpStatement(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return math_ops.puissance(left, right)
    
    def visitRacineStatement(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return math_ops.racine(left, right)
    
    def visitLnStatement(self, ctx):
        value = self.visit(ctx.expr())
        return math_ops.ln(value)
    
    def visitLogStatement(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return math_ops.log(left, right)

    def visitSinStatement(self, ctx):
        value = self.visit(ctx.expr())
        return math_ops.sinus(value)

    def visitCosStatement(self, ctx):
        value = self.visit(ctx.expr())
        return math_ops.cosinus(value)

    def visitTanStatement(self, ctx):
        value = self.visit(ctx.expr())
        return math_ops.sinus(value)/math_ops.cosinus(value)

    def visitInputStatement(self, ctx):
        prompt = ctx.STRING().getText().strip('"')
        return input(prompt)

    def visitArrayAppend(self, ctx):
        arr_name = ctx.ID().getText()
        array = self.memory.get(arr_name, [])
        element = self.visit(ctx.expr())
        array.append(element)
        self.memory[arr_name] = array
        return array

    def visitArrayRemove(self, ctx):
        arr_name = ctx.ID().getText()
        array = self.memory.get(arr_name, [])
        element = self.visit(ctx.expr())
        array.remove(element)
        self.memory[arr_name] = array
        return array

    def visitArrayPop(self, ctx):
        arr_name = ctx.ID().getText()
        array = self.memory.get(arr_name, [])
        if ctx.INT():
            index = int(ctx.INT().getText())
            array.pop(index)
        else:
            array.pop()
        self.memory[arr_name] = array
        return array

    def visitLinearRegression(self, ctx):
        x_var = ctx.ID(0).getText()
        y_var = ctx.ID(1).getText()

        x_values = self.memory[x_var]
        y_values = self.memory[y_var]

        n = len(x_values)
        if n != len(y_values):
            raise ValueError("Las listas deben tener el mismo tamaño.")

        mean_x = sum(x_values) / n
        mean_y = sum(y_values) / n

        # Pendiente y ordenada al origen
        numerador = sum((x_values[i] - mean_x) * (y_values[i] - mean_y) for i in range(n))
        denominador = sum((x_values[i] - mean_x) ** 2 for i in range(n))

        if denominador == 0:
            raise ZeroDivisionError("No se puede dividir por cero en la regresión lineal.")

        a = numerador / denominador
        b = mean_y - a * mean_x

        print(f"Modelo: y = {a:.2f}x + {b:.2f}")
        self.memory['lr_result'] = (a, b)
        return None

    def visitSplitStatement(self, ctx):
        arr_name = ctx.ID().getText()
        string = self.memory.get(arr_name, "")
        if ctx.STRING():
            sep = ctx.STRING().getText().strip('"')  # Eliminar las comillas
            # Interpretar secuencias de escape
            sep = sep.encode("utf-8").decode("unicode_escape")
            splitted = string.split(sep)
        else:
            splitted = string.split()
        return splitted

    def visitCountStatement(self, ctx):
        id_1 = ctx.ID(0).getText()  # Texto a contar
        id_2 = ctx.ID(1).getText()  # Lista elementos
        id_3 = ctx.ID(2).getText()  # Lista frecuencias
        values = self.memory[id_1]
        counter = Counter(values)
        elementos, frecuencias = zip(*counter.items()) if counter else ([], [])
        self.memory[id_2] = list(elementos)
        self.memory[id_3] = list(frecuencias)
        return None

    def visitMaxStatement(self, ctx):
        arr_id = ctx.ID().getText()
        array = self.memory[arr_id]
        return max(array)

    def visitIndexStatement(self, ctx):
        arr_id = ctx.ID().getText()
        array = self.memory[arr_id]
        element = self.visit(ctx.expr())
        return array.index(element)

    def visitIntCast(self, ctx):
        value = self.visit(ctx.expr())
        return int(value)

    def visitStrCast(self, ctx):
        value = self.visit(ctx.expr())
        return str(value)

    # -------- Manejo de Tensors y Arrays --------

    def visitTensor(self, ctx):
        rows = [self.visit(arr) for arr in ctx.arr()]
        return rows

    # -------- Manejo de Expr (según las etiquetas) --------

    def visitUnaryMinus(self, ctx):
        value = self.visit(ctx.expr())
        return -value

    def visitLogicalNot(self, ctx):
        value = self.visit(ctx.expr())
        return not value
    
    def visitTransStatement(self, ctx):
        value = self.visit(ctx.expr())
        return math_ops.trans(value)
    
    def visitInvStatement(self, ctx):
        value = self.visit(ctx.expr())
        return math_ops.inv(value)
    
    def visitPowerExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return math_ops.puissance(left, right)

    def visitRootExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        # Raíz: x ^ y -> x^(1/y)
        if right == 0:
            return float("inf")
        return left ** (1.0 / right)

    def visitMultExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return math_ops.multiplication(left,right)

    def visitDivExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if right == 0:
            raise ZeroDivisionError("División por cero")
        return left / right

    def visitModExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left % right

    def visitIntDivExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return math_ops.division(left,right)

    def visitAddExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return math_ops.somme(left,right)

    def visitSubExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return math_ops.soustraction(left,right)

    def visitEqExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left == right

    def visitNeqExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left != right

    def visitLtExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left < right

    def visitGtExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left > right

    def visitLeExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left <= right

    def visitGeExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left >= right

    def visitAndExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return bool(left) and bool(right)

    def visitOrExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return bool(left) or bool(right)

    def visitDotProductExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return math_ops.dot(left,right)

    def visitParentheses(self, ctx):
        return self.visit(ctx.expr())
    
    def visitArrayGraph(self, ctx):
        return [self.visit(e) for e in ctx.expr()]


    def visitArrayInvoke(self, ctx):
        arrayName = ctx.ID().getText()
        index = self.visit(ctx.expr())  # Esto debería retornar un entero
        # Suponiendo que guardas arrays en un diccionario "memory"
        # con clave=nombre de la variable y valor=lista de Python
        array = self.memory.get(arrayName, None)
        if array is None:
            raise ValueError(
                f"La variable '{arrayName}' no está definida o no es un array."
            )
        if not isinstance(index, int):
            raise ValueError("El índice debe ser un entero.")

        try:
            return array[index]
        except IndexError:
            raise ValueError(f"Índice fuera de rango para '{arrayName}'")

    def visitArrayLengthExpr(self, ctx):
        arr = self.visitArrayLength(ctx.arrayLength())
        return arr

    def visitFunctionInvokeExpr(self, ctx):
        return self.visitFunctionInvoke(ctx.functionInvoke())

    def visitInputStmtExpr(self, ctx):
        return self.visitInputStatement(ctx.inputStatement())

    def visitFactStmtExpr(self, ctx):
        return self.visitFactStatement(ctx.factStatement())

    def visitSqrtStmtExpr(self, ctx):
        return self.visitSqrtStatement(ctx.sqrtStatement())
    
    def visitExpStmtExpr(self, ctx):
        return self.visitExpStatement(ctx.expStatement())
    
    def visitLnStmtExpr(self, ctx):
        return self.visitLnStatement(ctx.lnStatement())
    
    def visitLogStmtExpr(self, ctx):
        return self.visitLogStatement(ctx.logStatement())
    
    def visitRacineStmtExpr(self, ctx):
        return self.visitRacineStatement(ctx.racineStatement())

    def visitSinStmtExpr(self, ctx):
        return self.visitSinStatement(ctx.sinStatement())

    def visitCosStmtExpr(self, ctx):
        return self.visitCosStatement(ctx.cosStatement())

    def visitTanStmtExpr(self, ctx):
        return self.visitTanStatement(ctx.tanStatement())
    
    def visitInvStmtExpr(self, ctx):
        return self.visitInvStatement(ctx.invStatement())
    
    def visitTransStmtExpr(self, ctx):
        return self.visitTransStatement(ctx.transStatement())

    def visitTensorExpr(self, ctx):
        return self.visitTensor(ctx.tensor())

    def visitArrayExpr(self, ctx):
        return self.visitArr(ctx.arr())

    def visitIdentifierExpr(self, ctx):
        var_name = ctx.ID().getText()
        return self.memory.get(var_name, 0)

    def visitIntegerExpr(self, ctx):
        return int(ctx.INT().getText())

    def visitFloatExpr(self, ctx):
        return float(ctx.FLOAT().getText())

    def visitStringExpr(self, ctx):
        return str(ctx.STRING().getText().strip('"'))

    def visitArrayAppendExpr(self, ctx):
        return self.visitArrayAppend(ctx.arrayAppend())

    def visitArrayRemoveExpr(self, ctx):
        return self.visitArrayRemove(ctx.arrayRemove())

    def visitArrayPopExpr(self, ctx):
        return self.visitArrayPop(ctx.arrayPop())

    def visitSplitStmtExpr(self, ctx):
        return self.visitSplitStatement(ctx.splitStatement())

    def visitMaxStmtExpr(self, ctx):
        return self.visitMaxStatement(ctx.maxStatement())

    def visitIndexStmtExpr(self, ctx):
        return self.visitIndexStatement(ctx.indexStatement())

    def visitIntCastExpr(self, ctx):
        return self.visitIntCast(ctx.intCast())

    def visitStrCastExpr(self, ctx):
        return self.visitStrCast(ctx.strCast())

    def visitArrayLength(self, ctx):
        arr = self.visit(ctx.expr())
        return len(arr)

    def visitMlpDefinitionExpr(self, ctx):
        return self.visitMlpDefinition(ctx.mlpDefinition())

    def visitMlpTrainExpr(self, ctx):
        return self.visitMlpTrain(ctx.mlpTrain())

    def visitMlpPredictExpr(self, ctx):
        return self.visitMlpPredict(ctx.mlpPredict())

    def visitClusteringKMeansExpr(self, ctx):
        return self.visitClusteringKMeansExpr(ctx.clusteringKMeans())

    # -------- Manejo de Expr (según las etiquetas) --------

    def visitMlpDefinition(self, ctx):
        mlp_id = ctx.ID().getText()
        layer_sizes = self.visit(ctx.layerSizes)
        learning_rate = float(ctx.learningRate.text)
        if isinstance(layer_sizes, list):
            layer_sizes = [int(x) for x in layer_sizes]
        self.mlps[mlp_id] = MLP(layer_sizes, learning_rate)
        return None

    def visitArr(self, ctx):
        return [self.visit(child) for child in ctx.expr()]

    def visitMlpTrain(self, ctx):
        mlp_id = ctx.ID().getText()
        inputs = self.visit(ctx.input_)
        outputs = self.visit(ctx.output)
        epochs = int(ctx.epochs.text)

        if mlp_id in self.mlps:
            self.mlps[mlp_id].train(inputs, outputs, epochs)
        else:
            raise Exception(f"MLP '{mlp_id}' no está definido.")
        return None

    def visitMlpPredict(self, ctx):
        mlp_id = ctx.ID().getText()
        input_data = self.visit(ctx.input_)

        if mlp_id in self.mlps:
            result = self.mlps[mlp_id].predict(input_data)
            return result
        else:
            raise Exception(f"MLP '{mlp_id}' no está definido.")

    def euclidean_distance(self, point1, point2):
        return sum((x - y) ** 2 for x, y in zip(point1, point2)) ** 0.5

    def visitClusteringKMeans(self, ctx):
        data_name = ctx.ID().getText()  # Identificador del dataset
        k = int(ctx.expr().getText())  # Número de clusters

        # Verifica que los datos existan en el entorno
        if data_name not in self.environment:
            raise KeyError(f"Los datos '{data_name}' no están definidos.")

        data = list(self.environment[data_name])  # Obtiene los datos
        centroids = [data[math_ops.randint(0,len(data))] for _ in range(k)]

        for _ in range(100):  # Iterar hasta la convergencia o 100 iteraciones
            clusters = [[] for _ in range(k)]

            for point in data:
                distances = [
                    self.euclidean_distance(point, centroid)
                    for centroid in centroids
                ]
                closest = distances.index(min(distances))
                clusters[closest].append(point)

            new_centroids = []
            for cluster in clusters:
                if cluster:
                    new_centroids.append(
                        [sum(coord) / len(coord) for coord in zip(*cluster)]
                    )
                else:
                    new_centroids.append(data[math_ops.randint(0,len(data))])

            for i in range(len(centroids)):
                if centroids[i] != new_centroids[i]:
                    break

        labels = [
            min(range(k), key=lambda i: self.euclidean_distance(point,
                                                                centroids[i]))
            for point in data
        ]
        self.environment[f"{data_name}_labels"] = labels
        return labels

    def visitMostrarClustering(self, ctx):
        simbolos=['°','*','+','☼','♦','•']
        width = 70
        height = 20
        canvas = graph.create_canvas(width, height)
        data_name = ctx.ID().getText()
        data = self.environment.get(data_name, [])
        labels = self.environment.get(f"{data_name}_labels", [])
        print("Resultados del Clustering:")
        x_min, x_max = min([pair[0] for pair in data]), max([pair[0] for pair in data])
        y_min, y_max = min([pair[0] for pair in data]), max([pair[0] for pair in data])
        for point, label in zip(data, labels):
            print(f"Punto: {point}, Cluster: {label}")
            cx = int((point[0] - x_min) / (x_max - x_min) * (width - 1))
            cy = int((point[1] - y_min) / (y_max - y_min) * (height - 1))
            graph.plot_point(canvas,cx,cy,char=simbolos[label])
            
        graph.draw_axes(canvas, width, height, x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max)
        graph.draw_canvas(canvas)
