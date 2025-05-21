from AVRVisitor import AVRVisitor

class MyAVRVisitor(AVRVisitor):
    def visitInstruction(self, ctx):
        mnemonic = ctx.mnemonic().getText()
        operands = ctx.operandList().getText() if ctx.operandList() else ""
        print(f"[Instruction] {mnemonic} {operands}")
        return self.visitChildren(ctx)

    def visitLabel(self, ctx):
        label_name = ctx.getText()
        print(f"[Label] {label_name}")
        return self.visitChildren(ctx)

    def visitDirective(self, ctx):
        print(f"[Directive] {ctx.getText()}")
        return self.visitChildren(ctx)

    def enterLabel(self, ctx):
        print(f"Label: {ctx.getText()}")

    def enterDirective(self, ctx):
        print(f"Directive: {ctx.getText()}")