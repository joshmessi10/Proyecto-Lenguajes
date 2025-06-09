# 📚 Proyecto final: GramaticaMKS

## Integrantes

- Eduardo Hincapie
- Josh Lopez
- Miguel Suarez
- Alejandra Vargas

---

## 📝 Descripción

Este proyecto define un lenguaje de programación basado en una gramática desarrollada con ANTLR4. El lenguaje soporta operaciones matemáticas, manejo de datos, funciones gráficas, manipulación de arrays, procesamiento de archivos, y operaciones de aprendizaje automático. Está diseñado para ser sencillo pero funcional, permitiendo una variedad de aplicaciones prácticas.

## Características Principales

- **Declaraciones:** numeros, variables, strings.
- **Control de flujo:** `if-else`, `while`, `for`, `print`, `return`.
- **Operaciones matemáticas:** suma, resta, potencias, raíces, funciones trigonométricas, valor absoluto, logaritmo natural, logaritmo, modulo etc.
- **Manipulación de arrays:** operaciones como `append`, `remove`, `pop`, `split`, `count`.
- **Manipulación de matrics:** operaciones como `inv`.
- **Funciones gráficas:** generación de gráficas punto a punto, funciones trigonometricas, lineales, cuadráticas, etc.
- **Procesamiento de archivos:** lectura y escritura de archivos.
- **Aprendizaje automático:** definición y entrenamiento de MLP, regresión lineal, y clustering con K-Means.

## Especificación de la gramática
```g4
grammar GramaticaMKS;

//Asiganciones
assignment          : 'let' ID '=' expr ';' ;
printStatement      : 'print' '(' expr ')' ';' ;

//Condicionales
ifElseStatement     : 'if' '(' expr ')' '{' ifBlock+=statement* '}'
                    ( 'else' '{' elseBlock+=statement* '}' )? ;

//Ciclos
whileStatement      : 'while' '(' expr ')' '{' statement* '}' ;
forStatement        : 'for' '(' ID rangeExpr ')' '{' statement* '}' ;

//Funciones
functionDefinition  : 'function' ID '(' params? ')' '{' statement* '}' ;
functionInvoke      : ID '(' args? ')' ';'? ;

//Graficar
graphsStatement     : 'graphs' '(' expr ',' expr ',' expr ',' expr ',' STRING ')' ';'
                    | 'graphs' '(' expr ',' expr (',' STRING)? ')' ';' ;

//Files
fileReadStatement   : 'read_file' '(' STRING ',' ID ')' ';' ;
fileWriteStatement  : 'write_file' '(' STRING ',' expr ')' ';' ;

//Funciones trigonometricas, etc
returnStatement     : 'return' '(' expr ')' ';' ;
sqrtStatement       : 'sqrt' '(' expr ')' ';'? ;
factStatement       : 'factorial' '(' expr ')' ';'? ;
expStatement        : 'exp' '(' expr ',' expr ')' ';'? ;
racineStatement     : 'racine' '(' expr ',' expr ')' ';'? ;
lnStatement         : 'ln' '(' expr ')' ';'? ;
logStatement        : 'log' '(' expr ',' expr ')' ';'? ;
sinStatement        : 'sin' '(' expr ')' ';'? ;
cosStatement        : 'cos' '(' expr ')' ';'? ;
tanStatement        : 'tan' '(' expr ')' ';'? ;

//Matrices
invStatement        : 'inv' '(' expr ')' ';'? ;
transStatement      : 'trans' '(' expr ')' ';'? ;

//Arrays
arrayAppend         : ID '.' 'append' '(' expr ')' ';' ;
arrayRemove         : ID '.' 'remove' '(' expr ')' ';' ;
arrayPop            : ID '.' 'pop' '(' INT? ')' ';' ;
splitStatement      : ID '.' 'split' '(' STRING? ')' ';'? ;
countStatement      : ID '.' 'count' '(' ID ',' ID ')' ';'? ;
maxStatement        : 'max' '(' ID ')' ';'? ;
indexStatement      : ID '.' 'index' '(' expr ')' ';'? ;

//Regresión Lineal
linearRegression    : 'linear_regression' '(' ID ',' ID ')' ';' ;

//MLP
mlpDefinition : 'mlp_define' '(' ID ',' layerSizes=arr ',' learningRate=FLOAT ')' ';'? ;
mlpTrain     : 'mlp_train' '(' ID ',' input=arr ',' output=arr ',' epochs=INT ')' ';'? ;
mlpPredict   : 'mlp_predict' '(' ID ',' input=arr ')' ';'? ;

//Clustering
clusteringKMeans   : 'kmeans' '(' ID ',' expr ')' ';' ;
mostrarClustering  : 'mostrarClustering' '(' ID ')' ;
```

## 🧷 Requerimientos

### Dependencias necesarias

- **ANTLR** (instalable en Linux y macOS)
- **Python** (versión 3 o superior)

### Instalación de ANTLR

1. Instala ANTLR4 siguiendo los siguientes pasos

#### Linux

##### Opción 1:

```sh
sudo apt-get install antlr4
```

##### Opción 2:

```sh
cd /usr/local/lib
sudo curl -O http://www.antlr.org/download/antlr-4.13.1-complete.jar
export CLASSPATH=”.:/usr/local/lib/antlr-4.13.1-complete.jar:$CLASSPATH” 
alias antlr4=’java -Xmx500M -cp “/usr/local/lib/antlr-4.13.1-complete.jar:$CLASSPATH” org.antlr.v4.Tool’
alias grun=’java org.antlr.v4.gui.TestRig’
```


### macOs
Instalar homebrew
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Instalar antlr
```sh
brew install antlr
```

##### Opción 2:

```sh
curl -O https://www.antlr.org/download/antlr-4.13.1-complete.jar
```

Mover el directorio:
```
mv antlr-4.13.1-complete.jar /usr/local/lib/
```

Agregarlo a `PATH` y `CLASSPATH`.
```
nano ~/.zshrc
export CLASSPATH=".:/usr/local/lib/antlr-4.13.1-complete.jar:$CLASSPATH"
alias antlr4='java -jar /usr/local/lib/antlr-4.13.1-complete.jar'
alias grun='java org.antlr.v4.gui.TestRig'
```

Recarga el perfil:
```
source ~/.zshrc
```

# ⚡Como usarlo

1. Clona este repositorio y navega a la carpeta principal del proyecto.

## Opción 1:

Para usar el lenguaje MKS puedes hacerlo ejecutando el script main.py y opcionalmente junto a un archivo con extensions mks.

Para simplificar el proceso de ejecutar un archivo, agregar el siguiente comando a el dotfile de la Shell.

### bash
Descargar el zip en descargas, recuerda estar ubicado en la carpeta de tu proyecto

Dar permisos al sh (ejemplo java.sh)
```
chmod +x setup.sh
```

Ejecutar el sh
```
./setup.sh
```

## Opción 2:

2. Genera los archivos necesarios a partir de la gramática:
   ```bash
   antlr4 -Dlanguage=Python3 -visitor GramaticaMKS.g4
   ```
3. Ejecuta el programa principal:
   ```bash
   python3 main.py input_file.mks
   ```


## Ejemplos de Uso

Este repositorio cuenta con una carpeta denominada `examples` donde se encuentran los siguientes ejemplos y otras ejecuciones prácticas para entender mejor la gramática y hacer uso del lenguaje MKS.

### 1. **Operaciones Matemáticas**

```mks
let numero = int(input("Ingrese un número para operaciones matemáticas: "));

let raiz = sqrt(numero);
let seno = sin(numero);
let coseno = cos(numero);
let tangente = tan(numero);
let raizCubica = numero^3;

print("");
print("Raíz cuadrada de " + str(numero) + " es: " + str(raiz));
print("Seno de " + str(numero) + " es: " + str(seno));
print("Coseno de " + str(numero) + " es: " + str(coseno));
print("Tangente de " + str(numero) + " es: " + str(tangente));
print("Raíz cúbica de " + str(numero) + " es: " + str(raizCubica));
```

**Salida:**

```
Ingrese un número para operaciones matemáticas: 8

Raíz cuadrada de 8 es: 2.8284271247461903
Seno de 8 es: 0.9893582466233818
Coseno de 8 es: -0.14550003380861354
Tangente de 8 es: -6.799711455220379
Raiz cubica de 8 es: 2.0
```

### 2. **Funciones Personalizadas**

```mks
function fact(n) {
    let resultado = 1;
    for (i from 1 to n) {
        let resultado = resultado * i;
    }
    return(resultado);
}

let numero = int(input("Ingrese un número para calcular su factorial: "));

let fact = factorial(numero);

print("El factorial de " + str(numero) + " es: " + str(fact) + ".");
```

**Salida:**

```
Ingrese un número para calcular su factorial: 5
El factorial de 5 es: 120.
```

### 3. **Matriz**

```
let x=[[1,2,3],[1,1,1]];
let y=[[9,8,7],[2,3,4]];
let cuadrado =[
    [4, 7],
    [2, 6]
];
print(x+y);
print(x-y);
print(2*x);
print(cuadrado @ x);
print(inv(cuadrado));
print(trans(cuadrado));
```
**Salida:**

```
[[10, 10, 10], [3, 4, 5]]
[[-8, -6, -4], [-1, -2, -3]]
[[2, 4, 6], [2, 2, 2]]
[[11, 15, 19], [8, 10, 12]]
[[0.6000000000000001, -0.7000000000000001], [-0.2, 0.4]]
[[4, 2], [7, 6]]
```

### 4. **Procesamiento de Archivos**

```mks
read_file("examples/El aguardientoski.txt", contenido);

let lineas = contenido.split("\n");

print("Contando frecuencias de líneas...");
let elementos=[];
let frecuencias=[];
lineas.count(elementos, frecuencias);

let max_freq = max(frecuencias);
let indice = frecuencias.index(max_freq);
let linea_mas_frecuente = elementos[indice];

print("La línea más frecuente es: '" + str(linea_mas_frecuente) + "' con una frecuencia de " + str(max_freq) + ".");

write_file("examples/salida.txt", "La línea más frecuente es: '" + str(linea_mas_frecuente) + "' con una frecuencia de " + str(max_freq) + ".");
```

**Salida:**

Guarda un archivo dentro de la carpeta de examples llamado `salida.txt` la última línea del siguiente bloque, que representa lo que se muestra en consola:

```
Contando frecuencias de líneas...
La línea más frecuente es: 'Sírvame un aguardientoski' con una frecuencia de 5.
```

### 5. **Graficar**

```
graphs([2, 20, 30, 2], [5, 10, 15, 8]);
graphs(-10, 10, -5, 5, "x^2");
graphs(-6.28, 6.28, -1.5, 1.5, "sin(x)");
```
**Salida:**

```
 15 -|                                                                      
     |                                                                     *
     |                                                                      
 13 -|                                                                      
     |                                                                      
     |                                                                      
     |                                                                      
 11 -|                                                                      
     |                                                                      
     |                                                                      
     |                                                                      
  9 -|                                            *                         
     |                                                                      
     |                                                                      
     |                                                                      
  7 -|*                                                                     
     |                                                                      
     |                                                                      
     |                                                                      
  5 -|                                                                      
      ----------------------------------------------------------------------
        2     5      8     10     13     16     19     22     24     27     
                                                                            


  5 -|                              x^2                                     
     |                                                                      
     |                           *             *                            
  3 -|                                                                      
     |                                                                      
     |                                                                      
     |                             *         *                              
  1 -|                                                                      
     |                               *     *                                
     |                                                                      
     |                                * * *                                 
 -1 -|                                                                      
     |                                                                      
     |                                                                      
     |                                                                      
 -3 -|                                                                      
     |                                                                      
     |                                                                      
     |                                                                      
 -5 -|                                                                      
      ----------------------------------------------------------------------
      -10    -8     -6     -4     -2      0      2      4      6      8     
                                                                            


  2 -|                             sin(x)                                   
     |                                                                      
     |                                                                      
  1 -|                                                                      
     |        * *                              * *                          
     |     *                                        *                       
     |             *                        *                               
  0 -|  *                                              *                    
     |                                                                      
     |                *                  *                                  
     |*                                                   *               * 
 -0 -|                                                                      
     |                   *            *                                     
     |                                                      *          *    
     |                              *                                       
 -1 -|                     *                                                
     |                        *  *                             *  *  *      
     |                                                                      
     |                                                                      
 -2 -|                                                                      
      ----------------------------------------------------------------------
       -6    -5     -4     -3     -1      0      1      3      4      5     
                                                                            
```



### 6. Regresión líneal
```
let x = [0, 2, 3, 4];
let y = [2, 4, 6, 8];
linear_regression(x, y);
```

**Salida:**
```
Modelo: y = 1.49x + 1.66
```


### 7. **Aprendizaje Automático con Redes Neuronales Secuenciales con función de activación Sigmoid**

```mks
mlp_define(myMLP, [2, 2, 3, 1], 0.1);

mlp_train(myMLP, [[0, 0], [0, 1], [1, 0], [1, 1]], [[0], [1], [1], [0]], 1000);

let result1 = mlp_predict(myMLP, [0, 0]);
print("Resultado de la predicción para [0, 0]: " + str(result1));

let result2 = mlp_predict(myMLP, [1, 1]);
print("Resultado de la predicción para [1, 1]: " + str(result2));

let result3 = mlp_predict(myMLP, [0, 1]);
print("Resultado de la predicción para [0, 1]: " + str(result3));
```

**Salida:**

```
Resultado de la predicción para [0, 0]: [0.4993827765993156]
Resultado de la predicción para [1, 1]: [0.5010458186179483]
Resultado de la predicción para [0, 1]: [0.5003285924142936]
```
### 8. **Clustering K-Means**

```mks
let data = [
    [1.0, 2.0], [1.1, 2.1], [1.2, 2.2], [1.3, 2.3], [1.4, 2.4],
    [5.0, 6.0], [5.1, 6.1], [5.2, 6.2], [5.3, 6.3], [5.4, 6.4],
    [10.0, 10.0], [10.1, 10.1], [10.2, 10.2], [10.3, 10.3], [10.4, 10.4],
    [15.0, 16.0], [15.1, 16.1], [15.2, 16.2], [15.3, 16.3], [15.4, 16.4]
];

kmeans(data, 4);
mostrarClustering(data);
```

**Salida:**

```
Punto: [1. 2.], Cluster: 1
Punto: [1.1 2.1], Cluster: 1
Punto: [1.2 2.2], Cluster: 0
Punto: [1.3 2.3], Cluster: 0
Punto: [1.4 2.4], Cluster: 0
Punto: [5. 6.], Cluster: 3
Punto: [5.1 6.1], Cluster: 3
Punto: [5.2 6.2], Cluster: 3
Punto: [5.3 6.3], Cluster: 3
Punto: [5.4 6.4], Cluster: 3
Punto: [10. 10.], Cluster: 2
Punto: [10.1 10.1], Cluster: 2
Punto: [10.2 10.2], Cluster: 2
Punto: [10.3 10.3], Cluster: 2
Punto: [10.4 10.4], Cluster: 2
Punto: [15. 16.], Cluster: 2
Punto: [15.1 16.1], Cluster: 2
Punto: [15.2 16.2], Cluster: 2
Punto: [15.3 16.3], Cluster: 2
Punto: [15.4 16.4], Cluster: 2
```
