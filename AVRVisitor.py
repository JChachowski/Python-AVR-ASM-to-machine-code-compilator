# Generated from AVR.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .AVRParser import AVRParser
else:
    from AVRParser import AVRParser

# This class defines a complete generic visitor for a parse tree produced by AVRParser.

class AVRVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AVRParser#program.
    def visitProgram(self, ctx:AVRParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AVRParser#line.
    def visitLine(self, ctx:AVRParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AVRParser#instruction.
    def visitInstruction(self, ctx:AVRParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AVRParser#operandList.
    def visitOperandList(self, ctx:AVRParser.OperandListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AVRParser#operand.
    def visitOperand(self, ctx:AVRParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AVRParser#label.
    def visitLabel(self, ctx:AVRParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AVRParser#directive.
    def visitDirective(self, ctx:AVRParser.DirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AVRParser#comment.
    def visitComment(self, ctx:AVRParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AVRParser#mnemonic.
    def visitMnemonic(self, ctx:AVRParser.MnemonicContext):
        return self.visitChildren(ctx)



del AVRParser