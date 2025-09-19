# Generated from WhileLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WhileLangParser import WhileLangParser
else:
    from WhileLangParser import WhileLangParser

# This class defines a complete listener for a parse tree produced by WhileLangParser.
class WhileLangListener(ParseTreeListener):

    # Enter a parse tree produced by WhileLangParser#program.
    def enterProgram(self, ctx:WhileLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by WhileLangParser#program.
    def exitProgram(self, ctx:WhileLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by WhileLangParser#statement.
    def enterStatement(self, ctx:WhileLangParser.StatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#statement.
    def exitStatement(self, ctx:WhileLangParser.StatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#declaration.
    def enterDeclaration(self, ctx:WhileLangParser.DeclarationContext):
        pass

    # Exit a parse tree produced by WhileLangParser#declaration.
    def exitDeclaration(self, ctx:WhileLangParser.DeclarationContext):
        pass


    # Enter a parse tree produced by WhileLangParser#type.
    def enterType(self, ctx:WhileLangParser.TypeContext):
        pass

    # Exit a parse tree produced by WhileLangParser#type.
    def exitType(self, ctx:WhileLangParser.TypeContext):
        pass


    # Enter a parse tree produced by WhileLangParser#assignment.
    def enterAssignment(self, ctx:WhileLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by WhileLangParser#assignment.
    def exitAssignment(self, ctx:WhileLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by WhileLangParser#whileStatement.
    def enterWhileStatement(self, ctx:WhileLangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#whileStatement.
    def exitWhileStatement(self, ctx:WhileLangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#ifStatement.
    def enterIfStatement(self, ctx:WhileLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#ifStatement.
    def exitIfStatement(self, ctx:WhileLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#breakStatement.
    def enterBreakStatement(self, ctx:WhileLangParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#breakStatement.
    def exitBreakStatement(self, ctx:WhileLangParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#continueStatement.
    def enterContinueStatement(self, ctx:WhileLangParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#continueStatement.
    def exitContinueStatement(self, ctx:WhileLangParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#ExprCondition.
    def enterExprCondition(self, ctx:WhileLangParser.ExprConditionContext):
        pass

    # Exit a parse tree produced by WhileLangParser#ExprCondition.
    def exitExprCondition(self, ctx:WhileLangParser.ExprConditionContext):
        pass


    # Enter a parse tree produced by WhileLangParser#ComparisonExpr.
    def enterComparisonExpr(self, ctx:WhileLangParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#ComparisonExpr.
    def exitComparisonExpr(self, ctx:WhileLangParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by WhileLangParser#StringExpr.
    def enterStringExpr(self, ctx:WhileLangParser.StringExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#StringExpr.
    def exitStringExpr(self, ctx:WhileLangParser.StringExprContext):
        pass


    # Enter a parse tree produced by WhileLangParser#IdExpr.
    def enterIdExpr(self, ctx:WhileLangParser.IdExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#IdExpr.
    def exitIdExpr(self, ctx:WhileLangParser.IdExprContext):
        pass


    # Enter a parse tree produced by WhileLangParser#NumberExpr.
    def enterNumberExpr(self, ctx:WhileLangParser.NumberExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#NumberExpr.
    def exitNumberExpr(self, ctx:WhileLangParser.NumberExprContext):
        pass


    # Enter a parse tree produced by WhileLangParser#ArithmeticExpr.
    def enterArithmeticExpr(self, ctx:WhileLangParser.ArithmeticExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#ArithmeticExpr.
    def exitArithmeticExpr(self, ctx:WhileLangParser.ArithmeticExprContext):
        pass


    # Enter a parse tree produced by WhileLangParser#ParenExpr.
    def enterParenExpr(self, ctx:WhileLangParser.ParenExprContext):
        pass

    # Exit a parse tree produced by WhileLangParser#ParenExpr.
    def exitParenExpr(self, ctx:WhileLangParser.ParenExprContext):
        pass



del WhileLangParser