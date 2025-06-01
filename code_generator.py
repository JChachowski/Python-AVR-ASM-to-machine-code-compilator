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
        print(hex(opcode))
        self.code.append(opcode)
        self.pc += 2
        return self.visitChildren(ctx)

    # 4 out of 124
    def encode_instruction(self, mnemonic, operands):
        if mnemonic == "ADC":
            # Format: ADC Rd,Rr
            # 0001 11rd dddd rrrr
            opcode = 0b0000110000000000
            Rd = int(operands[0].replace("R", ""))
            Rr = int(operands[1].replace("R", ""))

            final = opcode | ((Rr & 0b10000) << 5) | (Rd  << 4) | (Rr & 0b01111)
            return int(final)
        
        elif mnemonic == "ADD":
            # Format: ADD Rd,Rr
            # 0000 11rd dddd rrrr
            opcode = 0b0001110000000000
            Rd = int(operands[0].replace("R", ""))
            Rr = int(operands[1].replace("R", ""))

            final = opcode | ((Rr & 0b10000) << 5) | (Rd  << 4) | (Rr & 0b01111)
            return int(final)


        #elif mnemonic == "ADIW":

        elif mnemonic == "AND":
            # Format: AND Rd,Rr
            # 0010 00rd dddd rrrr
            opcode = 0b0010000000000000
            Rd = int(operands[0].replace("R", ""))
            Rr = int(operands[1].replace("R", ""))

            final = opcode | ((Rr & 0b10000) << 5) | (Rd  << 4) | (Rr & 0b01111)
            return int(final)
        
        elif mnemonic == "ANDI":
            # Format: ANDI Rd,K
            # 0111 KKKK dddd KKKK
            opcode = 0b0111000000000000
            Rd = int(operands[0].replace("R", ""))
            k = int(operands[1].lower(),0)
            #print(k)
            #if (k[1] == 'x'): k = int(k,16)
            #else: k = int(k)

            final = opcode | ((k & 0b11110000) << 4) | ((Rd & 0b00001111) << 4) | (k & 0b00001111)
            return int(final)

            

        elif mnemonic == "ASR":
            # Format: ASR Rd
            # 1001 010d dddd 0101
            opcode = 0b1001010000000101
            Rd = int(operands[0].replace("R", ""))

            final = opcode | (Rd<<4)
            return int(final)
        
        elif mnemonic == "BCLR":
            # Format: BCLR s
            # 1001 0100 1sss 1000
            opcode = 0b1001010010001000
            s = int(operands[0].lower(),0)

            final = opcode | ((s & 0b111) << 4)
            return int(final)

        elif mnemonic == "BLD":
            # Format: BLD Rd, b
            # 1111 100d dddd 0bbb
            opcode = 0b1111100000000000
            Rd = int(operands[0].replace("R", ""))
            b = int(operands[1].lower(),0)

            final = opcode | ((Rd&0b11111)<<4) | (b&0b111)
            return int(final)
        
        elif mnemonic == "BRBC":
            # Format: BRBC s,k
            # 1111 01kk kkkk ksss
            opcode = 0b1111010000000000

            s = int(operands[0].lower(),0)
            # k ma dwie opcje: 1. label, 2. liczba -64:63
            k = operands[1]
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = addres // 2
            else: addres = int(operands[1].lower(),0)

            final = opcode | ((addres&0b1111111) << 3) | (s&0b111)

            return int(final)
        
        elif mnemonic == "BRBS":
            # Format: BRBS s,k
            # 1111 00kk kkkk ksss
            opcode = 0b1111000000000000

            s = int(operands[0].lower(),0)
            k = operands[1]

            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = addres // 2
            else: addres = int(operands[1].lower(),0)

            final = opcode | ((addres&0b1111111) << 3) | (s&0b111)

            return int(final)

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


