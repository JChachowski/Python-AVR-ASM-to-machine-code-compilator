from antlr4 import *
from AVRLexer import AVRLexer
from AVRParser import AVRParser
from MyAVRVisitor import MyAVRVisitor 

input_code = InputStream("""
start:
    ldi    R16, 0x03
    ldi    R17, 0xFF
    out    0x3D, R17
    out    0x3E, R16
    ldi    R20, 1
    ldi    R21, 0
    out    0x17, R20
LOOP:
    out    0x18, R20
    call    DELAY_1S
    out    0x18, R21
    call    DELAY_1S
    jmp    LOOP

DELAY_1S:
    ldi    r16, 82
    ldi    r17, 43
    ldi    r18, 0
DELAY_1S_1: 
    dec    r18
    brne    DELAY_1S_1
    dec    r17
    brne    DELAY_1S_1
    dec    r16
    brne    DELAY_1S_1
    lpm
    nop
    ret
""".upper())

lexer = AVRLexer(input_code)
stream = CommonTokenStream(lexer)
parser = AVRParser(stream)

tree = parser.program()

# Visiting
visitor = MyAVRVisitor()
visitor.visit(tree)
