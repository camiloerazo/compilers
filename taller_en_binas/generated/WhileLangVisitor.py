# Generated from WhileLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .WhileLangParser import WhileLangParser
else:
    from WhileLangParser import WhileLangParser

# This class defines a complete generic visitor for a parse tree produced by WhileLangParser.

class WhileLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WhileLangParser#program.
    def visitProgram(self, ctx:WhileLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#statement.
    def visitStatement(self, ctx:WhileLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#declaration.
    def visitDeclaration(self, ctx:WhileLangParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#type.
    def visitType(self, ctx:WhileLangParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#assignment.
    def visitAssignment(self, ctx:WhileLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#whileStatement.
    def visitWhileStatement(self, ctx:WhileLangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#ifStatement.
    def visitIfStatement(self, ctx:WhileLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#breakStatement.
    def visitBreakStatement(self, ctx:WhileLangParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#continueStatement.
    def visitContinueStatement(self, ctx:WhileLangParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#ExprCondition.
    def visitExprCondition(self, ctx:WhileLangParser.ExprConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#ComparisonExpr.
    def visitComparisonExpr(self, ctx:WhileLangParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#StringExpr.
    def visitStringExpr(self, ctx:WhileLangParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#IdExpr.
    def visitIdExpr(self, ctx:WhileLangParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#NumberExpr.
    def visitNumberExpr(self, ctx:WhileLangParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#ArithmeticExpr.
    def visitArithmeticExpr(self, ctx:WhileLangParser.ArithmeticExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#ParenExpr.
    def visitParenExpr(self, ctx:WhileLangParser.ParenExprContext):
        return self.visitChildren(ctx)



del WhileLangParser