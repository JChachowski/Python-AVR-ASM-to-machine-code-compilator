from antlr4 import *
from AVRLexer import AVRLexer
from AVRParser import AVRParser
from MyAVRVisitor import MyAVRVisitor 
from intelhex import IntelHex
from label_collector import LabelCollector
from code_generator import CodeGenerator

#Intel HEX file generator
def write_hex_file(filename: str, machine_code: list[int]):
    ih = IntelHex()
    addr = 0
    for word in machine_code:
        ih.puts(addr, word.to_bytes(2, byteorder="little"))
        addr += 2
    ih.write_hex_file(filename)

#raw binary file generator
def write_bin_file(filename: str, machine_code: list[int]):
    with open(filename, 'wb') as f:
        for word in machine_code:
            f.write(word.to_bytes(2, byteorder='little'))

def assemble(input_code: str, hex_filename: str):
    input_stream = InputStream(input_code.upper())

    lexer = AVRLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = AVRParser(stream)
    tree = parser.program()

    #collect labels
    collector = LabelCollector()
    collector.visit(tree)

    #generate code
    generator = CodeGenerator(collector.labels)
    generator.visit(tree)
    machine_code = generator.get_flat_code()

    write_hex_file(hex_filename, machine_code)
    write_bin_file("out.bin",machine_code)
    return machine_code

#TODO input handling: add propper file input, sanitize it and add .upper()
input_code =  """
start:
        ADC R16, R17
        ADD R18, R19
        AND R20, R21
        ANDI R22, 0x0F
        ASR R23
        BCLR 0
        BLD R24, 1
        BRBC 1, start
        BRBS 2, start
        BRCC start
        BRCS start
        BREAK
        BREQ start
        BRGE start
        BRHC start
        BRHS start
        BRID start
        BRIE start
        BRLO start
        BRLT start
        BRMI start
        BRNE start
        BRPL start
        BRSH start
        BRTC start
        BRTS start
        BRVC start
        BRVS start
        BSET 1
        BST R25, 2
"""

assembled_code = assemble(input_code, "out.hex")
assembled_code