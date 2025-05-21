# Generated from AVR.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .AVRParser import AVRParser
else:
    from AVRParser import AVRParser

# This class defines a complete listener for a parse tree produced by AVRParser.
class AVRListener(ParseTreeListener):

    # Enter a parse tree produced by AVRParser#program.
    def enterProgram(self, ctx:AVRParser.ProgramContext):
        pass

    # Exit a parse tree produced by AVRParser#program.
    def exitProgram(self, ctx:AVRParser.ProgramContext):
        pass


    # Enter a parse tree produced by AVRParser#line.
    def enterLine(self, ctx:AVRParser.LineContext):
        pass

    # Exit a parse tree produced by AVRParser#line.
    def exitLine(self, ctx:AVRParser.LineContext):
        pass


    # Enter a parse tree produced by AVRParser#instruction.
    def enterInstruction(self, ctx:AVRParser.InstructionContext):
        pass

    # Exit a parse tree produced by AVRParser#instruction.
    def exitInstruction(self, ctx:AVRParser.InstructionContext):
        pass


    # Enter a parse tree produced by AVRParser#operandList.
    def enterOperandList(self, ctx:AVRParser.OperandListContext):
        pass

    # Exit a parse tree produced by AVRParser#operandList.
    def exitOperandList(self, ctx:AVRParser.OperandListContext):
        pass


    # Enter a parse tree produced by AVRParser#operand.
    def enterOperand(self, ctx:AVRParser.OperandContext):
        pass

    # Exit a parse tree produced by AVRParser#operand.
    def exitOperand(self, ctx:AVRParser.OperandContext):
        pass


    # Enter a parse tree produced by AVRParser#label.
    def enterLabel(self, ctx:AVRParser.LabelContext):
        pass

    # Exit a parse tree produced by AVRParser#label.
    def exitLabel(self, ctx:AVRParser.LabelContext):
        pass


    # Enter a parse tree produced by AVRParser#directive.
    def enterDirective(self, ctx:AVRParser.DirectiveContext):
        pass

    # Exit a parse tree produced by AVRParser#directive.
    def exitDirective(self, ctx:AVRParser.DirectiveContext):
        pass


    # Enter a parse tree produced by AVRParser#comment.
    def enterComment(self, ctx:AVRParser.CommentContext):
        pass

    # Exit a parse tree produced by AVRParser#comment.
    def exitComment(self, ctx:AVRParser.CommentContext):
        pass


    # Enter a parse tree produced by AVRParser#mnemonic.
    def enterMnemonic(self, ctx:AVRParser.MnemonicContext):
        pass

    # Exit a parse tree produced by AVRParser#mnemonic.
    def exitMnemonic(self, ctx:AVRParser.MnemonicContext):
        pass



del AVRParser