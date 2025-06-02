from AVRVisitor import AVRVisitor

class LabelCollector(AVRVisitor):
    def __init__(self):
        self.labels = {}
        self.address = 0

    def visitLabel(self, ctx):
        label = ctx.getText().rstrip(":")
        self.labels[label] = self.address
        return self.visitChildren(ctx)

    def visitInstruction(self, ctx):
        mnemonic = ctx.mnemonic().getText().upper()
        if(mnemonic == "CALL"):
            self.address += 4
        else:
            self.address += 2  # 2 bytes
        return self.visitChildren(ctx)