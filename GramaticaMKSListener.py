# Generated from GramaticaMKS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GramaticaMKSParser import GramaticaMKSParser
else:
    from GramaticaMKSParser import GramaticaMKSParser

# This class defines a complete listener for a parse tree produced by GramaticaMKSParser.
class GramaticaMKSListener(ParseTreeListener):

    # Enter a parse tree produced by GramaticaMKSParser#program.
    def enterProgram(self, ctx:GramaticaMKSParser.ProgramContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#program.
    def exitProgram(self, ctx:GramaticaMKSParser.ProgramContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#statement.
    def enterStatement(self, ctx:GramaticaMKSParser.StatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#statement.
    def exitStatement(self, ctx:GramaticaMKSParser.StatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#assignment.
    def enterAssignment(self, ctx:GramaticaMKSParser.AssignmentContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#assignment.
    def exitAssignment(self, ctx:GramaticaMKSParser.AssignmentContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#printStatement.
    def enterPrintStatement(self, ctx:GramaticaMKSParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#printStatement.
    def exitPrintStatement(self, ctx:GramaticaMKSParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#showGraph.
    def enterShowGraph(self, ctx:GramaticaMKSParser.ShowGraphContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#showGraph.
    def exitShowGraph(self, ctx:GramaticaMKSParser.ShowGraphContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#ifElseStatement.
    def enterIfElseStatement(self, ctx:GramaticaMKSParser.IfElseStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#ifElseStatement.
    def exitIfElseStatement(self, ctx:GramaticaMKSParser.IfElseStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#whileStatement.
    def enterWhileStatement(self, ctx:GramaticaMKSParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#whileStatement.
    def exitWhileStatement(self, ctx:GramaticaMKSParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#forStatement.
    def enterForStatement(self, ctx:GramaticaMKSParser.ForStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#forStatement.
    def exitForStatement(self, ctx:GramaticaMKSParser.ForStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:GramaticaMKSParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:GramaticaMKSParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#functionInvoke.
    def enterFunctionInvoke(self, ctx:GramaticaMKSParser.FunctionInvokeContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#functionInvoke.
    def exitFunctionInvoke(self, ctx:GramaticaMKSParser.FunctionInvokeContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#graphStatement.
    def enterGraphStatement(self, ctx:GramaticaMKSParser.GraphStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#graphStatement.
    def exitGraphStatement(self, ctx:GramaticaMKSParser.GraphStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#graphBarStatement.
    def enterGraphBarStatement(self, ctx:GramaticaMKSParser.GraphBarStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#graphBarStatement.
    def exitGraphBarStatement(self, ctx:GramaticaMKSParser.GraphBarStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#graphScatterStatement.
    def enterGraphScatterStatement(self, ctx:GramaticaMKSParser.GraphScatterStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#graphScatterStatement.
    def exitGraphScatterStatement(self, ctx:GramaticaMKSParser.GraphScatterStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#fileReadStatement.
    def enterFileReadStatement(self, ctx:GramaticaMKSParser.FileReadStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#fileReadStatement.
    def exitFileReadStatement(self, ctx:GramaticaMKSParser.FileReadStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#fileWriteStatement.
    def enterFileWriteStatement(self, ctx:GramaticaMKSParser.FileWriteStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#fileWriteStatement.
    def exitFileWriteStatement(self, ctx:GramaticaMKSParser.FileWriteStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#returnStatement.
    def enterReturnStatement(self, ctx:GramaticaMKSParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#returnStatement.
    def exitReturnStatement(self, ctx:GramaticaMKSParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#sqrtStatement.
    def enterSqrtStatement(self, ctx:GramaticaMKSParser.SqrtStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#sqrtStatement.
    def exitSqrtStatement(self, ctx:GramaticaMKSParser.SqrtStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#sinStatement.
    def enterSinStatement(self, ctx:GramaticaMKSParser.SinStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#sinStatement.
    def exitSinStatement(self, ctx:GramaticaMKSParser.SinStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#cosStatement.
    def enterCosStatement(self, ctx:GramaticaMKSParser.CosStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#cosStatement.
    def exitCosStatement(self, ctx:GramaticaMKSParser.CosStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#tanStatement.
    def enterTanStatement(self, ctx:GramaticaMKSParser.TanStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#tanStatement.
    def exitTanStatement(self, ctx:GramaticaMKSParser.TanStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#inputStatement.
    def enterInputStatement(self, ctx:GramaticaMKSParser.InputStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#inputStatement.
    def exitInputStatement(self, ctx:GramaticaMKSParser.InputStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#arrayAppend.
    def enterArrayAppend(self, ctx:GramaticaMKSParser.ArrayAppendContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#arrayAppend.
    def exitArrayAppend(self, ctx:GramaticaMKSParser.ArrayAppendContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#arrayRemove.
    def enterArrayRemove(self, ctx:GramaticaMKSParser.ArrayRemoveContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#arrayRemove.
    def exitArrayRemove(self, ctx:GramaticaMKSParser.ArrayRemoveContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#arrayPop.
    def enterArrayPop(self, ctx:GramaticaMKSParser.ArrayPopContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#arrayPop.
    def exitArrayPop(self, ctx:GramaticaMKSParser.ArrayPopContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#linearRegression.
    def enterLinearRegression(self, ctx:GramaticaMKSParser.LinearRegressionContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#linearRegression.
    def exitLinearRegression(self, ctx:GramaticaMKSParser.LinearRegressionContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#splitStatement.
    def enterSplitStatement(self, ctx:GramaticaMKSParser.SplitStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#splitStatement.
    def exitSplitStatement(self, ctx:GramaticaMKSParser.SplitStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#countStatement.
    def enterCountStatement(self, ctx:GramaticaMKSParser.CountStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#countStatement.
    def exitCountStatement(self, ctx:GramaticaMKSParser.CountStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#maxStatement.
    def enterMaxStatement(self, ctx:GramaticaMKSParser.MaxStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#maxStatement.
    def exitMaxStatement(self, ctx:GramaticaMKSParser.MaxStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#indexStatement.
    def enterIndexStatement(self, ctx:GramaticaMKSParser.IndexStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#indexStatement.
    def exitIndexStatement(self, ctx:GramaticaMKSParser.IndexStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#intCast.
    def enterIntCast(self, ctx:GramaticaMKSParser.IntCastContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#intCast.
    def exitIntCast(self, ctx:GramaticaMKSParser.IntCastContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#strCast.
    def enterStrCast(self, ctx:GramaticaMKSParser.StrCastContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#strCast.
    def exitStrCast(self, ctx:GramaticaMKSParser.StrCastContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#mlpDefinition.
    def enterMlpDefinition(self, ctx:GramaticaMKSParser.MlpDefinitionContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#mlpDefinition.
    def exitMlpDefinition(self, ctx:GramaticaMKSParser.MlpDefinitionContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#mlpTrain.
    def enterMlpTrain(self, ctx:GramaticaMKSParser.MlpTrainContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#mlpTrain.
    def exitMlpTrain(self, ctx:GramaticaMKSParser.MlpTrainContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#mlpPredict.
    def enterMlpPredict(self, ctx:GramaticaMKSParser.MlpPredictContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#mlpPredict.
    def exitMlpPredict(self, ctx:GramaticaMKSParser.MlpPredictContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#params.
    def enterParams(self, ctx:GramaticaMKSParser.ParamsContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#params.
    def exitParams(self, ctx:GramaticaMKSParser.ParamsContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#args.
    def enterArgs(self, ctx:GramaticaMKSParser.ArgsContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#args.
    def exitArgs(self, ctx:GramaticaMKSParser.ArgsContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#rangeExpr.
    def enterRangeExpr(self, ctx:GramaticaMKSParser.RangeExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#rangeExpr.
    def exitRangeExpr(self, ctx:GramaticaMKSParser.RangeExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#clusteringKMeans.
    def enterClusteringKMeans(self, ctx:GramaticaMKSParser.ClusteringKMeansContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#clusteringKMeans.
    def exitClusteringKMeans(self, ctx:GramaticaMKSParser.ClusteringKMeansContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#mostrarClustering.
    def enterMostrarClustering(self, ctx:GramaticaMKSParser.MostrarClusteringContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#mostrarClustering.
    def exitMostrarClustering(self, ctx:GramaticaMKSParser.MostrarClusteringContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#AndExpr.
    def enterAndExpr(self, ctx:GramaticaMKSParser.AndExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#AndExpr.
    def exitAndExpr(self, ctx:GramaticaMKSParser.AndExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#StringExpr.
    def enterStringExpr(self, ctx:GramaticaMKSParser.StringExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#StringExpr.
    def exitStringExpr(self, ctx:GramaticaMKSParser.StringExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#IndexStmtExpr.
    def enterIndexStmtExpr(self, ctx:GramaticaMKSParser.IndexStmtExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#IndexStmtExpr.
    def exitIndexStmtExpr(self, ctx:GramaticaMKSParser.IndexStmtExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#IntDivExpr.
    def enterIntDivExpr(self, ctx:GramaticaMKSParser.IntDivExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#IntDivExpr.
    def exitIntDivExpr(self, ctx:GramaticaMKSParser.IntDivExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#FloatExpr.
    def enterFloatExpr(self, ctx:GramaticaMKSParser.FloatExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#FloatExpr.
    def exitFloatExpr(self, ctx:GramaticaMKSParser.FloatExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#ArrayPopExpr.
    def enterArrayPopExpr(self, ctx:GramaticaMKSParser.ArrayPopExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#ArrayPopExpr.
    def exitArrayPopExpr(self, ctx:GramaticaMKSParser.ArrayPopExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#ArrayAppendExpr.
    def enterArrayAppendExpr(self, ctx:GramaticaMKSParser.ArrayAppendExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#ArrayAppendExpr.
    def exitArrayAppendExpr(self, ctx:GramaticaMKSParser.ArrayAppendExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#LtExpr.
    def enterLtExpr(self, ctx:GramaticaMKSParser.LtExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#LtExpr.
    def exitLtExpr(self, ctx:GramaticaMKSParser.LtExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#GtExpr.
    def enterGtExpr(self, ctx:GramaticaMKSParser.GtExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#GtExpr.
    def exitGtExpr(self, ctx:GramaticaMKSParser.GtExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#MaxStmtExpr.
    def enterMaxStmtExpr(self, ctx:GramaticaMKSParser.MaxStmtExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#MaxStmtExpr.
    def exitMaxStmtExpr(self, ctx:GramaticaMKSParser.MaxStmtExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#GeExpr.
    def enterGeExpr(self, ctx:GramaticaMKSParser.GeExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#GeExpr.
    def exitGeExpr(self, ctx:GramaticaMKSParser.GeExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#InputStmtExpr.
    def enterInputStmtExpr(self, ctx:GramaticaMKSParser.InputStmtExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#InputStmtExpr.
    def exitInputStmtExpr(self, ctx:GramaticaMKSParser.InputStmtExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#LeExpr.
    def enterLeExpr(self, ctx:GramaticaMKSParser.LeExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#LeExpr.
    def exitLeExpr(self, ctx:GramaticaMKSParser.LeExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#LogicalNot.
    def enterLogicalNot(self, ctx:GramaticaMKSParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#LogicalNot.
    def exitLogicalNot(self, ctx:GramaticaMKSParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#MlpTrainExpr.
    def enterMlpTrainExpr(self, ctx:GramaticaMKSParser.MlpTrainExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#MlpTrainExpr.
    def exitMlpTrainExpr(self, ctx:GramaticaMKSParser.MlpTrainExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#TensorExpr.
    def enterTensorExpr(self, ctx:GramaticaMKSParser.TensorExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#TensorExpr.
    def exitTensorExpr(self, ctx:GramaticaMKSParser.TensorExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#IdentifierExpr.
    def enterIdentifierExpr(self, ctx:GramaticaMKSParser.IdentifierExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#IdentifierExpr.
    def exitIdentifierExpr(self, ctx:GramaticaMKSParser.IdentifierExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#NeqExpr.
    def enterNeqExpr(self, ctx:GramaticaMKSParser.NeqExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#NeqExpr.
    def exitNeqExpr(self, ctx:GramaticaMKSParser.NeqExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#StrCastExpr.
    def enterStrCastExpr(self, ctx:GramaticaMKSParser.StrCastExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#StrCastExpr.
    def exitStrCastExpr(self, ctx:GramaticaMKSParser.StrCastExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#MlpDefinitionExpr.
    def enterMlpDefinitionExpr(self, ctx:GramaticaMKSParser.MlpDefinitionExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#MlpDefinitionExpr.
    def exitMlpDefinitionExpr(self, ctx:GramaticaMKSParser.MlpDefinitionExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#RandomStatementExpr.
    def enterRandomStatementExpr(self, ctx:GramaticaMKSParser.RandomStatementExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#RandomStatementExpr.
    def exitRandomStatementExpr(self, ctx:GramaticaMKSParser.RandomStatementExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#Parentheses.
    def enterParentheses(self, ctx:GramaticaMKSParser.ParenthesesContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#Parentheses.
    def exitParentheses(self, ctx:GramaticaMKSParser.ParenthesesContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#SplitStmtExpr.
    def enterSplitStmtExpr(self, ctx:GramaticaMKSParser.SplitStmtExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#SplitStmtExpr.
    def exitSplitStmtExpr(self, ctx:GramaticaMKSParser.SplitStmtExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#ArrayInvokeExpr.
    def enterArrayInvokeExpr(self, ctx:GramaticaMKSParser.ArrayInvokeExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#ArrayInvokeExpr.
    def exitArrayInvokeExpr(self, ctx:GramaticaMKSParser.ArrayInvokeExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#TanStmtExpr.
    def enterTanStmtExpr(self, ctx:GramaticaMKSParser.TanStmtExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#TanStmtExpr.
    def exitTanStmtExpr(self, ctx:GramaticaMKSParser.TanStmtExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#MlpPredictExpr.
    def enterMlpPredictExpr(self, ctx:GramaticaMKSParser.MlpPredictExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#MlpPredictExpr.
    def exitMlpPredictExpr(self, ctx:GramaticaMKSParser.MlpPredictExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#SqrtStmtExpr.
    def enterSqrtStmtExpr(self, ctx:GramaticaMKSParser.SqrtStmtExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#SqrtStmtExpr.
    def exitSqrtStmtExpr(self, ctx:GramaticaMKSParser.SqrtStmtExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#MultExpr.
    def enterMultExpr(self, ctx:GramaticaMKSParser.MultExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#MultExpr.
    def exitMultExpr(self, ctx:GramaticaMKSParser.MultExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#SubExpr.
    def enterSubExpr(self, ctx:GramaticaMKSParser.SubExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#SubExpr.
    def exitSubExpr(self, ctx:GramaticaMKSParser.SubExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#DotProductExpr.
    def enterDotProductExpr(self, ctx:GramaticaMKSParser.DotProductExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#DotProductExpr.
    def exitDotProductExpr(self, ctx:GramaticaMKSParser.DotProductExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#UnaryMinus.
    def enterUnaryMinus(self, ctx:GramaticaMKSParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#UnaryMinus.
    def exitUnaryMinus(self, ctx:GramaticaMKSParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#AddExpr.
    def enterAddExpr(self, ctx:GramaticaMKSParser.AddExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#AddExpr.
    def exitAddExpr(self, ctx:GramaticaMKSParser.AddExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#ArrayLengthExpr.
    def enterArrayLengthExpr(self, ctx:GramaticaMKSParser.ArrayLengthExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#ArrayLengthExpr.
    def exitArrayLengthExpr(self, ctx:GramaticaMKSParser.ArrayLengthExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#CosStmtExpr.
    def enterCosStmtExpr(self, ctx:GramaticaMKSParser.CosStmtExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#CosStmtExpr.
    def exitCosStmtExpr(self, ctx:GramaticaMKSParser.CosStmtExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#OrExpr.
    def enterOrExpr(self, ctx:GramaticaMKSParser.OrExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#OrExpr.
    def exitOrExpr(self, ctx:GramaticaMKSParser.OrExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#SinStmtExpr.
    def enterSinStmtExpr(self, ctx:GramaticaMKSParser.SinStmtExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#SinStmtExpr.
    def exitSinStmtExpr(self, ctx:GramaticaMKSParser.SinStmtExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#FunctionInvokeExpr.
    def enterFunctionInvokeExpr(self, ctx:GramaticaMKSParser.FunctionInvokeExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#FunctionInvokeExpr.
    def exitFunctionInvokeExpr(self, ctx:GramaticaMKSParser.FunctionInvokeExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#PowerExpr.
    def enterPowerExpr(self, ctx:GramaticaMKSParser.PowerExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#PowerExpr.
    def exitPowerExpr(self, ctx:GramaticaMKSParser.PowerExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#ArrayExpr.
    def enterArrayExpr(self, ctx:GramaticaMKSParser.ArrayExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#ArrayExpr.
    def exitArrayExpr(self, ctx:GramaticaMKSParser.ArrayExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#IntegerExpr.
    def enterIntegerExpr(self, ctx:GramaticaMKSParser.IntegerExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#IntegerExpr.
    def exitIntegerExpr(self, ctx:GramaticaMKSParser.IntegerExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#ArrayRemoveExpr.
    def enterArrayRemoveExpr(self, ctx:GramaticaMKSParser.ArrayRemoveExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#ArrayRemoveExpr.
    def exitArrayRemoveExpr(self, ctx:GramaticaMKSParser.ArrayRemoveExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#ClusteringKMeansExpr.
    def enterClusteringKMeansExpr(self, ctx:GramaticaMKSParser.ClusteringKMeansExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#ClusteringKMeansExpr.
    def exitClusteringKMeansExpr(self, ctx:GramaticaMKSParser.ClusteringKMeansExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#DivExpr.
    def enterDivExpr(self, ctx:GramaticaMKSParser.DivExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#DivExpr.
    def exitDivExpr(self, ctx:GramaticaMKSParser.DivExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#RootExpr.
    def enterRootExpr(self, ctx:GramaticaMKSParser.RootExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#RootExpr.
    def exitRootExpr(self, ctx:GramaticaMKSParser.RootExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#EqExpr.
    def enterEqExpr(self, ctx:GramaticaMKSParser.EqExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#EqExpr.
    def exitEqExpr(self, ctx:GramaticaMKSParser.EqExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#IntCastExpr.
    def enterIntCastExpr(self, ctx:GramaticaMKSParser.IntCastExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#IntCastExpr.
    def exitIntCastExpr(self, ctx:GramaticaMKSParser.IntCastExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#ModExpr.
    def enterModExpr(self, ctx:GramaticaMKSParser.ModExprContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#ModExpr.
    def exitModExpr(self, ctx:GramaticaMKSParser.ModExprContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#arrayInvoke.
    def enterArrayInvoke(self, ctx:GramaticaMKSParser.ArrayInvokeContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#arrayInvoke.
    def exitArrayInvoke(self, ctx:GramaticaMKSParser.ArrayInvokeContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#arrayLength.
    def enterArrayLength(self, ctx:GramaticaMKSParser.ArrayLengthContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#arrayLength.
    def exitArrayLength(self, ctx:GramaticaMKSParser.ArrayLengthContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#randomStatement.
    def enterRandomStatement(self, ctx:GramaticaMKSParser.RandomStatementContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#randomStatement.
    def exitRandomStatement(self, ctx:GramaticaMKSParser.RandomStatementContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#tensor.
    def enterTensor(self, ctx:GramaticaMKSParser.TensorContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#tensor.
    def exitTensor(self, ctx:GramaticaMKSParser.TensorContext):
        pass


    # Enter a parse tree produced by GramaticaMKSParser#arr.
    def enterArr(self, ctx:GramaticaMKSParser.ArrContext):
        pass

    # Exit a parse tree produced by GramaticaMKSParser#arr.
    def exitArr(self, ctx:GramaticaMKSParser.ArrContext):
        pass



del GramaticaMKSParser