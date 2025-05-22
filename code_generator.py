from AVRVisitor import AVRVisitor

class CodeGenerator(AVRVisitor):
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
        self.code = []
        self.pc = 0

    def visitInstruction(self, ctx):
        mnemonic = ctx.mnemonic().getText()
        operands = ctx.operandList().getText().replace(" ", "").split(",") if ctx.operandList() else []
        opcode = self.encode_instruction(mnemonic, operands)
        self.code.append(opcode)
        self.pc += 2
        return self.visitChildren(ctx)

    # 3 out of 124
    def encode_instruction(self, mnemonic, operands):
        if mnemonic == "LDI":
            # Format: LDI Rd, K
            reg = int(operands[0].replace("R", ""))
            imm = int(operands[1], 0)
            opcode = 0xE000 | ((reg & 0xF) << 4) | (imm & 0xF)
            return opcode
        elif mnemonic == "OUT":
            #TODO 
            # OUT A, Rr — simplified for low IO space
            addr = int(operands[0], 0)
            reg = int(operands[1].replace("R", ""))
            opcode = 0xB800 | ((addr & 0x18) << 5) | ((reg & 0x1F) | ((addr & 0x07) << 3))
            return opcode
        elif mnemonic == "JMP":
            label = operands[0]
            addr = self.symbol_table.get(label, 0) // 2  # word address
            opcode = [0x940C, addr]  # simplified pseudo-encoding for demo
            return opcode
        else:
            return 0x0000  # default NOP for unknown

    def get_flat_code(self):
        flat = []
        for entry in self.code:
            if isinstance(entry, list):
                flat.extend(entry)
            else:
                flat.append(entry)
        return flat


