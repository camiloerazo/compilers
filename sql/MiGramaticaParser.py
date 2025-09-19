# Generated from MiGramatica.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,48,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,1,0,1,0,3,0,21,8,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,
        29,8,1,10,1,12,1,32,9,1,3,1,34,8,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,
        4,1,5,1,5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,2,1,0,7,12,1,0,14,
        15,43,0,14,1,0,0,0,2,33,1,0,0,0,4,35,1,0,0,0,6,37,1,0,0,0,8,39,1,
        0,0,0,10,43,1,0,0,0,12,45,1,0,0,0,14,15,5,1,0,0,15,16,3,2,1,0,16,
        17,5,2,0,0,17,20,3,6,3,0,18,19,5,3,0,0,19,21,3,8,4,0,20,18,1,0,0,
        0,20,21,1,0,0,0,21,22,1,0,0,0,22,23,5,6,0,0,23,1,1,0,0,0,24,34,5,
        4,0,0,25,30,3,4,2,0,26,27,5,5,0,0,27,29,3,4,2,0,28,26,1,0,0,0,29,
        32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,
        0,33,24,1,0,0,0,33,25,1,0,0,0,34,3,1,0,0,0,35,36,5,13,0,0,36,5,1,
        0,0,0,37,38,5,13,0,0,38,7,1,0,0,0,39,40,3,4,2,0,40,41,3,10,5,0,41,
        42,3,12,6,0,42,9,1,0,0,0,43,44,7,0,0,0,44,11,1,0,0,0,45,46,7,1,0,
        0,46,13,1,0,0,0,3,20,30,33
    ]

class MiGramaticaParser ( Parser ):

    grammarFileName = "MiGramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'SELECT'", "'FROM'", "'WHERE'", "'*'", 
                     "','", "';'", "'>'", "'<'", "'='", "'>='", "'<='", 
                     "'!='" ]

    symbolicNames = [ "<INVALID>", "SELECT", "FROM", "WHERE", "STAR", "COMMA", 
                      "SEMI", "GT", "LT", "EQ", "GE", "LE", "NE", "IDENTIFIER", 
                      "NUMBER", "STRING", "WS" ]

    RULE_query = 0
    RULE_column_list = 1
    RULE_column = 2
    RULE_table = 3
    RULE_condition = 4
    RULE_operator = 5
    RULE_value = 6

    ruleNames =  [ "query", "column_list", "column", "table", "condition", 
                   "operator", "value" ]

    EOF = Token.EOF
    SELECT=1
    FROM=2
    WHERE=3
    STAR=4
    COMMA=5
    SEMI=6
    GT=7
    LT=8
    EQ=9
    GE=10
    LE=11
    NE=12
    IDENTIFIER=13
    NUMBER=14
    STRING=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(MiGramaticaParser.SELECT, 0)

        def column_list(self):
            return self.getTypedRuleContext(MiGramaticaParser.Column_listContext,0)


        def FROM(self):
            return self.getToken(MiGramaticaParser.FROM, 0)

        def table(self):
            return self.getTypedRuleContext(MiGramaticaParser.TableContext,0)


        def SEMI(self):
            return self.getToken(MiGramaticaParser.SEMI, 0)

        def WHERE(self):
            return self.getToken(MiGramaticaParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(MiGramaticaParser.ConditionContext,0)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)




    def query(self):

        localctx = MiGramaticaParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(MiGramaticaParser.SELECT)
            self.state = 15
            self.column_list()
            self.state = 16
            self.match(MiGramaticaParser.FROM)
            self.state = 17
            self.table()
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 18
                self.match(MiGramaticaParser.WHERE)
                self.state = 19
                self.condition()


            self.state = 22
            self.match(MiGramaticaParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(MiGramaticaParser.STAR, 0)

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.ColumnContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.ColumnContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiGramaticaParser.COMMA)
            else:
                return self.getToken(MiGramaticaParser.COMMA, i)

        def getRuleIndex(self):
            return MiGramaticaParser.RULE_column_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_list" ):
                listener.enterColumn_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_list" ):
                listener.exitColumn_list(self)




    def column_list(self):

        localctx = MiGramaticaParser.Column_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_column_list)
        self._la = 0 # Token type
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.match(MiGramaticaParser.STAR)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.column()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 26
                    self.match(MiGramaticaParser.COMMA)
                    self.state = 27
                    self.column()
                    self.state = 32
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiGramaticaParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiGramaticaParser.RULE_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn" ):
                listener.enterColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn" ):
                listener.exitColumn(self)




    def column(self):

        localctx = MiGramaticaParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(MiGramaticaParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiGramaticaParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiGramaticaParser.RULE_table

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable" ):
                listener.enterTable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable" ):
                listener.exitTable(self)




    def table(self):

        localctx = MiGramaticaParser.TableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_table)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(MiGramaticaParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self):
            return self.getTypedRuleContext(MiGramaticaParser.ColumnContext,0)


        def operator(self):
            return self.getTypedRuleContext(MiGramaticaParser.OperatorContext,0)


        def value(self):
            return self.getTypedRuleContext(MiGramaticaParser.ValueContext,0)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = MiGramaticaParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.column()
            self.state = 40
            self.operator()
            self.state = 41
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(MiGramaticaParser.GT, 0)

        def LT(self):
            return self.getToken(MiGramaticaParser.LT, 0)

        def EQ(self):
            return self.getToken(MiGramaticaParser.EQ, 0)

        def GE(self):
            return self.getToken(MiGramaticaParser.GE, 0)

        def LE(self):
            return self.getToken(MiGramaticaParser.LE, 0)

        def NE(self):
            return self.getToken(MiGramaticaParser.NE, 0)

        def getRuleIndex(self):
            return MiGramaticaParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = MiGramaticaParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8064) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(MiGramaticaParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(MiGramaticaParser.STRING, 0)

        def getRuleIndex(self):
            return MiGramaticaParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = MiGramaticaParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





