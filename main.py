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

    write_hex_file("test.hex",machine_code)
    write_bin_file("test.bin",machine_code)
    return machine_code

#TODO input handling: add propper file input, sanitize it and add .upper()
input_code =  """
start:
    ldi    R16, 0xF0
    ldi    R17, 0xF0
    out    0x04, R16
    out    0x05, R16
    jmp    start
"""

assembled_code = assemble(input_code, "out.hex")
assembled_code