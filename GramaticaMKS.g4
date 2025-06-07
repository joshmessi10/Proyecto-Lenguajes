grammar GramaticaMKS;

// Reglas de inicio
program : statement+ ;

// Reglas de declaración de statements
statement
    : assignment 
    | printStatement
    | ifElseStatement
    | whileStatement
    | forStatement
    | functionDefinition
    | functionInvoke
    | graphStatement
    | graphBarStatement
    | graphScatterStatement
    | fileReadStatement
    | fileWriteStatement
    | returnStatement
    | sqrtStatement
    | sinStatement
    | cosStatement
    | tanStatement
    | invStatement
    | transStatement
    | inputStatement
    | arrayAppend
    | arrayRemove
    | arrayPop
    | linearRegression
    | splitStatement
    | showGraph
    | countStatement
    | maxStatement
    | indexStatement
    | intCast
    | strCast
    | mlpDefinition
    | mlpTrain
    | mlpPredict
    | clusteringKMeans
    | mostrarClustering
    ;

// Reglas específicas de statements
assignment          : 'let' ID '=' expr ';' ;
printStatement      : 'print' '(' expr ')' ';' ;
showGraph           : 'show_graph' '(' ')' ';' ;

ifElseStatement     : 'if' '(' expr ')' '{' ifBlock+=statement* '}'
                    ( 'else' '{' elseBlock+=statement* '}' )? ;

whileStatement      : 'while' '(' expr ')' '{' statement* '}' ;
forStatement        : 'for' '(' ID rangeExpr ')' '{' statement* '}' ;

functionDefinition  : 'function' ID '(' params? ')' '{' statement* '}' ;
functionInvoke      : ID '(' args? ')' ';'? ;

graphStatement      : 'graph' '(' expr ',' expr (',' STRING)? ')' ';' ;
graphBarStatement   : 'graph_bar' '(' expr ',' expr (',' STRING)? ')' ';' ;
graphScatterStatement : 'graph_scatter' '(' expr ',' expr (',' STRING)? ')' ';' ;

fileReadStatement   : 'read_file' '(' STRING ',' ID ')' ';' ;
fileWriteStatement  : 'write_file' '(' STRING ',' expr ')' ';' ;
returnStatement     : 'return' '(' expr ')' ';' ;
sqrtStatement       : 'sqrt' '(' expr ')' ';'? ;
factStatement       : 'factorial' '(' expr ')' ';'? ;
sinStatement        : 'sin' '(' expr ')' ';'? ;
cosStatement        : 'cos' '(' expr ')' ';'? ;
tanStatement        : 'tan' '(' expr ')' ';'? ;
invStatement        : 'inv' '(' expr ')' ';'? ;
transStatement      : 'trans' '(' expr ')' ';'? ;


inputStatement      : 'input' '(' STRING ')' ';'? ;

arrayAppend         : ID '.' 'append' '(' expr ')' ';' ;
arrayRemove         : ID '.' 'remove' '(' expr ')' ';' ;
arrayPop            : ID '.' 'pop' '(' INT? ')' ';' ;

linearRegression    : 'linear_regression' '(' ID ',' ID ')' ';' ;
splitStatement      : ID '.' 'split' '(' STRING? ')' ';'? ;
countStatement      : ID '.' 'count' '(' ID ',' ID ')' ';'? ;
maxStatement        : 'max' '(' ID ')' ';'? ;
indexStatement      : ID '.' 'index' '(' expr ')' ';'? ;

intCast             : 'int' '(' expr ')' ';'? ;
strCast             : 'str' '(' expr ')' ';'? ;

//MLP
mlpDefinition : 'mlp_define' '(' ID ',' layerSizes=arr ',' learningRate=FLOAT ')' ';'? ;
mlpTrain     : 'mlp_train' '(' ID ',' input=arr ',' output=arr ',' epochs=INT ')' ';'? ;
mlpPredict   : 'mlp_predict' '(' ID ',' input=arr ')' ';'? ;

// Definición de parámetros y argumentos
params    : ID (',' ID)* ;
args      : expr (',' expr)* ;
rangeExpr : 'from' expr 'to' expr ;

//Clustering
clusteringKMeans   : 'kmeans' '(' ID ',' expr ')' ';' ;
mostrarClustering  : 'mostrarClustering' '(' ID ')' ;

 

// Regla única para expresión, manejando todas las operaciones
expr
   : '-' expr                                      #UnaryMinus
   | '!' expr                                      #LogicalNot
   | expr '**' expr                                #PowerExpr
   | expr '^' expr                                 #RootExpr
   | expr '*' expr                                 #MultExpr
   | expr '/' expr                                 #DivExpr
   | expr '%' expr                                 #ModExpr
   | expr '//' expr                                #IntDivExpr
   | expr '+' expr                                 #AddExpr
   | expr '-' expr                                 #SubExpr
   | expr '==' expr                                #EqExpr
   | expr '!=' expr                                #NeqExpr
   | expr '<' expr                                 #LtExpr
   | expr '>' expr                                 #GtExpr
   | expr '<=' expr                                #LeExpr
   | expr '>=' expr                                #GeExpr
   | expr '&&' expr                                #AndExpr
   | expr '||' expr                                #OrExpr
   | expr '@' expr                                 #DotProductExpr
   | '(' expr ')'                                  #Parentheses
   | randomStatement                               #RandomStatementExpr
   | arrayInvoke                                   #ArrayInvokeExpr
   | arrayLength                                   #ArrayLengthExpr
   | functionInvoke                                #FunctionInvokeExpr
   | inputStatement                                #InputStmtExpr
   | sqrtStatement                                 #SqrtStmtExpr
   | factStatement                                 #FacttmtExpr
   | sinStatement                                  #SinStmtExpr
   | cosStatement                                  #CosStmtExpr
   | tanStatement                                  #TanStmtExpr
   | invStatement                                  #InvStmtExpr
   | transStatement                                #TransStmtExpr
   | tensor                                        #TensorExpr
   | arr                                           #ArrayExpr
   | ID                                            #IdentifierExpr
   | INT                                           #IntegerExpr
   | FLOAT                                         #FloatExpr
   | STRING                                        #StringExpr
   | arrayAppend                                   #ArrayAppendExpr
   | arrayRemove                                   #ArrayRemoveExpr
   | arrayPop                                      #ArrayPopExpr
   | splitStatement                                #SplitStmtExpr
   | maxStatement                                  #MaxStmtExpr
   | indexStatement                                #IndexStmtExpr
   | intCast                                       #IntCastExpr
   | strCast                                       #StrCastExpr
   | mlpDefinition                                 #MlpDefinitionExpr
   | mlpTrain                                      #MlpTrainExpr
   | mlpPredict                                    #MlpPredictExpr
   | clusteringKMeans                              #ClusteringKMeansExpr
   ;

arrayInvoke         : ID '[' expr ']' ;
arrayLength         : 'length' '(' expr ')' ;
randomStatement      : 'random' '(' INT ',' INT ')';

// Definición de tensores y arreglos
tensor : '[' arr (',' arr)* ']' ;
arr    : '[' (expr)? (',' expr)* ']' ('[' INT ']')? ;

// Tokens léxicos
ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
INT    : '-'? [0-9]+ ;
FLOAT  : '-'? [0-9]+ '.' [0-9]* ;
STRING : '"' .*? '"' ;
WS     : [ \t\r\n]+ -> skip ;
COMMENT: ( '//' ~[\r\n]* | '/*' .*? '*/' ) -> skip ;
