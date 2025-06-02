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
        print(hex(opcode), "@ pc: ", self.pc)
        self.code.append(opcode)
        if(mnemonic == "CALL"):
            self.pc += 4
        else:
            self.pc += 2
        return self.visitChildren(ctx)

    # 4 out of 124
    def encode_instruction(self, mnemonic, operands):
        if mnemonic == "ADC":
            # Format: ADC Rd,Rr
            # 0001 11rd dddd rrrr
            opcode = 0b0001110000000000
            Rd = int(operands[0].replace("R", ""))
            Rr = int(operands[1].replace("R", ""))

            final = opcode | ((Rr & 0b10000) << 5) | (Rd  << 4) | (Rr & 0b01111)
            return int(final)
        
        elif mnemonic == "ADD":
            # Format: ADD Rd,Rr
            # 0000 11rd dddd rrrr
            opcode = 0b0000110000000000
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

            final = opcode | ((Rd & 0b11111) << 4) | (b & 0b111)
            return int(final)
        
        elif mnemonic == "BRBC":
            # Format: BRBC s,k
            # 1111 01kk kkkk ksss
            opcode = 0b1111010000000000

            s = int(operands[0].lower(),0)
            # k ma dwie opcje: 1. label, 2. liczba -64:63
            k = operands[1]
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = (addres-self.pc) // 2 - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3) | (s & 0b111)
            return int(final)
        
        elif mnemonic == "BRBS":
            # Format: BRBS s,k
            # 1111 00kk kkkk ksss
            opcode = 0b1111000000000000

            s = int(operands[0].lower(),0)
            k = operands[1]

            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = (addres-self.pc) // 2 - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3) | (s & 0b111)
            return int(final)

        elif mnemonic == "BRCC":
            #Format: BRCC k
            #1111 01kk kkkk k000
            opcode = 0b1111010000000000 
            k = operands[0]
            
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = (addres-self.pc) // 2 - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3)
            return int(final)

        elif mnemonic == "BRCS":
            #Format: BRCS k
            #1111 00kk kkkk k000
            opcode = 0b1111000000000000
            k = operands[0]
            
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = (addres-self.pc) // 2 - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3)
            return int(final)

        elif mnemonic == "BREAK":
            #Syntax: BREAK
            # 1001 0101 1001 1000
            opcode = 0b1001010110011000
            return int(opcode)
        
        elif mnemonic == "BREQ":
            #Syntax: BREQ k 
            # 1111 00kk kkkk k001
            opcode = 0b1111000000000001
            k = operands[0]
            
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = (addres-self.pc) // 2 - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3) 
            return int(final)

        elif mnemonic == "BRGE":
            #Syntax: BRGE k 
            # 1111 01kk kkkk k100
            opcode = 0b1111010000000100
            k = operands[0]
            
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = (addres-self.pc) // 2 - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3) 
            return int(final)
         
        elif mnemonic == "BRHC":
            #Syntax: BRHC k 
            # 1111 01kk kkkk k101
            opcode = 0b1111010000000101
            k = operands[0]
            
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = (addres-self.pc) // 2 - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3) 
            return int(final)
        
        elif mnemonic == "BRHS":
            #Syntax: BRHS k 
            # 1111 00kk kkkk k101
            opcode = 0b1111000000000101
            k = operands[0]
            
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = (addres-self.pc) // 2 - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3) 
            return int(final)
        
        elif mnemonic == "BRID":
            #Syntax: BRID k 
            # 1111 01kk kkkk k111
            opcode = 0b1111010000000111
            k = operands[0]
            
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = (addres-self.pc) // 2 - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3) 
            return int(final)
        
        elif mnemonic == "BRIE":
            #Syntax: BRIE k 
            # 1111 00kk kkkk k111
            opcode = 0b1111000000000111
            k = operands[0]
            
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = (addres-self.pc) // 2 - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3) 
            return int(final)
        
        elif mnemonic == "BRLO":
            #Syntax: BRLO k 
            # 1111 00kk kkkk k000
            opcode = 0b1111000000000000
            k = operands[0]
            
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = (addres-self.pc) // 2 - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3) 
            return int(final)
        
        elif mnemonic == "BRLT":
            #Syntax: BRLT k
            # 1111 00kk kkkk k100
            opcode = 0b1111000000000100
            k = operands[0]
            
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = (addres-self.pc) // 2 - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3) 
            return int(final)
        
        elif mnemonic == "BRMI":
            #Syntax: BRMI k 
            # 1111 00kk kkkk k010
            opcode = 0b1111000000000010
            k = operands[0]

            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = ((addres-self.pc) // 2) - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3) 
            return int(final)

        elif mnemonic == "BRNE":
            #Syntax: BRNE k 
            # 1111 01kk kkkk k001
            opcode = 0b1111010000000001
            k = operands[0]
            
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = ((addres-(self.pc))  // 2) - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3) 
            return int(final)

        elif mnemonic == "BRPL":
            #Syntax: BRPL k 
            # 1111 01kk kkkk k010
            opcode = 0b1111010000000010
            k = operands[0]
            
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = (addres-self.pc) // 2 - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3) 
            return int(final)
        
        elif mnemonic == "BRSH":
            #Syntax: BRSH k 
            # 1111 01kk kkkk k000
            opcode = 0b1111010000000000
            k = operands[0]
            
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = (addres-self.pc) // 2 - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3) 
            return int(final)

        elif mnemonic == "BRTC":
            #Syntax: BRTC k 
            # 1111 01kk kkkk k110
            opcode = 0b1111010000000110
            k = operands[0]
            
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = (addres-self.pc) // 2 - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3) 
            return int(final)
        
        elif mnemonic == "BRTS":
            #Syntax: BRTS k 
            # 1111 00kk kkkk k110
            opcode = 0b1111000000000110
            k = operands[0]
            
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = (addres-self.pc) // 2 - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3) 
            return int(final)
        
        elif mnemonic == "BRVC":
            #Syntax: BRVC k 
            # 1111 01kk kkkk k011
            opcode = 0b1111010000000011
            k = operands[0]
            
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = (addres-self.pc) // 2 - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3) 
            return int(final)
        
        elif mnemonic == "BRVS":
            #Syntax: BRVS k 
            # 1111 00kk kkkk k011
            opcode = 0b1111000000000011
            k = operands[0]
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = (addres-self.pc) // 2 - 1
            else: addres = int(k.lower(),0)

            final = opcode | ((addres & 0b1111111) << 3) 
            return int(final)
        
        
        elif mnemonic == "BSET":
            #Syntax: BSET s 
            # 1001 0100 0sss 1000
            opcode = 0b1001010000001000
            s = int(operands[0].lower(),0)

            final = opcode | ((s & 0b111) << 4)
            return int(final)

        elif mnemonic == "BST":
            #Syntax: BST Rd,b 
            # 1111 101d dddd 0bbb
            opcode = 0b1111101000000000

            Rd = int(operands[0].replace("R", ""))
            b = int(operands[1].lower(),0)

            final = opcode | ((Rd & 0b11111) << 4) | (b & 0b111)
            return int(final)
        
        # 32bit instruction, k is either PC number or label
        elif mnemonic == "CALL":
            #Syntax: CALL k 
            # 1001 010k kkkk 111k kkkk kkkk kkkk kkkk
            opcode = 0b10010100000011100000000000000000
            k = operands[0]
            addres = self.symbol_table.get(k,None)
            if(addres != None): addres = addres // 2
            else: addres = int(k.lower(),0)
            #print()
            #print("opcode", bin(opcode))
            #print("adres", bin(addres))
            #print("---vvv---")
            #print(bin(((addres & 0b1111100000000000000000) << 3)))
            #print(bin((addres & 0b0000011111111111111111)))
            #print(bin(opcode))
            #print("---^^^---")
            final = opcode | ((addres & 0b1111100000000000000000) << 3) | (addres & 0b0000011111111111111111)
            #print("final", bin(final))
            return int(final)


        #elif mnemonic == "":
        #elif mnemonic == "":
        #elif mnemonic == "":
        #elif mnemonic == "":
        #elif mnemonic == "":
        #elif mnemonic == "":
        #elif mnemonic == "":
        #elif mnemonic == "":
        elif mnemonic == "RET":
            #Syntax: RET
            # 1001 0101 0000 1000
            opcode = 0b1001010100001000
            return(int(opcode))
        
        elif mnemonic == "OUT":
            #Syntax: OUT A,Rr 
            # 1011 1AAr rrrr AAAA
            opcode = 0b1011100000000000
            a = int(operands[0].lower(),0)
            Rr = int(operands[1].replace("R", ""))
            
            final = opcode | ((a & 0b110000) << 5) | ((Rr & 0b11111)<<4) | (a & 0b001111)
            return int(final)
        
        elif mnemonic == "LDI":
            #Syntax: LDI Rd, k
            # 1110 KKKK dddd KKKK
            opcode = 0b1110000000000000
            Rd = int(operands[0].replace("R", ""))

            k = int(operands[1].lower(),0)
            print(operands[1])
            #if(k[1] == 'x'): k = int(operands[1].lower(),16)
            #if(k[1] == 'b'): k = int(operands[1].lower(),2)
            print(k)
            final = opcode | ((k & 0b11110000) << 4) | ((Rd & 0b00001111) << 4) | (k & 0b00001111)
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


