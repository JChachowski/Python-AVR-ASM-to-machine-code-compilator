import sys
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

#type "hex" | "bin"
def assemble(input_code: str, filename: str, type: str):
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

    if(type == "hex"):
        filename = filename
        write_hex_file(filename, machine_code)
    elif(type == "bin"): 
        filename = filename
        write_bin_file(filename, machine_code)
    else: print("ERROR: file not saved, wrong type")
    return machine_code

#TODO input handling: add propper file input, sanitize it and add .upper()
input_code =  """

start:
        LDI R16, 0x20      ; R16 = 0b00100000 (PB5 mask)
        OUT 0x04, R16          ; DDRB ← R16 (set PB5 as output)

loop:
        OUT 0x05, R16          ; PORTB ← R16 → LED ON

        ; ~0.5 second delay (nested loops)
        LDI R17, 20            ; Outer loop count (tuned)
delay_on_outer:
        LDI R18, 255           ; Middle loop
delay_on_middle:
        LDI R19, 255           ; Inner loop
delay_on_inner:
        NOP
        NOP
        NOP
        NOP
        NOP
        ADD R19, R20           ; R20 = 0, so acts like DEC (loop R19 down)
        BRNE delay_on_inner
        ADD R18, R20
        BRNE delay_on_middle
        ADD R17, R20
        BRNE delay_on_outer

        LDI R21, 0x00
        OUT 0x05, R21          ; PORTB ← 0 → LED OFF

        ; ~0.5 second delay again
        LDI R17, 20
delay_off_outer:
        LDI R18, 255
delay_off_middle:
        LDI R19, 255
delay_off_inner:
        NOP
        NOP
        NOP
        NOP
        NOP
        ADD R19, R20
        BRNE delay_off_inner
        ADD R18, R20
        BRNE delay_off_middle
        ADD R17, R20
        BRNE delay_off_outer

        BRCC loop              ; Unconditional loop back
"""

input_filename = sys.argv[1]
output_filename = sys.argv[2]
print(input_filename[-4:])
print(output_filename[-4:] == ".hex")
if(input_filename[-4:] != ".asm"): 
    print("ERROR: input filename extension incorrect")
    exit()
if(output_filename[-4:] not in [".hex", ".bin"]): 
    print("ERROR: output filename extension incorrect")
    exit()
output_type = output_filename[-3:]

with open(input_filename, "r", encoding="utf-8") as file:
    input_code = file.read()

assembled_code = assemble(input_code, "out.hex",output_type)
assembled_code