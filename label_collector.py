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
        self.address += 2  # each instruction is 2 bytes
        return self.visitChildren(ctx)