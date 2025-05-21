# Generated from AVR.g4 by ANTLR 4.13.0
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
        4,1,128,58,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,3,2,36,8,2,1,3,1,3,1,3,5,3,41,8,
        3,10,3,12,3,44,9,3,1,4,1,4,1,5,1,5,1,6,1,6,3,6,52,8,6,1,7,1,7,1,
        8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,2,2,0,121,122,124,124,1,
        0,2,120,56,0,21,1,0,0,0,2,31,1,0,0,0,4,33,1,0,0,0,6,37,1,0,0,0,8,
        45,1,0,0,0,10,47,1,0,0,0,12,49,1,0,0,0,14,53,1,0,0,0,16,55,1,0,0,
        0,18,20,3,2,1,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,
        1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,
        32,3,4,2,0,27,32,3,10,5,0,28,32,3,12,6,0,29,32,3,14,7,0,30,32,5,
        127,0,0,31,26,1,0,0,0,31,27,1,0,0,0,31,28,1,0,0,0,31,29,1,0,0,0,
        31,30,1,0,0,0,32,3,1,0,0,0,33,35,3,16,8,0,34,36,3,6,3,0,35,34,1,
        0,0,0,35,36,1,0,0,0,36,5,1,0,0,0,37,42,3,8,4,0,38,39,5,1,0,0,39,
        41,3,8,4,0,40,38,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,
        0,43,7,1,0,0,0,44,42,1,0,0,0,45,46,7,0,0,0,46,9,1,0,0,0,47,48,5,
        123,0,0,48,11,1,0,0,0,49,51,5,125,0,0,50,52,3,6,3,0,51,50,1,0,0,
        0,51,52,1,0,0,0,52,13,1,0,0,0,53,54,5,126,0,0,54,15,1,0,0,0,55,56,
        7,1,0,0,56,17,1,0,0,0,5,21,31,35,42,51
    ]

class AVRParser ( Parser ):

    grammarFileName = "AVR.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'ADC'", "'ADD'", "'ADIW'", "'AND'", 
                     "'ANDI'", "'ASR'", "'BCLR'", "'BLD'", "'BRBC'", "'BRBS'", 
                     "'BRCC'", "'BRCS'", "'BREAK'", "'BREQ'", "'BRGE'", 
                     "'BRHC'", "'BRHS'", "'BRID'", "'BRIE'", "'BRLO'", "'BRLT'", 
                     "'BRMI'", "'BRNE'", "'BRPL'", "'BRSH'", "'BRTC'", "'BRTS'", 
                     "'BRVC'", "'BRVS'", "'BSET'", "'BST'", "'CALL'", "'CBI'", 
                     "'CBR'", "'CLC'", "'CLH'", "'CLI'", "'CLN'", "'CLR'", 
                     "'CLS'", "'CLT'", "'CLV'", "'CLZ'", "'COM'", "'CP'", 
                     "'CPC'", "'CPI'", "'CPSE'", "'DEC'", "'DES'", "'EICALL'", 
                     "'EIJMP'", "'ELPM'", "'EOR'", "'FMUL'", "'FMULS'", 
                     "'FMULSU'", "'ICALL'", "'IJMP'", "'IN'", "'INC'", "'JMP'", 
                     "'LAC'", "'LAS'", "'LAT'", "'LD'", "'LDD'", "'LDI'", 
                     "'LDS'", "'LPM'", "'LSL'", "'LSR'", "'MOV'", "'MOVW'", 
                     "'MUL'", "'MULS'", "'MULSU'", "'NEG'", "'NOP'", "'OR'", 
                     "'ORI'", "'OUT'", "'POP'", "'PUSH'", "'RCALL'", "'RET'", 
                     "'RETI'", "'RJMP'", "'ROL'", "'ROR'", "'SBC'", "'SBCI'", 
                     "'SBI'", "'SBIC'", "'SBIS'", "'SBIW'", "'SBR'", "'SBRC'", 
                     "'SBRS'", "'SEC'", "'SEH'", "'SEI'", "'SEN'", "'SER'", 
                     "'SES'", "'SET'", "'SEV'", "'SEZ'", "'SLEEP'", "'SPM'", 
                     "'ST'", "'STD'", "'STS'", "'SUB'", "'SUBI'", "'SWAP'", 
                     "'TST'", "'WDR'", "'XCH'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "REGISTER", "NUMBER", "LABEL_DEF", "LABEL_REF", 
                      "DOT_DIRECTIVE", "COMMENT", "NEWLINE", "WS" ]

    RULE_program = 0
    RULE_line = 1
    RULE_instruction = 2
    RULE_operandList = 3
    RULE_operand = 4
    RULE_label = 5
    RULE_directive = 6
    RULE_comment = 7
    RULE_mnemonic = 8

    ruleNames =  [ "program", "line", "instruction", "operandList", "operand", 
                   "label", "directive", "comment", "mnemonic" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    T__55=56
    T__56=57
    T__57=58
    T__58=59
    T__59=60
    T__60=61
    T__61=62
    T__62=63
    T__63=64
    T__64=65
    T__65=66
    T__66=67
    T__67=68
    T__68=69
    T__69=70
    T__70=71
    T__71=72
    T__72=73
    T__73=74
    T__74=75
    T__75=76
    T__76=77
    T__77=78
    T__78=79
    T__79=80
    T__80=81
    T__81=82
    T__82=83
    T__83=84
    T__84=85
    T__85=86
    T__86=87
    T__87=88
    T__88=89
    T__89=90
    T__90=91
    T__91=92
    T__92=93
    T__93=94
    T__94=95
    T__95=96
    T__96=97
    T__97=98
    T__98=99
    T__99=100
    T__100=101
    T__101=102
    T__102=103
    T__103=104
    T__104=105
    T__105=106
    T__106=107
    T__107=108
    T__108=109
    T__109=110
    T__110=111
    T__111=112
    T__112=113
    T__113=114
    T__114=115
    T__115=116
    T__116=117
    T__117=118
    T__118=119
    T__119=120
    REGISTER=121
    NUMBER=122
    LABEL_DEF=123
    LABEL_REF=124
    DOT_DIRECTIVE=125
    COMMENT=126
    NEWLINE=127
    WS=128

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AVRParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AVRParser.LineContext)
            else:
                return self.getTypedRuleContext(AVRParser.LineContext,i)


        def getRuleIndex(self):
            return AVRParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = AVRParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & -1585267068834414593) != 0):
                self.state = 18
                self.line()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(AVRParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self):
            return self.getTypedRuleContext(AVRParser.InstructionContext,0)


        def label(self):
            return self.getTypedRuleContext(AVRParser.LabelContext,0)


        def directive(self):
            return self.getTypedRuleContext(AVRParser.DirectiveContext,0)


        def comment(self):
            return self.getTypedRuleContext(AVRParser.CommentContext,0)


        def NEWLINE(self):
            return self.getToken(AVRParser.NEWLINE, 0)

        def getRuleIndex(self):
            return AVRParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = AVRParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.instruction()
                pass
            elif token in [123]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.label()
                pass
            elif token in [125]:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.directive()
                pass
            elif token in [126]:
                self.enterOuterAlt(localctx, 4)
                self.state = 29
                self.comment()
                pass
            elif token in [127]:
                self.enterOuterAlt(localctx, 5)
                self.state = 30
                self.match(AVRParser.NEWLINE)
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


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mnemonic(self):
            return self.getTypedRuleContext(AVRParser.MnemonicContext,0)


        def operandList(self):
            return self.getTypedRuleContext(AVRParser.OperandListContext,0)


        def getRuleIndex(self):
            return AVRParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = AVRParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.mnemonic()
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & 11) != 0):
                self.state = 34
                self.operandList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AVRParser.OperandContext)
            else:
                return self.getTypedRuleContext(AVRParser.OperandContext,i)


        def getRuleIndex(self):
            return AVRParser.RULE_operandList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperandList" ):
                listener.enterOperandList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperandList" ):
                listener.exitOperandList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperandList" ):
                return visitor.visitOperandList(self)
            else:
                return visitor.visitChildren(self)




    def operandList(self):

        localctx = AVRParser.OperandListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_operandList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.operand()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 38
                self.match(AVRParser.T__0)
                self.state = 39
                self.operand()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REGISTER(self):
            return self.getToken(AVRParser.REGISTER, 0)

        def NUMBER(self):
            return self.getToken(AVRParser.NUMBER, 0)

        def LABEL_REF(self):
            return self.getToken(AVRParser.LABEL_REF, 0)

        def getRuleIndex(self):
            return AVRParser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = AVRParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_operand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not(((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & 11) != 0)):
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


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LABEL_DEF(self):
            return self.getToken(AVRParser.LABEL_DEF, 0)

        def getRuleIndex(self):
            return AVRParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = AVRParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(AVRParser.LABEL_DEF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT_DIRECTIVE(self):
            return self.getToken(AVRParser.DOT_DIRECTIVE, 0)

        def operandList(self):
            return self.getTypedRuleContext(AVRParser.OperandListContext,0)


        def getRuleIndex(self):
            return AVRParser.RULE_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirective" ):
                listener.enterDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirective" ):
                listener.exitDirective(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirective" ):
                return visitor.visitDirective(self)
            else:
                return visitor.visitChildren(self)




    def directive(self):

        localctx = AVRParser.DirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_directive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(AVRParser.DOT_DIRECTIVE)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 121)) & ~0x3f) == 0 and ((1 << (_la - 121)) & 11) != 0):
                self.state = 50
                self.operandList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(AVRParser.COMMENT, 0)

        def getRuleIndex(self):
            return AVRParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = AVRParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(AVRParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MnemonicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AVRParser.RULE_mnemonic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMnemonic" ):
                listener.enterMnemonic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMnemonic" ):
                listener.exitMnemonic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMnemonic" ):
                return visitor.visitMnemonic(self)
            else:
                return visitor.visitChildren(self)




    def mnemonic(self):

        localctx = AVRParser.MnemonicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_mnemonic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & -4) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 144115188075855871) != 0)):
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





