# Generated from MiGramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiGramaticaParser import MiGramaticaParser
else:
    from MiGramaticaParser import MiGramaticaParser

# This class defines a complete listener for a parse tree produced by MiGramaticaParser.
class MiGramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by MiGramaticaParser#query.
    def enterQuery(self, ctx:MiGramaticaParser.QueryContext):
        pass

    # Exit a parse tree produced by MiGramaticaParser#query.
    def exitQuery(self, ctx:MiGramaticaParser.QueryContext):
        pass


    # Enter a parse tree produced by MiGramaticaParser#column_list.
    def enterColumn_list(self, ctx:MiGramaticaParser.Column_listContext):
        pass

    # Exit a parse tree produced by MiGramaticaParser#column_list.
    def exitColumn_list(self, ctx:MiGramaticaParser.Column_listContext):
        pass


    # Enter a parse tree produced by MiGramaticaParser#column.
    def enterColumn(self, ctx:MiGramaticaParser.ColumnContext):
        pass

    # Exit a parse tree produced by MiGramaticaParser#column.
    def exitColumn(self, ctx:MiGramaticaParser.ColumnContext):
        pass


    # Enter a parse tree produced by MiGramaticaParser#table.
    def enterTable(self, ctx:MiGramaticaParser.TableContext):
        pass

    # Exit a parse tree produced by MiGramaticaParser#table.
    def exitTable(self, ctx:MiGramaticaParser.TableContext):
        pass


    # Enter a parse tree produced by MiGramaticaParser#condition.
    def enterCondition(self, ctx:MiGramaticaParser.ConditionContext):
        pass

    # Exit a parse tree produced by MiGramaticaParser#condition.
    def exitCondition(self, ctx:MiGramaticaParser.ConditionContext):
        pass


    # Enter a parse tree produced by MiGramaticaParser#operator.
    def enterOperator(self, ctx:MiGramaticaParser.OperatorContext):
        pass

    # Exit a parse tree produced by MiGramaticaParser#operator.
    def exitOperator(self, ctx:MiGramaticaParser.OperatorContext):
        pass


    # Enter a parse tree produced by MiGramaticaParser#value.
    def enterValue(self, ctx:MiGramaticaParser.ValueContext):
        pass

    # Exit a parse tree produced by MiGramaticaParser#value.
    def exitValue(self, ctx:MiGramaticaParser.ValueContext):
        pass



del MiGramaticaParser