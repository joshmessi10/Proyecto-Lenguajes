from GramaticaMKSVisitor import GramaticaMKSVisitor
from scipy import stats
import numpy as np
import random
import math_ops
import matplotlib
import matplotlib.pyplot as plt
from collections import Counter

matplotlib.use("TkAgg")


class MLP:
    def __init__(self, layer_sizes, learning_rate):
        self.layer_sizes = layer_sizes
        self.learning_rate = learning_rate
        self.weights = [
            np.random.randn(layer_sizes[i], layer_sizes[i + 1])
            for i in range(len(layer_sizes) - 1)
        ]
        self.biases = [np.random.randn(size) for size in layer_sizes[1:]]

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, inputs, outputs, epochs):
        inputs = np.array(inputs)
        outputs = np.array(outputs)
        for _ in range(epochs):
            # Forward pass
            activations = [inputs]
            for w, b in zip(self.weights, self.biases):
                activations.append(self.sigmoid(np.dot(activations[-1], w) + b))

            # Backward pass
            deltas = [outputs - activations[-1]]
            for i in range(len(self.weights) - 1, 0, -1):
                deltas.append(
                    deltas[-1]
                    @ self.weights[i].T
                    * self.sigmoid_derivative(activations[i])
                )

            deltas.reverse()

            # Update weights and biases
            for i in range(len(self.weights)):
                self.weights[i] += activations[i].T @ deltas[i] * self.learning_rate
                self.biases[i] += np.sum(deltas[i], axis=0) * self.learning_rate

    def predict(self, input_data):
        input_data = np.array(input_data)
        for w, b in zip(self.weights, self.biases):
            input_data = self.sigmoid(np.dot(input_data, w) + b)
        return input_data


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

    def visitGraphStatement(self, ctx):
        x_values = self.visit(ctx.expr(0))
        y_values = self.visit(ctx.expr(1))
        if ctx.STRING():
            title = ctx.STRING().getText().strip('"')
            plt.ylim(-10, 10)
            plt.plot(x_values, y_values, label=title)
            plt.legend()
        else:
            plt.ylim(-10, 10)
            plt.plot(x_values, y_values)
        return None

    def visitGraphBarStatement(self, ctx):
        x_values = self.visit(ctx.expr(0))
        y_values = self.visit(ctx.expr(1))
        if ctx.STRING():
            title = ctx.STRING().getText().strip('"')
            plt.title(title)
        plt.bar(x_values, y_values)
        return None

    def visitGraphScatterStatement(self, ctx):
        x_values = self.visit(ctx.expr(0))
        y_values = self.visit(ctx.expr(1))
        if ctx.STRING():
            title = ctx.STRING().getText().strip('"')
            plt.scatter(x_values, y_values, label=title)
            plt.legend()
        else:
            plt.scatter(x_values, y_values)
        return None

    def visitShowGraph(self, ctx):
        plt.show()
        return None

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
        result = random.randint(min_value, max_value)

        # Devuelve el número generado (o imprime, según tu necesidad)
        return result

    def visitSqrtStatement(self, ctx):
        value = self.visit(ctx.expr())
        return value**(1/2)

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
        id_x = ctx.ID(0).getText()
        id_y = ctx.ID(1).getText()
        X = np.array(self.memory[id_x])
        Y = np.array(self.memory[id_y])
        slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
        print(f"Pendiente: {slope}")
        print(f"Intersección: {intercept}")
        print(f"Coeficiente de correlación: {r_value}")
        print(f"Valor p: {p_value}")
        print(f"Error estándar: {std_err}")
        Y_pred = slope * X + intercept
        plt.scatter(X, Y, label="Datos")
        plt.plot(X, Y_pred, color="red", label="Recta de ajuste")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.show()
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

    def visitSqrtStmtExpr(self, ctx):
        return self.visitSqrtStatement(ctx.sqrtStatement())

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
        centroids = random.sample(data, k)

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
                    new_centroids.append(random.choice(data))

            if np.allclose(centroids, new_centroids):
                break

        labels = [
            min(range(k), key=lambda i: self.euclidean_distance(point,
                                                                centroids[i]))
            for point in data
        ]
        self.environment[f"{data_name}_labels"] = labels
        return labels

    def visitMostrarClustering(self, ctx):
        data_name = ctx.ID().getText()
        data = self.environment.get(data_name, [])
        labels = self.environment.get(f"{data_name}_labels", [])
        print("Resultados del Clustering:")
        for point, label in zip(data, labels):
            print(f"Punto: {point}, Cluster: {label}")
