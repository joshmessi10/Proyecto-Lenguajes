# Generated from GramaticaMKS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GramaticaMKSParser import GramaticaMKSParser
else:
    from GramaticaMKSParser import GramaticaMKSParser

# This class defines a complete generic visitor for a parse tree produced by GramaticaMKSParser.

class GramaticaMKSVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GramaticaMKSParser#program.
    def visitProgram(self, ctx:GramaticaMKSParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#statement.
    def visitStatement(self, ctx:GramaticaMKSParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#assignment.
    def visitAssignment(self, ctx:GramaticaMKSParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#printStatement.
    def visitPrintStatement(self, ctx:GramaticaMKSParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#showGraph.
    def visitShowGraph(self, ctx:GramaticaMKSParser.ShowGraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#ifElseStatement.
    def visitIfElseStatement(self, ctx:GramaticaMKSParser.IfElseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#whileStatement.
    def visitWhileStatement(self, ctx:GramaticaMKSParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#forStatement.
    def visitForStatement(self, ctx:GramaticaMKSParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:GramaticaMKSParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#functionInvoke.
    def visitFunctionInvoke(self, ctx:GramaticaMKSParser.FunctionInvokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#graphStatement.
    def visitGraphStatement(self, ctx:GramaticaMKSParser.GraphStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#graphBarStatement.
    def visitGraphBarStatement(self, ctx:GramaticaMKSParser.GraphBarStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#graphScatterStatement.
    def visitGraphScatterStatement(self, ctx:GramaticaMKSParser.GraphScatterStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#fileReadStatement.
    def visitFileReadStatement(self, ctx:GramaticaMKSParser.FileReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#fileWriteStatement.
    def visitFileWriteStatement(self, ctx:GramaticaMKSParser.FileWriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#returnStatement.
    def visitReturnStatement(self, ctx:GramaticaMKSParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#sqrtStatement.
    def visitSqrtStatement(self, ctx:GramaticaMKSParser.SqrtStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#sinStatement.
    def visitSinStatement(self, ctx:GramaticaMKSParser.SinStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#cosStatement.
    def visitCosStatement(self, ctx:GramaticaMKSParser.CosStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#tanStatement.
    def visitTanStatement(self, ctx:GramaticaMKSParser.TanStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#inputStatement.
    def visitInputStatement(self, ctx:GramaticaMKSParser.InputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#arrayAppend.
    def visitArrayAppend(self, ctx:GramaticaMKSParser.ArrayAppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#arrayRemove.
    def visitArrayRemove(self, ctx:GramaticaMKSParser.ArrayRemoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#arrayPop.
    def visitArrayPop(self, ctx:GramaticaMKSParser.ArrayPopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#linearRegression.
    def visitLinearRegression(self, ctx:GramaticaMKSParser.LinearRegressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#splitStatement.
    def visitSplitStatement(self, ctx:GramaticaMKSParser.SplitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#countStatement.
    def visitCountStatement(self, ctx:GramaticaMKSParser.CountStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#maxStatement.
    def visitMaxStatement(self, ctx:GramaticaMKSParser.MaxStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#indexStatement.
    def visitIndexStatement(self, ctx:GramaticaMKSParser.IndexStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#intCast.
    def visitIntCast(self, ctx:GramaticaMKSParser.IntCastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#strCast.
    def visitStrCast(self, ctx:GramaticaMKSParser.StrCastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#mlpDefinition.
    def visitMlpDefinition(self, ctx:GramaticaMKSParser.MlpDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#mlpTrain.
    def visitMlpTrain(self, ctx:GramaticaMKSParser.MlpTrainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#mlpPredict.
    def visitMlpPredict(self, ctx:GramaticaMKSParser.MlpPredictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#params.
    def visitParams(self, ctx:GramaticaMKSParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#args.
    def visitArgs(self, ctx:GramaticaMKSParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#rangeExpr.
    def visitRangeExpr(self, ctx:GramaticaMKSParser.RangeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#clusteringKMeans.
    def visitClusteringKMeans(self, ctx:GramaticaMKSParser.ClusteringKMeansContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#mostrarClustering.
    def visitMostrarClustering(self, ctx:GramaticaMKSParser.MostrarClusteringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#AndExpr.
    def visitAndExpr(self, ctx:GramaticaMKSParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#StringExpr.
    def visitStringExpr(self, ctx:GramaticaMKSParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#IndexStmtExpr.
    def visitIndexStmtExpr(self, ctx:GramaticaMKSParser.IndexStmtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#IntDivExpr.
    def visitIntDivExpr(self, ctx:GramaticaMKSParser.IntDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#FloatExpr.
    def visitFloatExpr(self, ctx:GramaticaMKSParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#ArrayPopExpr.
    def visitArrayPopExpr(self, ctx:GramaticaMKSParser.ArrayPopExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#ArrayAppendExpr.
    def visitArrayAppendExpr(self, ctx:GramaticaMKSParser.ArrayAppendExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#LtExpr.
    def visitLtExpr(self, ctx:GramaticaMKSParser.LtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#GtExpr.
    def visitGtExpr(self, ctx:GramaticaMKSParser.GtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#MaxStmtExpr.
    def visitMaxStmtExpr(self, ctx:GramaticaMKSParser.MaxStmtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#GeExpr.
    def visitGeExpr(self, ctx:GramaticaMKSParser.GeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#InputStmtExpr.
    def visitInputStmtExpr(self, ctx:GramaticaMKSParser.InputStmtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#LeExpr.
    def visitLeExpr(self, ctx:GramaticaMKSParser.LeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#LogicalNot.
    def visitLogicalNot(self, ctx:GramaticaMKSParser.LogicalNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#MlpTrainExpr.
    def visitMlpTrainExpr(self, ctx:GramaticaMKSParser.MlpTrainExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#TensorExpr.
    def visitTensorExpr(self, ctx:GramaticaMKSParser.TensorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#IdentifierExpr.
    def visitIdentifierExpr(self, ctx:GramaticaMKSParser.IdentifierExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#NeqExpr.
    def visitNeqExpr(self, ctx:GramaticaMKSParser.NeqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#StrCastExpr.
    def visitStrCastExpr(self, ctx:GramaticaMKSParser.StrCastExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#MlpDefinitionExpr.
    def visitMlpDefinitionExpr(self, ctx:GramaticaMKSParser.MlpDefinitionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#RandomStatementExpr.
    def visitRandomStatementExpr(self, ctx:GramaticaMKSParser.RandomStatementExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#Parentheses.
    def visitParentheses(self, ctx:GramaticaMKSParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#SplitStmtExpr.
    def visitSplitStmtExpr(self, ctx:GramaticaMKSParser.SplitStmtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#ArrayInvokeExpr.
    def visitArrayInvokeExpr(self, ctx:GramaticaMKSParser.ArrayInvokeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#TanStmtExpr.
    def visitTanStmtExpr(self, ctx:GramaticaMKSParser.TanStmtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#MlpPredictExpr.
    def visitMlpPredictExpr(self, ctx:GramaticaMKSParser.MlpPredictExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#SqrtStmtExpr.
    def visitSqrtStmtExpr(self, ctx:GramaticaMKSParser.SqrtStmtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#MultExpr.
    def visitMultExpr(self, ctx:GramaticaMKSParser.MultExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#SubExpr.
    def visitSubExpr(self, ctx:GramaticaMKSParser.SubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#DotProductExpr.
    def visitDotProductExpr(self, ctx:GramaticaMKSParser.DotProductExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#UnaryMinus.
    def visitUnaryMinus(self, ctx:GramaticaMKSParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#AddExpr.
    def visitAddExpr(self, ctx:GramaticaMKSParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#ArrayLengthExpr.
    def visitArrayLengthExpr(self, ctx:GramaticaMKSParser.ArrayLengthExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#CosStmtExpr.
    def visitCosStmtExpr(self, ctx:GramaticaMKSParser.CosStmtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#OrExpr.
    def visitOrExpr(self, ctx:GramaticaMKSParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#SinStmtExpr.
    def visitSinStmtExpr(self, ctx:GramaticaMKSParser.SinStmtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#FunctionInvokeExpr.
    def visitFunctionInvokeExpr(self, ctx:GramaticaMKSParser.FunctionInvokeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#PowerExpr.
    def visitPowerExpr(self, ctx:GramaticaMKSParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#ArrayExpr.
    def visitArrayExpr(self, ctx:GramaticaMKSParser.ArrayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#IntegerExpr.
    def visitIntegerExpr(self, ctx:GramaticaMKSParser.IntegerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#ArrayRemoveExpr.
    def visitArrayRemoveExpr(self, ctx:GramaticaMKSParser.ArrayRemoveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#ClusteringKMeansExpr.
    def visitClusteringKMeansExpr(self, ctx:GramaticaMKSParser.ClusteringKMeansExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#DivExpr.
    def visitDivExpr(self, ctx:GramaticaMKSParser.DivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#RootExpr.
    def visitRootExpr(self, ctx:GramaticaMKSParser.RootExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#EqExpr.
    def visitEqExpr(self, ctx:GramaticaMKSParser.EqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#IntCastExpr.
    def visitIntCastExpr(self, ctx:GramaticaMKSParser.IntCastExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#ModExpr.
    def visitModExpr(self, ctx:GramaticaMKSParser.ModExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#arrayInvoke.
    def visitArrayInvoke(self, ctx:GramaticaMKSParser.ArrayInvokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#arrayLength.
    def visitArrayLength(self, ctx:GramaticaMKSParser.ArrayLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#randomStatement.
    def visitRandomStatement(self, ctx:GramaticaMKSParser.RandomStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#tensor.
    def visitTensor(self, ctx:GramaticaMKSParser.TensorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaMKSParser#arr.
    def visitArr(self, ctx:GramaticaMKSParser.ArrContext):
        return self.visitChildren(ctx)



del GramaticaMKSParser